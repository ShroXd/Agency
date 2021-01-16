# Scrapy settings for myrss project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myrss'

SPIDER_MODULES = ['myrss.spiders']
NEWSPIDER_MODULE = 'myrss.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True


# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16


# Log
LOG_LEVEL = 'DEBUG'


# Middlewares
DOWNLOADER_MIDDLEWARES = {
    'myrss.middlewares.MyrssDownloaderMiddleware': 543,
    'myrss.middlewares.RandomUserAgentMiddleware': 544,

    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None
}


# Pipelines
ITEM_PIPELINES = {
    'myrss.pipelines.MyrssPipeline': 300,
}


# MongoDB
MONGO_URL = 'mongodb://localhost:27017/dev'
MONGO_DB = 'rss'
