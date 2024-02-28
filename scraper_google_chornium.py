import asyncio
import json
import time
import psutil
from bs4 import BeautifulSoup
from pyppeteer import launch

# Inisialisasi list kosong untuk menampung hasil akhir
links = []

# Inisialisasi list untuk menyimpan waktu yang dibutuhkan
times = []

# Inisialisasi variabel untuk menyimpan penggunaan memori
memory_usage = []

async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()

    # Melakukan loop hingga tidak ada hasil pencarian lagi
    page_num = 0
    while True:
        start_time = time.time()  # Catat waktu awal
        
        if page_num == 0:
            url = "https://www.google.com/search?q=jokowi+::+cnn&tbs=cdr:1,cd_min:01-02-2024,cd_max:01-02-2024&tbm=nws"
        else:
            url = f"https://www.google.com/search?q=jokowi+::+cnn&tbs=cdr:1,cd_min:01-02-2024,cd_max:01-02-2024&start={page_num * 10}&tbm=nws"

        await page.goto(url)
        
        # Tunggu sebentar untuk memastikan halaman telah dimuat sepenuhnya
        await asyncio.sleep(2)  # Ganti dari page.waitForTimeout() menjadi asyncio.sleep()
        
        content = await page.content()
        soup = BeautifulSoup(content, 'html.parser')

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
        
        page_num += 1

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

# Menyimpan links ke dalam file JSON
with open('pyppeteer.json', 'w') as f:
    json.dump(links, f)

print("Links:", len(links))

# Menghitung total waktu yang dibutuhkan dan penggunaan memori
total_time = sum(times)
total_memory = sum(memory_usage)

print("Total Time:", total_time, "seconds")
print("Total Memory Usage:", total_memory / (1024 * 1024), "MB")  # Mengonversi dari byte ke MB
