from playwright.sync_api import sync_playwright
import time

url = 'https://news.google.com/rss/articles/CBMic2h0dHBzOi8vd3d3LmNubmluZG9uZXNpYS5jb20vdGVrbm9sb2dpLzIwMjQwMjA1MTYzNDA5LTE5Mi0xMDU4OTEyL3Jpc2V0LWFuaWVzLXVuZ2d1bC10aXBpcy1kaS14LXByYWJvd28tcmFqYS10aWt0b2vSAXdodHRwczovL3d3dy5jbm5pbmRvbmVzaWEuY29tL3Rla25vbG9naS8yMDI0MDIwNTE2MzQwOS0xOTItMTA1ODkxMi9yaXNldC1hbmllcy11bmdndWwtdGlwaXMtZGkteC1wcmFib3dvLXJhamEtdGlrdG9rL2FtcA?oc=5'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    time.sleep(5)  # Wait for 5 seconds
    response_url = page.url
    print(response_url)
    browser.close()
