import requests
import soupsieve.css_parser
from bs4 import BeautifulSoup
import time

st = time.time()
target_url = 'https://belese.com.tr/'

def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    return soup

Found_Links = []

def crawl(url):
    links = make_request(url)
    for link in links.find_all('a'):
        found_link = link.get('href')
        if found_link:
            if '#' in found_link:
                found_link = found_link.split('#')[0]
            if target_url in found_link and found_link not in Found_Links:
                Found_Links.append(found_link)
                print(found_link)
                crawl(found_link)


crawl(target_url)
ft = time.time()
et = ft-st
print('Total elapsed time is : ',et, 'second')
print('Total link count is : ',len(Found_Links))
