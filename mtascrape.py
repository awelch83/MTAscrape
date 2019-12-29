import requests
import urllib
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for i in range(35,len(soup.findAll('a'))+1):
    current_atag = soup.findAll('a')[i]
    link = current_atag['href']
    url_download = 'http://web.mta.info/developers/' + link
    urllib.request.urlretrieve(url_download,'./turnstile/'+link[link.find('/turnstile_')+1:])
    time.sleep(1)
