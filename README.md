# 📊 ReviewInsight Pro  
### BestBuy Review Scraper & Sentiment Intelligence Tool

ReviewInsight Pro is a Python-based automated analytics tool that extracts customer reviews from **BestBuy Canada**, performs **sentiment analysis**, and generates **business insights** from customer feedback.

This project uses BestBuy’s official public API and applies Natural Language Processing (NLP) techniques to classify and analyze reviews.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
[![GitHub stars](https://img.shields.io/github/stars/gopitsinghal/yt-play?style=social)](https://github.com/gopitsinghal/yt-play/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/gopitsinghal/yt-play?style=social)](https://github.com/gopitsinghal/yt-play/network/members)  
---

## 🚀 Why ReviewInsight Pro?

- 🔎 Automated Review Extraction
- 🧠 Sentiment Intelligence (Positive / Neutral / Negative)
- 📈 Business Driver Analysis
- 🛡 Anti-Scraping Protection Mechanisms
- 📁 Clean CSV Export
- 🔄 Multi-Product Support
- 💻 Fully Offline Sentiment Support

---

## 📦 Features

### ✅ Web Scraping (API-Based)
- Extracts publicly available reviews
- Uses BestBuy Reviews API
- Supports pagination
- Supports sorting:
  - Relevancy
  - Newest
  - Highest Rating
  - Lowest Rating


### ✅ Extracted Fields

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


### ✅ Sentiment Analysis
- Uses **NLTK VADER**
- Lexicon + Rule-based model
- Offline capable
- Categorizes reviews into:
  - Positive
  - Neutral
  - Negative


### ✅ Anti-Scraping Protection
- Rotating User-Agents
- Retry mechanism (403, 429, 500 handling)
- Optional proxy support
- Rate limiting
- Session-based requests


### ✅ Business Insights Engine
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

## 1️⃣ Install Python

Download Python 3.9+:

👉 https://www.python.org/downloads/

During installation:

✔ Add Python to PATH


Verify installation:
Open a terminal (or PowerShell) inside the folder :

```bash
python --version
```

## 2️⃣ Clone Repository
```bash
git clone https://github.com/gopitsinghal/reviewinsight-pro.git
cd reviewinsight-pro
```

Or download ZIP and extract.

## 3️⃣ Create Virtual Environment (Recommended)
🔹 Windows
```bash
python -m venv venv
venv\Scripts\activate
```

🔹 macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see (venv) in terminal.

## 4️⃣ Install Required Packages
```bash
pip install requests pandas nltk urllib3 collections
```

## 5️⃣ Install VADER (Sentiment Model)
✅ If Internet Available
Open Python:
```bash
import nltk
nltk.download("vader_lexicon")
```

### ❗ If Offline (Manual Installation Method)

If NLTK download fails due to network restrictions, follow these steps:

Step 1: Download VADER Lexicon

    Download manually from:
    👉 https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/sentiment/vader_lexicon.zip
    Extract the file.
---

Step 2: Create Required Folder Structure
  Go to:
  C:\Users\<your-username>\AppData\Roaming\nltk_data

Create this exact structure:
```
nltk_data
 └── sentiment
      └── vader_lexicon.zip
           └── vader_lexicon
                └── vader_lexicon.txt
```

### Important:
- Create a folder named vader_lexicon.zip (even though it's a folder)
- Place vader_lexicon.txt inside it

---

Step 3: Verify Installation
Run:
```bash
python VADER_verifier.py
```
If no error appears → Setup successful.

## ▶️ How to Run the Tool
Use this command:
```bash
python bestbuy_reviews_api_scraper.py "<product_url>"
```

Example
**python bestbuy_reviews_api_scraper.py "https://www.bestbuy.ca/en-ca/product/samsung-galaxy-s25-fe-128gb-jet-black-unlocked/19411402"**

---

# 📁 Output
## 📸 Screenshots
### Main UI  
![Webpage Screenshot](./Output.png) 
![CMD Output Screenshot](./Output.png) 
![Excel CSV Screenshot](./Output.png) 
After execution:
**CSV file generated:**
  ``` bestbuy_reviews_<product_id>.csv ```

**Console displays:**
  - Total reviews fetched
  - Sentiment distribution
  - Business insights summary

## 🔄 Sorting Options

Inside the script you can modify:
```bash
df = scraper.scrape(sort_by="relevancy")
```
Available options:
| Options | Description |
|-------|-------------|
| relevancy	| Most relevant |
| newest | Most recent |
| ratingHigh | Highest rating |
| ratingLow |	Lowest rating | 


## 🌐 Using Proxies (Optional)

If you own proxies:
```
proxies = {
    "http": "http://user:pass@proxy:port",
    "https": "http://user:pass@proxy:port"
}
```
**Then pass:**
  ``` proxies=proxies ```
**If not using proxies**:
  ``` proxies=None ```

## 📊 Sample Business Insight Output
```bash
{
  "total_reviews": 988,
  "positive_drivers": [
    ["camera", 210],
    ["battery", 185]
  ],
  "negative_drivers": [
    ["price", 95],
    ["performance", 40]
  ]
}
```
---

## 🛡 Ethical Scraping Notice
- Only publicly available data is accessed
- No login required
- No authentication bypass
- No private information collected
- API-based structured extraction
- Respectful request frequency
This project is intended for educational and research purposes only.

## 📉 Limitations
- Works only for BestBuy Canada
- Dependent on API availability
- Keyword-based aspect extraction
- Lexicon-based sentiment (limited sarcasm detection)

## 🚀 Future Improvements
- BERT-based sentiment analysis
- Topic modeling
- Web dashboard (Streamlit)
- Multi-platform scraping
- Visualization layer
- Real-time monitoring

## 🎯 Use Cases
- Market research
- Customer feedback analytics
- Academic research
- Business intelligence
- Product improvement strategy
---

## 👨‍💻 Author

**Developed by: Gopit Singhal
Project Type: Data Engineering + NLP
Year: 2026**
