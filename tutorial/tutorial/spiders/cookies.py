import scrapy
from scrapy.http import Request

class Cookies(scrapy.Spider):
    name = 'cookies'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/cookies/profile.php']

    """
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies={'username': 'Ayyaz','loggedin':'1'}, callback=self.parse)

    """
    def make_requests_from_url(self, url):
        request = super(Cookies, self).make_requests_from_url(url)
        request.cookies['username'] = 'Ayyaz!'
        request.cookies['loggedin'] = '1'
        return request

    def parse(self, response):
        return { 'text': response.xpath('//body/text()').get() }