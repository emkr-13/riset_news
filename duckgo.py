from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = [r for r in ddgs.text("jokowi :: kompas", max_results=100)]
    print(results)