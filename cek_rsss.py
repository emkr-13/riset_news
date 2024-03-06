import feedparser
from urllib.parse import quote, unquote
import time
from playwright.sync_api import sync_playwright

search = "jokowi widodo"
berita = "cnnindonesia.com"

encoded_search = quote(search)
encoded_berita = quote(berita)

url = f'https://news.google.com/rss/search?q="{encoded_search}"%20%3A%3A%20{encoded_berita}%20after%3A2024-01-02%20before%3A2024-01-02&hl=id&gl=ID&ceid=ID:id'
print(url)
feed = feedparser.parse(url)

# Extract links from the feed entries
links = [entry.link for entry in feed.entries]

link_clean = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    for link in links:
        try:
            page.goto(link)
            response_url = unquote(page.url)
            link_clean.append(response_url)
        except Exception as e:
            print(f"An error occurred while fetching link: {link}")
            print(f"Error details: {e}")
            # Jika terjadi kesalahan, coba lagi setelah beberapa saat
            time.sleep(3)
            continue
    
    browser.close()

print(link_clean)
