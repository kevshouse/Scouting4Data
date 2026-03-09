import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Target URL
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
headers = {"User-Agent": "PortfolioProject/1.0 (Contact: your-email@example.com)"}

print(f"🚀 Starting extraction on: {url}...")

# 2. Fetch and Parse
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Find the "External Links" Section
# In Wikipedia, external links are usually in a <ul> under a specific ID
external_links = []
for link in soup.find_all('a', href=True):
    href = link['href']
    # Filter: We only want links starting with 'http' (External)
    # This ignores internal '/wiki/...' links
    if href.startswith('http'):
        external_links.append({
            "Link Text": link.text.strip() or "No Title",
            "URL": href
        })

# 4. Save to CSV
df = pd.DataFrame(external_links)
df.to_csv("external_links.csv", index=False)

print(f"✅ Success! Extracted {len(external_links)} links to 'external_links.csv'.")