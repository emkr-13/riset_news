import requests
from bs4 import BeautifulSoup
import re

url = 'https://news.google.com/rss/articles/CBMidGh0dHBzOi8vd3d3LmNuYmNpbmRvbmVzaWEuY29tL25ld3MvMjAyNDAyMDYxMzUyNDgtNC01MTIyODcvbGVtYmFnYS1hc2luZy1zdXJ2ZWktcGVtZW5hbmctcGlscHJlcy1yaS1jYXByZXMtaW5pLWp1YXJh0gF4aHR0cHM6Ly93d3cuY25iY2luZG9uZXNpYS5jb20vbmV3cy8yMDI0MDIwNjEzNTI0OC00LTUxMjI4Ny9sZW1iYWdhLWFzaW5nLXN1cnZlaS1wZW1lbmFuZy1waWxwcmVzLXJpLWNhcHJlcy1pbmktanVhcmEvYW1w?oc=5'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# # Cari skrip yang mengandung 'CommentComponent'
# comment_script = soup.find('script', string=re.compile(r'CommentComponent'))

# # Jika skrip ditemukan, ekstrak URL-nya
# if comment_script:
#     match = re.search(r"url\s*:\s*'([^']*)'", comment_script.string)
#     if match:
#         comment_url = match.group(1)
#         print("URL dari CSS:", comment_url)
#     else:
#         print("URL tidak ditemukan dalam script.")
# else:
#     print("Script tidak ditemukan dalam halaman.")
