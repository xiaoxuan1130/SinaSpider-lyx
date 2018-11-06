import scrapy

class StudentInfoItem(scrapy.Item):
    no=scrapy.Field()
    name=scrapy.Field()