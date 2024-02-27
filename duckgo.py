import json
from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = [r for r in ddgs.text("jokowi :: kompas", max_results=100)]

# Menyimpan hasil pencarian ke dalam file JSON
with open('search_results.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)

print("Hasil pencarian telah disimpan dalam file 'search_results.json'.")
