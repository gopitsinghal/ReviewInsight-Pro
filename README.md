# 📊 ReviewInsight Pro  
### BestBuy Review Scraper & Sentiment Intelligence Tool

ReviewInsight Pro is a Python-based automated analytics tool that extracts customer reviews from **BestBuy Canada**, performs **sentiment analysis**, and generates **business insights** from customer feedback.

This project uses BestBuy’s official public API and applies Natural Language Processing (NLP) techniques to classify and analyze reviews.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
[![GitHub stars](https://img.shields.io/github/stars/gopitsinghal/yt-play?style=social)](https://github.com/gopitsinghal/yt-play/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/gopitsinghal/yt-play?style=social)](https://github.com/gopitsinghal/yt-play/network/members)  
---

# 🚀 Why ReviewInsight Pro?

- 🔎 Automated Review Extraction
- 🧠 Sentiment Intelligence (Positive / Neutral / Negative)
- 📈 Business Driver Analysis
- 🛡 Anti-Scraping Protection Mechanisms
- 📁 Clean CSV Export
- 🔄 Multi-Product Support
- 💻 Fully Offline Sentiment Support

---

# 📦 Features

## ✅ Web Scraping (API-Based)
- Extracts publicly available reviews
- Uses BestBuy Reviews API
- Supports pagination
- Supports sorting:
  - Relevancy
  - Newest
  - Highest Rating
  - Lowest Rating

---

## ✅ Extracted Fields

| Field | Description |
|-------|-------------|
| pk | Unique Review ID |
| title | Review Title |
| review_text | Full Review Content |
| date | Submission Date (YYYY-MM-DD) |
| rating | Rating (1–5) |
| source | bestbuy.ca |
| reviewer | Reviewer Name |
| sentiment | Sentiment Category |
| sentiment_score | Polarity Score |

---

## ✅ Sentiment Analysis
- Uses **NLTK VADER**
- Lexicon + Rule-based model
- Offline capable
- Categorizes reviews into:
  - Positive
  - Neutral
  - Negative

---

## ✅ Anti-Scraping Protection
- Rotating User-Agents
- Retry mechanism (403, 429, 500 handling)
- Optional proxy support
- Rate limiting
- Session-based requests

---

## ✅ Business Insights Engine
Analyzes keywords related to:
- Camera
- Battery
- Performance
- Display
- Price
- Design
- Quality

Outputs:
- Top positive drivers
- Top negative drivers
- Total review count

---

# 🛠 Installation Guide (Step-by-Step)

---

# 1️⃣ Install Python

Download Python 3.9+:

👉 https://www.python.org/downloads/

During installation:
