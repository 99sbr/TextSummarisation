# -*- coding: utf-8 -*-
import scrapy


class ContentSpider(scrapy.Spider):
    name = "content_getter"

    # This method must be in the spider,
    # and will be automatically called by the crawl command.
    def start_requests(self):
        self.index = 0
        urls = [
            'https://www.dnb.com/business-directory/company-profiles.ficofi_hong_kong_limited.b2dcb1a99345335ac36fb9dbf4d6f0d3.html',
        ]
        for url in urls:
            # We make a request to each url and call the parse function on the http response.
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = "kitten_response" + str(self.index)
        with open(filename, 'wb') as f:
            # All we'll do is save the whole response as a huge text file.
            f.write(response.body)
        self.log('Saved file %s' % filename)