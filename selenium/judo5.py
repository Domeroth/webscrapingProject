from selenium import webdriver
from selenium.webdriver.support.ui import Select

gecko_path = '/usr/local/bin/geckodriver'
url = 'https://www.ijf.org/judoka'

options = webdriver.firefox.options.Options()
options.headless = False

driver = webdriver.Firefox()

# Actual program:
driver.get(url)

#Getting the country values from dropdown and converting them to list of countries
selection = Select(driver.find_element_by_xpath('//select[@name="nation"]'))
options = selection.options
countryList = []
for index in range (1, len(options)-1):
    countryList += ["https://www.ijf.org/judoka?name=&nation=" + (options[index].get_attribute('value')) + "&gender=both&category=sen"]
#saving the results
countryListFile = open("countryListFile.csv", "w")
for element in countryList:
    countryListFile.write(element + "\n")
countryListFile.close()

#Gathering the data about competitors in each country
judokaList = []
for link in countryList:
    driver.get(link)
    try:
        #selection = driver.find_element_by_xpath('//div[@class="results container-narrow"]/a').get_attribute("href")
        aTagsInLi = driver.find_elements_by_css_selector('div a')
        #I chose to select all a tags inside div tag - this is where links for competitors pages are located
        #I order to keep only the relevan links, I had to use "startswith" on a string
        for a in aTagsInLi:
            if str(a.get_attribute('href')).startswith("https://www.ijf.org/judoka/"):
                judokaList += [(a.get_attribute('href'))+ "/results?results_rank_group=all"]
    except:
        selection = "ERROR"
print(judokaList)

#saving the results
judokaListFile = open("judokaListFile.csv", "w")
for element in judokaList:
    judokaListFile.write(element + "\n")
judokaListFile.close()
# Close browser:
driver.quit()
