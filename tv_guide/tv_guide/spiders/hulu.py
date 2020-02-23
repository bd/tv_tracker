# -*- coding: utf-8 -*-
import scrapy


class HuluSpider(scrapy.Spider):
    name = 'hulu'
    allowed_domains = ['hulu.com']
    start_urls = ['http://hulu.com/']

    def parse(self, response):
        pass
