from urllib import request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

# Look at the page and the code
#Used this method based on https://stackoverflow.com/questions/16627227/http-error-403-in-python-3-web-scraping
req = Request('https://www.ijf.org/judoka', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
bs = BS(webpage, "html.parser")

#Looking for all different countries in the Nation dropdown
rList = bs.find('select', {"name":'nation'})
children = rList.findAll("option")

#And now listing all of the links to different country pages
links = ["https://www.ijf.org/judoka?name=&nation=" + tag["value"] + "&gender=both&category=sen" for tag in children]

for link in links:
    print(link)


