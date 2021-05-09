# -*- coding: utf-8 -*-
import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class CountryListsSpider(scrapy.Spider):
    name = 'country_list'
    start_urls = ['https://www.ijf.org/judoka']


    def parse(self, response):
        selection = response.xpath('//select[@name="nation"]/option/@value')
        for s in selection:
            l = Link()
            l['link'] = 'https://www.ijf.org/judoka?name=&nation=' + s.get() + "&gender=both&category=sen"
            yield l

