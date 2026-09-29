import requests
from bs4 import BeautifulSoup

def scrape():
    print('\n========== WEB SCRAPING ==========')
    try:
        r=requests.get('https://example.com',timeout=10); r.raise_for_status(); soup=BeautifulSoup(r.text,'html.parser'); print('Page Title:',soup.title.get_text(strip=True) if soup.title else 'None'); print('Headings:')
        for h in soup.find_all(['h1','h2','h3']): print('-',h.get_text(strip=True))
    except requests.RequestException as e: print('Web scraping error:',e)
