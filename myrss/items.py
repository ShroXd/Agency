# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyrssItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class IpsPool(scrapy.Item):

    # 代理池
    protocol = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    agency = scrapy.Field()