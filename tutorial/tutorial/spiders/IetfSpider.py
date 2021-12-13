import scrapy
import w3lib.html

class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        #  <span class="subheading">
        return {
            'title': response.xpath('//span[@class="title"]/text()').get(),
            'subheading': response.xpath('//span[@class="subheading"]/text()').getall(),
            'author': response.xpath('//meta[@name="DC.Creator"]/@content').get(),
            'text': w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get())
        }