import scrapy


class AgencySpider(scrapy.Spider):
    name = 'agency'
    allowed_domains = ['ip.ihuan.me']
    start_urls = ['https://ip.ihuan.me/']

    def parse(self, response):
        pass
