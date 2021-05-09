from selenium import webdriver
import pandas as pd
import csv
import re
import time

limitPages = True
start = time.time()
gecko_path = '/usr/local/bin/geckodriver'

options = webdriver.firefox.options.Options()
options.headless = False

driver = webdriver.Firefox()

sportsmen = []
with open("judokaListFile.csv") as csvfile:
    judokaListFile = csv.reader(csvfile)
    for row in judokaListFile:
        sportsmen += row

# Gathering the data about competitors achievments from each individual page
judoka = []
d = pd.DataFrame(
    {"name": [], "age": [], "country": [], "wCat": [], "gold": [], "silver": [], "bronze": [], "other": []})

if limitPages:
    scrapedFile = sportsmen[:10]
else:
    scrapedFile = sportsmen

for link in scrapedFile:
    driver.get(link)

    try:
        # Targeting the Name without country, age, this time using regular expression
        toReplace = driver.find_element_by_xpath('//div[@class="athlete-title-hero"]').text
        name = re.sub("[\n]+.*", "", toReplace)
        print(name)
    except:
        name = ""
    try:
        age1 = driver.find_element_by_xpath('//div[@class="age-info"]').text
        age = age1.replace("Age: ", "").replace(" years", "")
    except:
        age = ""
    try:
        country = driver.find_element_by_xpath('//div[@class="location"]').text
    except:
        country = ""
    try:
        wCat = driver.find_element_by_xpath('//div[@class="kg"]').text
    except:
        wCat = ""
    try:
        other = driver.find_element_by_xpath('//table[@class="table table--athlete_results"]/tbody/tr['
                                             '@class="selected"]/td[@data-t="Other"]/a/div/').text
    except:
        other = ""
    try:
        bronze = driver.find_element_by_xpath('//table[@class="table table--athlete_results"]/tbody/tr['
                                              '@class="selected"]/td[@data-t="Bronze"]/a/div').text
    except:
        bronze = ""
    try:
        silver = driver.find_element_by_xpath('//table[@class="table table--athlete_results"]/tbody/tr['
                                              '@class="selected"]/td[@data-t="Silver"]/a/div').text
    except:
        silver = ""
    try:
        gold = driver.find_element_by_xpath('//table[@class="table table--athlete_results"]/tbody/tr['
                                            '@class="selected"]/td[@data-t="Gold"]/a/div').text
    except:
        gold = ""

    judoka = {'name': name, "age": age, "country": country, "wCat": wCat,
              "other": other, "bronze": bronze, "silver": silver, "gold": gold}

    d = d.append(judoka, ignore_index=True)

print(d)
d.to_csv("results.csv", index=False)

# Close browser:
driver.quit()
end = time.time()
print(end - start)
