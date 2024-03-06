import feedparser
from urllib.parse import quote, unquote
from bs4 import BeautifulSoup
import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import psutil

# Renaming the file to avoid conflicts
search = "jokowi"
berita = "cnnindonesia.com"

encoded_search = quote(search)
encoded_berita = quote(berita)

url = f'https://news.google.com/rss/search?q="{encoded_search}"%20%3A%3A%20{encoded_berita}%20after%3A2024-01-02%20before%3A2024-01-02&hl=id&gl=ID&ceid=ID:id'
print(url)
feed = feedparser.parse(url)

# Extract links from the feed entries
links = [entry.link for entry in feed.entries]
print(len(links))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

link_clean = []
driver = webdriver.Chrome()
for link in links:
    driver.get(link)
    
    time.sleep(3)
    response_url = unquote(driver.current_url) 
    link_clean.append(response_url)
    
print(link_clean) 