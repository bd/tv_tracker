# -*- coding: utf-8 -*-
import scrapy
from pprint import pprint

class HuluSpider(scrapy.Spider):
    name = 'hulu'
    allowed_domains = ['hulu.com']
    start_urls = ['http://hulu.com/',
                  'https://www.hulu.com/sitemap_index.xml',
                  '/api/2.0/static/page_content']

    def parse(self, response):
        '''
        Needs more research on parsing React pages.
        as of now, none of the xpath or css selectors
        I've pulled from the page yield anything very useful
        '''
        return None
