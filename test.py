from serpapi import GoogleSearch

params = {
  "engine": "google",
  "q": "ganjar :: kompas",
  "api_key": "667e5834028b8e535dba919c3155be7a7a8e5cdf977794033a37a84140adfecf"
}

search = GoogleSearch(params)
results = search.get_dict()
# organic_results = results["organic_results"]
print(results)