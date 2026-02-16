# NLTK is the Natural Language Toolkit, a widely used, open-source Python library for processing and analyzing human language data.
# VADER (Valence Aware Dictionary and sEntiment Reasoner) is a popular lexicon and rule-based sentiment analysis tool that is included within the NLTK library. 





import requests
import pandas as pd
import time
from datetime import datetime
import sys
import re

import random

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry



def extract_product_id(url):

    match = re.search(r"/(\d+)$", url)

    return match.group(1) if match else None




import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download("vader_lexicon", quiet=True)


                      

# ------------------------------------
# BestBuy Reviews API Scraper (2026)
# ------------------------------------

class BestBuyReviewAPIScraper:

    # ------------------------------------
    #5. Suggested solution for scraping challenges (ways to handle anti-scraping blockers e.g. rotating proxies,CAPTCHA bypass, or retry mechanisms, IP blocking.)
    # ------------------------------------

    # ------------------------------------
    #A. Rotating User-Agents (Prevents fingerprinting)
    # ------------------------------------
    
    USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Windows NT 10.0; rv:109.0)"
    ]

    BASE_URL = "https://www.bestbuy.ca/api/reviews/v2/products/{}/reviews"

    #constructor
    def __init__(self, product_id, max_reviews=500, delay=0.5, proxies=None):
        self.product_id = product_id
        self.max_reviews = max_reviews
        self.delay = delay
        self.proxies = proxies

        self.session = self._init_session()

        self.headers = {
            "Accept": "application/json",
            "Referer": f"https://www.bestbuy.ca/en-ca/product/{product_id}"
        }


    # Rotating User-Agent Helper
    def _get_headers(self):
        headers = self.headers.copy()
        headers["User-Agent"] = random.choice(self.USER_AGENTS)
        return headers

    # ------------------------------------
    #C. Retry Mechanism ( Handles rate limits, Handles temporary bans)
    # ------------------------------------
    
    def _init_session(self):
        session = requests.Session()

        retry = Retry(
            total=5,
            backoff_factor=1,
            status_forcelist=[403, 429, 500, 502, 503]
        )

        adapter = HTTPAdapter(max_retries=retry)

        session.mount("https://", adapter)

        return session


    def _build_params(self, page, sort_by):

        return {
            "source": "all",
            "lang": "en-CA",
            "pageSize": 100,
            "page": page,
            "sortBy": sort_by,
            "hasPhotosFilter": "false"
        }

    def scrape(self, sort_by="relevancy"):

        all_reviews = []

        page = 1

        while len(all_reviews) < self.max_reviews:

            params = self._build_params(page, sort_by)

            r = self.session.get(
                self.BASE_URL.format(self.product_id),
                params=params,
                headers=self._get_headers(),
                proxies=self.proxies,
                timeout=15
            )

            if r.status_code != 200:
                print("Request failed:", r.status_code)
                break

            data = r.json()

            reviews = data.get("reviews", [])

            if not reviews:
                break

            for rev in reviews:

                review_text = (
                    rev.get("text") or
                    rev.get("reviewText") or
                    rev.get("comment") or
                    rev.get("content", {}).get("body") or
                    rev.get("details", {}).get("body") or
                    ""
                )

                raw_date = (
                    rev.get("submissionDate") or
                    rev.get("submittedAt") or
                    rev.get("submissionTime") or
                    rev.get("createdAt") or
                    rev.get("submissionDateTime")
                )

                formatted_date = self._format_date(raw_date)


                reviewer = (
                    rev.get("author", {}).get("nickname") or
                    rev.get("authorName") or
                    rev.get("userNickname") or
                    rev.get("reviewerName") or
                    (rev.get("author") if isinstance(rev.get("author"), str) else None)
                )

                review = {
                    "pk": rev.get("id"),
                    "title": rev.get("title"),
                    "review_text": review_text.strip(),
                    "date": formatted_date,
                    "rating": rev.get("rating"),
                    "source": "bestbuy.ca",
                    "reviewer": reviewer
                }

                all_reviews.append(review)

                if len(all_reviews) >= self.max_reviews:
                    break

            print(f"Fetched page {page} | Total: {len(all_reviews)}")

            page += 1
            time.sleep(self.delay)

        return pd.DataFrame(all_reviews)

    def _format_date(self, raw):

        try:
            dt = datetime.fromisoformat(raw.replace("Z", ""))
            return dt.strftime("%Y-%m-%d")
        except:
            return None
        

# ------------------------------------
# Sentiment Analyzer (VADER)
# ------------------------------------

from nltk.sentiment import SentimentIntensityAnalyzer

class ReviewSentimentAnalyzer:

    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def preprocess(self, text):
        if not text:
            return ""
        return text.lower().replace("\n", " ").strip()

    def analyze(self, text):

        cleaned = self.preprocess(text)

        scores = self.analyzer.polarity_scores(cleaned)

        compound = scores["compound"]

        if compound >= 0.05:
            label = "Positive"
        elif compound <= -0.05:
            label = "Negative"
        else:
            label = "Neutral"

        return label, compound


# ------------------------------------
# 6. Business Context – Insights & Recommendations 
# ------------------------------------

from collections import Counter

ASPECT_KEYWORDS = {
    "camera": ["camera", "photo", "picture"],
    "battery": ["battery", "charge", "power"],
    "display": ["screen", "display"],
    "performance": ["fast", "slow", "lag"],
    "price": ["price", "cost", "expensive", "cheap"],
    "design": ["design", "look", "color"],
    "quality": ["quality", "build", "durable"]
}

def extract_aspects(text):

    found = []

    text = text.lower()

    for aspect, words in ASPECT_KEYWORDS.items():
        for w in words:
            if w in text:
                found.append(aspect)
                break

    return found


def generate_business_insights(df):

    positive_df = df[df["sentiment"] == "Positive"]
    negative_df = df[df["sentiment"] == "Negative"]

    pos_aspects = []
    neg_aspects = []

    for text in positive_df["review_text"]:
        pos_aspects += extract_aspects(text)

    for text in negative_df["review_text"]:
        neg_aspects += extract_aspects(text)

    insights = {
        "total_reviews": len(df),
        "positive_drivers": Counter(pos_aspects).most_common(5),
        "negative_drivers": Counter(neg_aspects).most_common(5)
    }

    return insights

# ------------------------------------
# Runner
# ------------------------------------

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage:")
        print("python bestbuy_reviews_api_scraper.py <product_url>")
        exit(1)

    url = sys.argv[1]

    PRODUCT_ID = extract_product_id(url)

    if not PRODUCT_ID:
        print("Invalid product URL. Could not extract product ID.")
        exit(1)

    print("Using Product ID:", PRODUCT_ID)

    proxies = {
    "http": "http://user:pass@proxy:port",
    "https": "http://user:pass@proxy:port"
    }

    scraper = BestBuyReviewAPIScraper(
        product_id=PRODUCT_ID,
        max_reviews=5000,
        proxies=None #If you don’t actually own proxies, just pass None:( once you have proxies put it in proxies above and replace none with 'proxies' keyword. )
    )

    # Possible sorts: relevancy, newest, ratingHigh, ratingLow
    df = scraper.scrape(sort_by="relevancy")

    # Sentiment analysis
    sentiment_model = ReviewSentimentAnalyzer()

    sentiments = []
    scores = []

    for text in df["review_text"]:
        label, score = sentiment_model.analyze(text)
        sentiments.append(label)
        scores.append(score)

    df["sentiment"] = sentiments
    df["sentiment_score"] = scores

    #putting data into CSV
    df.to_csv("bestbuy_reviews_"+PRODUCT_ID+".csv", index=False)

    
    print("\nSaved:", len(df), "reviews to bestbuy_reviews_"+PRODUCT_ID+".csv")
   
    #printing Sentiments
    print("\nSentiment Distribution:")
    print(df["sentiment"].value_counts())

    print("------------------------------------")

    #Printing Insights
    insights = generate_business_insights(df)
    print("\nBusiness Insights:")
    print(insights)



