import scrapy
import requests
from scrapy.http import Request
from bs4 import BeautifulSoup

from myrss.items import IpsPool


class AgencySpider(scrapy.Spider):
    name = 'agency'
    allowed_domains = ['ip.ihuan.me']
    start_urls = ['https://ip.ihuan.me/address/5Lit5Zu9.html']

    def parse(self, response):
        html = BeautifulSoup(response.text, 'lxml')
        pages = html.find('ul', class_='pagination').find_all('a')
        paths = self.parse_page(pages)
        # for path in paths:
        #     next_page = self.start_urls[0] + path[0]
        #     yield Request(next_page, callback=self.parse_ips)
        return Request(self.start_urls[0] + paths[0][0], callback=self.parse_ips)

    def parse_ips(self, response):
        page = BeautifulSoup(response.text, 'lxml')
        items = page.find('tbody').find_all('tr')
        items = list(map(self.parse_ip, items))

    def parse_page(self, pages):
        def parse_path(page):
            return (page.string, page['href'])

        pages.pop()
        pages.pop(0)
        return list(map(parse_path, pages))

    def parse_ip(self, item):
        ips_pool = IpsPool()
        item = item.find_all('td')     
        ip = item[0].find('a').contents[1]
        port = item[1].string
        protocol = 'https' if item[4].string == '支持' else 'http'

        if port == '80':
            agency = '{}://{}'.format(protocol, ip)
        else:
            agency = '{}://{}:{}'.format(protocol, ip, port)

        res = requests.get('https://www.baidu.com/', proxies={protocol: agency})
        if res.status_code == 200:
            ips_pool['protocol'] = protocol
            ips_pool['ip'] = ip
            ips_pool['port'] = port
            ips_pool['agency'] = agency

        yield ips_pool