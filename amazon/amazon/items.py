# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    
    item_name = scrapy.Field()
    item_price = scrapy.Field()
    item_imagelink = scrapy.Field()
    item_releaseDate = scrapy.Field()
    
