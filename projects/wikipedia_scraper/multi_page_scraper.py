import logging
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time  # Essential for "Rate Limiting"
from datetime import datetime
import random

# 1. INFRASTRUCTURE & PATH SETUP
# Using the script's own location as the base to avoid path errors
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(BASE_DIR, "data", "targets")
RESULTS_DIR = os.path.join(BASE_DIR, "data", "results")

# Ensure directories exist immediately
os.makedirs(TARGET_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# 2. LOGGING SETUP
logging.basicConfig(
    filename=os.path.join(RESULTS_DIR,"wikipedia_scraper_activity.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 3. DATA LOADING (The "Notice" Phase)
file_path = os.path.join(TARGET_DIR, "urls.txt")
urls = []

try:
    with open(file_path, "r", encoding="utf-8") as file:
        urls = [line.strip() for line in file if line.strip()]
    if urls:
        logging.info(f"📂 Loaded {len(urls)} URLs from {file_path}")
        print(f"✅ Successfully loaded {len(urls)} URLs.")
except FileNotFoundError:
    logging.error(f"❌ File not found: {file_path}")
    print(f"❌ Error: {file_path} is missing.")
    urls = []

# 4. GUARD CLAUSE
if not urls:
    logging.warning("⛔ No URLs to scrape. Exiting script.")
    print(f"👉 ACTION: Please add links to: {file_path}")
    exit()

# 5. OUTPUT CONFIGURATION
today = datetime.now().strftime("%Y-%m-%d")
output_path = os.path.join(RESULTS_DIR, f"master_wikipedia_data_{today}.csv")
# --- Automated Rate Limiting ---
# Wait 2-5 seconds between pages to look like a human

headers = {"User-Agent": "DataScoutPortfolio/1.0 (Contact: your-email@example.com)"}
all_data = []

logging.info("🚀 SCRAPER STARTED")

for url in urls:
    print(f"🔍 Scraping: {url.split('/')[-1]}...")
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        if response.status_code == 200:
            logging.info(f"✅ Successfully scraped: {url}")
            # Extract title and first paragraph
            title = soup.find('h1').text
            summary = soup.find('p', class_=None).text.strip()

            all_data.append({"Title": title, "URL": url, "Summary": summary})
        
            # --- Rate Limiting ---
            # Wait 2-5 seconds between pages to look like a human
            wait_time = random.uniform(2, 5)
            print(f"⏳ Waiting {wait_time:.2f}s to be polite...")
            time.sleep(wait_time)
        else:
            logging.warning(f"⚠️ Received status code {response.status_code} for {url}")
            
        time.sleep(random.uniform(1, 3))  # Short wait before processing data

    except Exception as e:
        # Instead of just printing, log the full error details
        logging.exception(f"❌ CRITICAL ERROR scraping {url}")
        print(f"❌ Error scraping {url}: {e}")

# 2. Save all results at once
df = pd.DataFrame(all_data)
df.to_csv(output_path, index=False) # Use the new variable here!
print(f"✅ Done! All data saved to {output_path}")

