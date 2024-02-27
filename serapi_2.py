import json
import psutil
import time
from serpapi import GoogleSearch

# Function to get current memory usage
def get_memory_usage():
    process = psutil.Process()
    return process.memory_info().rss  # Get memory usage in bytes

# Start time
start_time = time.time()

# Initial memory usage
initial_memory = get_memory_usage()

params = {
    "engine": "google",
    "q": "ganjar :: kompas",
    "api_key": "667e5834028b8e535dba919c3155be7a7a8e5cdf977794033a37a84140adfecf"
}

search = GoogleSearch(params)
results = search.get_dict()

# End time
end_time = time.time()
execution_time = end_time - start_time

# Final memory usage
final_memory = get_memory_usage()

# Memory used during execution
memory_used = final_memory - initial_memory

# Write results to file
with open('serapi.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)

# Print execution information
print("Hasil pencarian telah disimpan dalam file 'serapi.json'.")
print(f"Execution Time: {execution_time} seconds")
print(f"Memory Used: {memory_used / (1024 * 1024)} MB")  # Convert to MB for readability
