# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class RawItem(Item):
    # define the fields for your item here like:
    raw_html = Field()
    url = Field()
    domain = Field()
    category = Field()
    money = Field()
    location = Field()
    date = Field()
    jobtitle = Field()
    jobdetial = Field()
    companyName = Field()
    companyUrl = Field()
    applyMethod = Field()
    
    pass



