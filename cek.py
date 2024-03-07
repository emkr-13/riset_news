import requests
from bs4 import BeautifulSoup
import re

url = 'https://news.google.com/rss/articles/CBMic2h0dHBzOi8vd3d3LmNubmluZG9uZXNpYS5jb20vdGVrbm9sb2dpLzIwMjQwMjA1MTYzNDA5LTE5Mi0xMDU4OTEyL3Jpc2V0LWFuaWVzLXVuZ2d1bC10aXBpcy1kaS14LXByYWJvd28tcmFqYS10aWt0b2vSAXdodHRwczovL3d3dy5jbm5pbmRvbmVzaWEuY29tL3Rla25vbG9naS8yMDI0MDIwNTE2MzQwOS0xOTItMTA1ODkxMi9yaXNldC1hbmllcy11bmdndWwtdGlwaXMtZGkteC1wcmFib3dvLXJhamEtdGlrdG9rL2FtcA?oc=5'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Cari tag <link> dengan atribut rel="canonical"
canonical_link = soup.find('link', rel='canonical')

# Jika ditemukan, ambil URL-nya
if canonical_link:
    canonical_url = canonical_link.get('href')
    print("Canonical URL:", canonical_url)
else:
    print("Canonical URL tidak ditemukan.")
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
