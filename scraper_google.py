from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# Initialize Chrome webdriver directly with options
driver = webdriver.Chrome()

# Query to obtain links
query = 'jokowi::cnn'
links = [] # Initiate empty list to capture final results
# Specify number of pages on google search, each page contains 10 #links
n_pages = 11
for page in range(1, n_pages):
    # url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 1) + "&tbm=nws"
    url="https://www.google.com/search?q=jokowi+::+cnn?&tbs=cdr:1,cd_min:01-02-2024,cd_max:02-02-2024start=1&tbm=nws"
    # url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1) * 1)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # soup = BeautifulSoup(r.text, 'html.parser')

    search = soup.find_all('div', class_="yuRUbf")
    for h in search:
        links.append(h.a.get('href'))
        
print(links)
