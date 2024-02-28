from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import psutil

# Inisialisasi Playwright
with sync_playwright() as p:
    browser = p.firefox.launch()

    # Membuka halaman baru di browser Firefox
    page = browser.new_page()

    query = 'jokowi::cnn'
    links = []  # Inisialisasi list kosong untuk menampung hasil akhir
    # Tentukan jumlah halaman pada pencarian google, setiap halaman berisi 10 tautan
    n_pages = 3

    # Inisialisasi list untuk menyimpan waktu yang dibutuhkan
    times = []

    # Inisialisasi variabel untuk menyimpan penggunaan memori
    memory_usage = []

    for page_number in range(n_pages):
        start_time = time.time()  # Catat waktu awal
        if page_number == 0:
            url = "https://www.google.com/search?q=jokowi+::+cnn&tbs=cdr:1,cd_min:01-02-2024,cd_max:01-02-2024&tbm=nws"
        else:
            url = f"https://www.google.com/search?q=jokowi+::+cnn&tbs=cdr:1,cd_min:01-02-2024,cd_max:01-02-2024&start={page_number * 10}&tbm=nws"
        
        page.goto(url)
        page.wait_for_load_state("load")

        soup = BeautifulSoup(page.content(), 'html.parser')

        search = soup.find_all('div', class_="SoaBEf")
        for h in search:
            links.append(h.a.get('href'))
            
        end_time = time.time()  # Catat waktu akhir
        times.append(end_time - start_time)  # Hitung waktu yang dibutuhkan
        memory_usage.append(psutil.Process().memory_info().rss)  # Hitung penggunaan memori

    print("Links:", len(links))
    print("Times:", times)
    print("Memory Usage:", memory_usage)

    # Menghitung total waktu yang dibutuhkan dan penggunaan memori
    total_time = sum(times)
    total_memory = sum(memory_usage)

    print("Total Time:", total_time, "seconds")
    print("Total Memory Usage:", total_memory / (1024 * 1024), "MB")  # Mengonversi dari byte ke MB

    browser.close()
