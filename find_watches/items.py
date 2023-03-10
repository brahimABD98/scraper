# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FindWatchesItem(scrapy.Item):
    name = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    img = scrapy.Field()
    status = scrapy.Field()
    website = scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
