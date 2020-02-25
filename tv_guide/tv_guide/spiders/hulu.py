# -*- coding: utf-8 -*-
from pprint import pprint

from scrapy.spiders import SitemapSpider

class HuluSitemap(SitemapSpider):
    name = 'hulu_sitemap'
    allowed_domains = ['hulu.com']
    sitemap_urls = ['https://www.hulu.com/sitemap_index.xml']

    def sitemap_filter(self, entries):
        for entry in entries:
            if 'hulu.com/series/' in entry['loc']:
                yield entry

    def parse(self, response):
        # response.selector.remove_namespaces()
        return response.xpath('//*')


