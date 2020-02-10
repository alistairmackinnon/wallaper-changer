import os
from bs4 import BeautifulSoup
import requests
import urllib.request

# set urls
url = 'https://apod.nasa.gov/apod/astropix.html'
img_base_url = 'https://apod.nasa.gov/'

# get and parse files
resp = requests.get(url)
html = BeautifulSoup(resp.text, features="html.parser")
img = html.find('img')
img = img['src']
img_link = os.path.join(img_base_url, img)

# download image
urllib.request.urlretrieve(img_link, '/home/ali/Pictures/potd.jpg')

# refresh wallpaper
os.system('xfdesktop --reload')

