# Scouting4Data# 🕸️ Web Data Extraction Portfolio

A collection of professional Python scripts designed for structured data collection, cleaning, and automation.

## 🛠️ Tech Stack
- **Language:** Python 3.12+
- **Libraries:** BeautifulSoup4, Requests, Pandas
- **Environment:** Isolated Virtual Environments (venv)

## 📁 Project Structure
- `basic_summary.py`: A entry-level script that extracts the primary summary from a Wikipedia page and saves it to a structured CSV.
- `multi_page_scraper.py`: An automated pipeline that loops through multiple URLs, featuring **rate limiting** (to respect server load) and **error handling**.

## 🚀 Key Features
- **Ethical Scraping:** Implements `User-Agent` headers and `time.sleep()` delays to follow scraping best practices.
- **Data Integrity:** Uses Pandas for data normalization and export to CSV/Excel formats.
- **Resilient Logic:** Try-Except blocks ensure the pipeline continues even if a single URL fails.

## ⚙️ Setup
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/Scouting4Data.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run any script: `python projects/wikipedia_scraper/multi_page_scraper.py`