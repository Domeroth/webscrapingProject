# -*- coding: utf-8 -*-
import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class JudokaListsSpider(scrapy.Spider):
    name = 'judoka_list'

    try:
        with open("countries.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][2:]
    except:
        start_urls = []

    def parse(self, response):
        selection = response.xpath('//div[@class="results container-narrow"]/a/@href')
        for s in selection:
            l = Link()
            l['link'] = 'https://www.ijf.org' + s.get() + "/results?results_rank_group=all"
            yield l

