import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from DownloadFiles.items import DownloadfilesItem

class NirsoftSpider(CrawlSpider):
    name = 'download_files'
    allowed_domains = ['www.nirsoft.net']
    start_urls = ['http://www.nirsoft.net/']

    rules = (
        Rule(callback='parse_item', follow=True ),
    )

    def parse_item(self, response):
        file_url = response.css('.downloadline::attr(href)').get()
        file_url = response.urljoin(file_url)
        item = DownloadfilesItem()
        item['file_urls'] = [file_url]
        yield item