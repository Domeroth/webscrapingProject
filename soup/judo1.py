from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS, NavigableString
import pandas as pd
import time

limitPages = True

start = time.time()
# Look at the page and the code
# Used this method based on https://stackoverflow.com/questions/16627227/http-error-403-in-python-3-web-scraping
req = Request('https://www.ijf.org/judoka', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
bs = BS(webpage, "html.parser")
# Looking for all different countries in the Nation dropdown
rList = bs.find('select', {"name": 'nation'})
children = rList.findAll("option")
# And now listing all of the links to different country pages for Category "All Seniors"
countryLinks = ["https://www.ijf.org/judoka?name=&nation=" + tag["value"] + "&gender=both&category=sen" for tag in
                children]
# for link in countryLinks:
#    print(link)
# Finding all athletes from certain countries:

sportsmen = []
for link in countryLinks[1:]:
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    bs = BS(webpage, 'html.parser')
    tags = bs.find_all('a', {"class": 'judoka'})
    link_temp_list = []
    for tag in tags:
        try:
            link_temp_list.append('https://www.ijf.org' + tag['href'])
        except:
            0
    sportsmen.extend(link_temp_list)
print(sportsmen)
# sportsmenTextFile = open("sportsmenTextFile.txt", "w")
# for element in sportsmen:
#     sportsmenTextFile.write(element + "\n")
# sportsmenTextFile.close()
d = pd.DataFrame(
    {"name": [], "age": [], "country": [], "wCat": [], "gold": [], "silver": [], "bronze": [], "other": []})
##
if limitPages:
    scrapedFile = sportsmen[:100]
else:
    scrapedFile = sportsmen
for athlete in scrapedFile:
    print(athlete)

    req = Request(athlete, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    bs = BS(html, 'html.parser')
    try:
        # Targeting the Name without country, age
        # name = bs.find("div", {"class":"athlete-title-hero"},recursive=False).get_text(strip=True)
        name1 = [node for node in bs.find("div", {"class": "athlete-title-hero"}).contents if
                 type(node) is NavigableString]
        name = name1[0].strip()
    except:
        name = ""
    try:
        age1 = bs.find("div", {"class": "age-info"}).get_text(strip=True)
        age = age1.replace("Age: ", "").replace(" years", "")
    except:
        age = ""
    try:
        country = bs.find("div", {"class": "location"}).get_text(strip=True)
    except:
        country = ""
    try:
        wCat = bs.find("div", {"class": "kg"}).get_text(strip=True)
    except:
        wCat = ""
    # Going to results page to gather medal data
    req = Request(athlete + "/results?results_rank_group=all", headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    bs = BS(html, 'html.parser')
    try:
        other = bs.find("div", {"class": "panel competitions-panel"}).find_previous("div").get_text(strip=True)
    except:
        other = ""
    try:
        bronze = bs.find("div", {"class": "panel competitions-panel"}).find_previous("div").find_previous(
            "div").get_text(strip=True)
    except:
        bronze = ""
    try:
        silver = bs.find("div", {"class": "panel competitions-panel"}).find_previous("div").find_previous("div") \
            .find_previous("div").get_text(strip=True)
    except:
        silver = ""
    try:
        gold = bs.find("div", {"class": "panel competitions-panel"}).find_previous("div").find_previous("div") \
            .find_previous("div").find_previous("div").get_text(strip=True)
    except:
        gold = ""
    judoka = {'name': name, "age": age, "country": country, "wCat": wCat,
              "other": other, "bronze": bronze, "silver": silver, "gold": gold}

    d = d.append(judoka, ignore_index=True)

print(d)

d.to_csv('judoka.csv')

end = time.time()
print(end - start)
