import asyncio
from bs4 import BeautifulSoup
from pyppeteer import launch
import time
import psutil

# Fungsi untuk melakukan crawling menggunakan pyppeteer dengan browser Firefox
async def crawl_google():
    browser = await launch(headless=True, executablePath='../.././../../usr/bin/brave-browser')
    page = await browser.newPage()

    links = []
    times = []
    memory_usage = []

    for page_num in range(n_pages):
        start_time = time.time()

        if page_num == 0:
            url = "https://www.google.com/search?q=jokowi+::+cnn&tbs=cdr:1,cd_min:01-02-2024,cd_max:01-02-2024&tbm=nws"
        else:
            url = f"https://www.google.com/search?q=jokowi+::+cnn&tbs=cdr:1,cd_min:01-02-2024,cd_max:01-02-2024&start={page_num * 10}&tbm=nws"

        await page.goto(url, timeout=30)  # Menambahkan opsi timeout yang lebih panjang (misalnya, 60 detik)
        await asyncio.sleep(3)

        html = await page.content()
        soup = BeautifulSoup(html, 'html.parser')

        search = soup.find_all('div', class_="SoaBEf")
        for h in search:
            links.append(h.a.get('href'))

        end_time = time.time()
        times.append(end_time - start_time)
        memory_usage.append(psutil.Process().memory_info().rss)

    await browser.close()

    return links, times, memory_usage

n_pages = 3

# Menjalankan fungsi crawling dan mendapatkan hasilnya
links, times, memory_usage = asyncio.get_event_loop().run_until_complete(crawl_google())

print("Links:", len(links))
print("Times:", times)
print("Memory Usage:", memory_usage)

# Menghitung total waktu yang dibutuhkan dan penggunaan memori
total_time = sum(times)
total_memory = sum(memory_usage)

print("Total Time:", total_time, "seconds")
print("Total Memory Usage:", total_memory / (1024 * 1024), "MB")
