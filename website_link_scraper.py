import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse


def googleSearch(query):
    cleaned = []
    url = 'https://www.google.com/search?client=ubuntu&channel=fs&q={}\
    &ie=utf-8&oe=utf-8'.format(query)
    try:
        html = requests.get(url)
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, "html.parser")
            a = soup.find_all('a') 
            for i in a:
                k = i.get('href')
                try:
                    m = re.search("(?P<url>https?://[^\s]+)", k)
                    n = m.group(0)
                    rul = n.split('&')[0]
                    domain = urlparse(rul)
                    if(re.search('google.com', domain.netloc)):
                        continue
                    else:
                        cleaned.append(rul)
                except:
                    continue
    except Exception as ex:
        print(str(ex))
    finally:
        return cleaned

result = []
for i in set(googleSearch("Car Service Provider")):
    if "quora" not in i:
        result.append(i)
        
with open("links.txt", "w") as fout:
    print(*result, sep="\n", file=fout)

print("Links Scraped!")
