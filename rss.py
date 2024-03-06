import feedparser
from urllib.parse import quote, unquote
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.options import Options

# Search query and target news source
search = "ganjar pranowo"
berita = "cnnindonesia.com"

# Encoding search query and news source for URL
encoded_search = quote(search)
encoded_berita = quote(berita)

# Generating Google News RSS feed URL for the search query and target news source
url = f'https://news.google.com/rss/search?q={encoded_search}%20%3A%3A%20{encoded_berita}%20after%3A2024-01-02%20before%3A2024-01-02&hl=id&gl=ID&ceid=ID:id'

# Parsing the RSS feed
feed = feedparser.parse(url)

# Extracting links from the feed entries
links = [entry.link for entry in feed.entries]

# Function to scrape URL with retries
def scrape_url_with_retry(url, max_retries=2):
    for attempt in range(max_retries):
        try:
            # Setting up Selenium options to run headless and stealth mode
            options = Options()
            options.add_argument("--headless")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)

            # Creating WebDriver instance
            driver = webdriver.Chrome(options=options)
            stealth(driver)

            # Opening URL in WebDriver
            driver.get(url)

            # Sleeping to ensure page is fully loaded
            time.sleep(3)

            # Getting unquoted URL (in case of redirects)
            response_url = unquote(driver.current_url)

            # Parsing page source with BeautifulSoup
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            # Extracting title
            title_elem = soup.find('h1', {"class": "mb-2 text-[28px] leading-9 text-cnn_black"})
            title_text = title_elem.text.strip() if title_elem else "Title not found"

            # Extracting content
            body_elem = soup.find('div', {"class": "detail-text text-cnn_black text-sm grow min-w-0"})
            if body_elem:
                content_elem = body_elem.find_all('p')
                content_text = " ".join(p.text.strip() for p in content_elem)
                content_text = content_text.replace("ADVERTISEMENT SCROLL TO CONTINUE WITH CONTENT", "").replace("ADVERTISEMENTSCROLL TO CONTINUE WITH CONTENT","")
            else:
                content_text = "Content not found"

            # Returning scraped data
            return {
                'title': title_text,
                'content': content_text,
                'link': response_url
            }
        except Exception as e:
            print(f"Error processing URL '{url}' (attempt {attempt+1}/{max_retries}): {e}")
            # Retry after a short delay
            time.sleep(5)

    # Return None if max retries reached without success
    return None

# List to store scraped data
scraped_data = []

# Scraping each URL in parallel
for url in links:
    data = scrape_url_with_retry(url)
    if data:
        scraped_data.append(data)

# Printing scraped data
for data in scraped_data:
    print(data)
