import json
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import psutil

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

# Initialize Chrome webdriver directly with options
driver = webdriver.Chrome()

# Inisialisasi list kosong untuk menampung hasil akhir
links = []

# Inisialisasi list untuk menyimpan waktu yang dibutuhkan
times = []

# Inisialisasi variabel untuk menyimpan penggunaan memori
memory_usage = []

# Melakukan loop hingga tidak ada hasil pencarian lagi
page = 0
while True:
    start_time = time.time()  # Catat waktu awal
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
    if not search:  # Jika tidak ada hasil, hentikan loop
        break
    
    for h in search:
        links.append(h.a.get('href'))
        
    # Catat waktu akhir
    end_time = time.time()  
    # Hitung waktu yang dibutuhkan
    times.append(end_time - start_time)  
    # Hitung penggunaan memori
    memory_usage.append(psutil.Process().memory_info().rss)  
    
    page += 1

# Menyimpan links ke dalam file JSON
with open('chorme.json', 'w') as f:
    json.dump(links, f)

print("Links:", len(links))

# Menghitung total waktu yang dibutuhkan dan penggunaan memori
total_time = sum(times)
total_memory = sum(memory_usage)

print("Total Time:", total_time, "seconds")
print("Total Memory Usage:", total_memory / (1024 * 1024), "MB")  # Mengonversi dari byte ke MB

# Close the webdriver
driver.quit()
