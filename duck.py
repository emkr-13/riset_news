import json
import time
import psutil
from duckduckgo_search import DDGS

# Inisialisasi waktu awal
start_time = time.time()

with DDGS() as ddgs:
    results = [r for r in ddgs.text("jokowi::kompas", max_results=100)]
