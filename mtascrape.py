import requests
import urllib
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

current_atag = soup.findAll('a')[35]
link = current_atag['href']
url_download = 'http://web.mta.info/developers/' + link

urllib.request.urlretrieve(url_download,'./'+link[link.find('/turnstile_')+1:])

