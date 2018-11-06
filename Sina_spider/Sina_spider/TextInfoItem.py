import scrapy

class TextInfoItem(scrapy.Item):
    title=scrapy.Field()
    time=scrapy.Field()