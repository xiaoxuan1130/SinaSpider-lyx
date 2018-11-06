#coding=utf8
import scrapy

from Sina_spider.TextInfoItem import TextInfoItem


class NewsSpider3(scrapy.Spider):

    name='iotSpider'


    ##主站链接
    base_site='http://www.iotcn.org.cn/'

    start_urls=[
        'http://www.iotcn.org.cn/cygc/'
    ]

    def parse(self, response):
        webcome=response.css(".menu>.menu-item-welcome::text").extract_first()
        if(webcome is None):
            webcome=response.css(".mobile_avatar>span::text").extract_first()
        print(webcome)
        liList= response.css('.content>.content-wrap>.box')
        for str in liList:
            url=str.xpath('article/h2/a/@href').extract_first()
            yield scrapy.Request(url,callback=self.getInfo)

    def getInfo(self,response):
        item=TextInfoItem()
        item['title']= response.css(".post-head>h2").extract_first(),
        item['time'] = response.css(".date").extract_first()
        return item


