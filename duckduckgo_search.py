import json
import time
import psutil
from duckduckgo_search import DDGS

# Inisialisasi waktu awal
start_time = time.time()

with DDGS() as ddgs:
    results = [r for r in ddgs.text("jokowi::kompas", max_results=100)]

# Hitung waktu yang diperlukan
elapsed_time = time.time() - start_time

# Menyimpan hasil pencarian ke dalam file JSON
with open('search_results.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)

# Hitung penggunaan memori
memory_usage = psutil.Process().memory_info().rss

print("Hasil pencarian telah disimpan dalam file 'search_results.json'.")
print("Waktu yang diperlukan:", elapsed_time, "seconds")
print("Penggunaan memori:", memory_usage / (1024 * 1024), "MB")  
