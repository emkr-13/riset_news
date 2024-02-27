import requests
from bs4 import BeautifulSoup
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Google search URL
GOOGLE_SEARCH_URL = 'https://www.google.com/search'

# Headers to simulate a real user visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def fetch_search_results(query, start_page):
    """ Fetches search results for a given query """
    logging.info(f"Fetching search results for page starting at {start_page}")
    params = {
        'q': query,
        'start': start_page
    }
    response = requests.get(GOOGLE_SEARCH_URL, headers=headers, params=params)
    if response.status_code == 200:
        logging.info("Successfully fetched search results")
    else:
        logging.warning(f"Failed to fetch search results, status code: {response.status_code}")
    return response.text

def parse_links(html):
    """ Parses links from the HTML of a Google search results page """
    logging.info("Parsing links from the HTML")
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for div in soup.find_all('div', class_='MjjYud'):
        a_tag = div.find('a', href=True)
        if a_tag and 'href' in a_tag.attrs:
            links.append(a_tag['href'])
    logging.info(f"Found {len(links)} links")
    return links

def main():
    # Number of pages to scrape
    num_pages = 2
    all_links = []
    query='jokowi::cnn'
    for page in range(0, num_pages * 10, 10):
        logging.info(f"Processing search results page {page // 10 + 1}")
        html = fetch_search_results(query, page)
        links = parse_links(html)
        all_links.extend(links)
        time.sleep(2) # Respectful delay between requests

    # Log the final count of links
    logging.info(f"Total number of links collected: {len(all_links)}")

    # Do something with the links, e.g., print or save to a file
    for link in all_links:
        print(link)

if __name__ == '__main__':
    main()