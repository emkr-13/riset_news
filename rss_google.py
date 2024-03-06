import feedparser
from urllib.parse import quote, unquote
from bs4 import BeautifulSoup
import time
from playwright.sync_api import sync_playwright

# Renaming the file to avoid conflicts
search = "ganjar pranowo"
berita = "cnnindonesia.com"

encoded_search = quote(search)
encoded_berita = quote(berita)

url = f'https://news.google.com/rss/search?q={encoded_search}%20%3A%3A%20{encoded_berita}%20after%3A2024-01-02%20before%3A2024-01-02&hl=id&gl=ID&ceid=ID:id'
print(url)
feed = feedparser.parse(url)

# Extract links from the feed entries
links = [entry.link for entry in feed.entries]

# Scrape URL function
def scrape_url(url, max_retries=2):
    retries = 0
    while retries < max_retries:
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(url)
                time.sleep(5)  # Consider using wait_until for more robustness
                response_url = unquote(page.url)

                soup = BeautifulSoup(page.content(), 'html.parser')

                # Judul Berita
                title_elem = soup.find('h1', {"id": "arttitle"})
                title_text = title_elem.text.strip() if title_elem else "Title not found"

                body_elem = soup.find('div', {"class": "side-article txt-article multi-fontsize editcontent"})

                if body_elem:
                    content_elem = body_elem.find_all('p')
                    content_text = " ".join([p.text.strip() for p in content_elem])
                    content_text = content_text.replace('\n', '').replace('\r', '').replace('\t', '')
                else:
                    content_text = "Content not found"

                browser.close()
                return {
                    'title': title_text,
                    'content': content_text,
                    'link': response_url
                }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL '{url}': {e}")
        except Exception as e:
            print(f"Error processing URL '{url}': {e}")
        retries += 1
        if retries < max_retries:
            time.sleep(5)  # You can adjust the delay as needed
    return None

# List to store scraped data
scraped_data = []

print(len(links))
# Scrape each URL in parallel
for url in links:
    scraped_data.append(scrape_url(url))

# Print scraped data
for data in scraped_data:
    print(data)