import json
import time
import psutil
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

# Inisialisasi list kosong untuk menampung hasil akhir
links = []

# Inisialisasi list untuk menyimpan waktu yang dibutuhkan
times = []

# Inisialisasi variabel untuk menyimpan penggunaan memori
memory_usage = []

with sync_playwright() as p:
    browser = p.firefox.launch(headless=True)
    page = browser.new_page()

    # Melakukan loop hingga tidak ada hasil pencarian lagi
    page_number = 0
    while True:
        start_time = time.time()  # Catat waktu awal
        # Untuk page_number == 0, tidak perlu dikurangi 1
        if page_number == 0:
            url = "https://www.google.com/search?q=jokowi+::+cnn&tbs=cdr:1,cd_min:01-02-2024,cd_max:01-02-2024&tbm=nws"
        else:
            url = f"https://www.google.com/search?q=jokowi+::+cnn&tbs=cdr:1,cd_min:01-02-2024,cd_max:01-02-2024&start={page_number * 10}&tbm=nws"

        page.goto(url)
        page_content = page.content()
        soup = BeautifulSoup(page_content, 'html.parser')

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

        page_number += 1

    browser.close()

# Menyimpan links ke dalam file JSON
with open('firefox.json', 'w') as f:
    json.dump(links, f)

print("Links:", len(links))

# Menghitung total waktu yang dibutuhkan dan penggunaan memori
total_time = sum(times)
total_memory = sum(memory_usage)

print("Total Time:", total_time, "seconds")
print("Total Memory Usage:", total_memory / (1024 * 1024), "MB")  # Mengonversi dari byte ke MB
