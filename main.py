from serpapi import GoogleSearch

params = {
    "q": "jokowi :: kompas ",
    "api_key": "667e5834028b8e535dba919c3155be7a7a8e5cdf977794033a37a84140adfecf",
    "start": 0,  # Adjust the starting point of the results
    "num": 7     # Number of results per page
}

all_results = []

for page_num in range(5):  # Example: iterate through 5 pages
    params["start"] = page_num * params["num"]
    search = GoogleSearch(params)
    results = search.get_dict()
    # Append results to the list of all results
    all_results.extend(results["organic_results"])
    
print(all_results)

# Now all_results contains all search results from multiple pages

# from serpapi import GoogleSearch
# search = GoogleSearch({})
# account = search.get_account()
