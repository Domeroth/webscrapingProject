# -*- coding: utf-8 -*-
import scrapy


class Judoka(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()
    country = scrapy.Field()
    wCat = scrapy.Field()
    gold = scrapy.Field()
    silver = scrapy.Field()
    bronze = scrapy.Field()
    other = scrapy.Field()


class JudokaSpider(scrapy.Spider):
    name = "judoka"
    limitPages = True
    try:
        with open("athletes.csv", "rt") as f:
            if limitPages:
                start_urls = [url.strip() for url in f.readlines()][1:101]
            else:
                start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        p = Judoka()

        name_xpath = '//div[@class="athlete-title-hero"]/text()'
        age_xpath = '//div[@class="age-info"]/text()'
        country_xpath = '//div[@class="location"]/text()'
        wCat_xpath = '//div[@class="kg"]/text()'
        gold_xpath = '//table[@class="table table--athlete_results"]/tbody/tr[@class="selected"]/td[' \
                     '@data-t="Gold"]/a/div/text() '
        silver_xpath = '//table[@class="table table--athlete_results"]/tbody/tr[@class="selected"]/td[' \
                       '@data-t="Silver"]/a/div/text() '
        bronze_xpath = '//table[@class="table table--athlete_results"]/tbody/tr[@class="selected"]/td[' \
                       '@data-t="Bronze"]/a/div/text() '
        other_xpath = '//table[@class="table table--athlete_results"]/tbody/tr[@class="selected"]/td[' \
                      '@data-t="Other"]/a/div/text() '

        p['name'] = response.xpath(name_xpath).get().strip()
        p['age'] = response.xpath(age_xpath).get().strip().replace("Age: ", "").replace(" years", "")
        p['country'] = response.xpath(country_xpath).getall()[1].strip()
        p['wCat'] = response.xpath(wCat_xpath).get().strip()
        p['gold'] = response.xpath(gold_xpath).get().strip()
        p['silver'] = response.xpath(silver_xpath).get().strip()
        p['bronze'] = response.xpath(bronze_xpath).get().strip()
        p['other'] = response.xpath(other_xpath).get().strip()

        yield p
