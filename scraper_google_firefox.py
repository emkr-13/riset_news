from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Tentukan jalur ke driver Chrome di Ubuntu
chrome_driver_path = '/usr/bin/chromium-browser'


# Inisialisasi Chrome webdriver dengan jalur yang ditentukan
driver = webdriver.Chrome()

# Query untuk mendapatkan tautan
query = 'jokowi::cnn'
links = [] # Inisialisasi list kosong untuk menampung hasil akhir
# Tentukan jumlah halaman pada pencarian google, setiap halaman berisi 10 tautan
n_pages = 5
for page in range(n_pages):
    # Untuk page == 0, tidak perlu dikurangi 1
    if page == 0:
        url = "https://www.google.com/search?q=jokowi+::+cnn&tbs=cdr:1,cd_min:01-02-2024,cd_max:01-02-2024&tbm=nws"
    else:
        url = "https://www.google.com/search?q=jokowi+::+cnn&tbs=cdr:1,cd_min:01-02-2024,cd_max:01-02-2024" + "&start=" + str(page * 10) + "&tbm=nws"
    
    driver.get(url)
    
    # Tunggu 2 detik untuk memungkinkan halaman untuk dimuat
    time.sleep(3)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    search = soup.find_all('div', class_="SoaBEf")
    for h in search:
        links.append(h.a.get('href'))
        
print(links)
