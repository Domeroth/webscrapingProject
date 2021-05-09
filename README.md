TODO: write instruction how to run your scrapers.

soup:
run judo1.py
Looking for all different countries in the Nation dropdown
And now listing all of the links to different country pages for Category "All Seniors"
Going to results page to gather medal data
In the end the data is saved to 'judoka.csv'

scrapy:
put spiders into spiders folder

run

scrapy crawl country_list -O countries.csv

scrapy crawl judoka_list -O athletes.csv

scrapy crawl judoka -O results.csv

First spider gathers information from the main page country dropdown
Second spider uses information from the first spider, and for each country gathers information about competitors
Third spider visits each of the competitors site, and gathers information about them

Three files are created - each with the information gathered by a relevant spider

selenium: 
run judo5.py 
and then run
judo6.py
