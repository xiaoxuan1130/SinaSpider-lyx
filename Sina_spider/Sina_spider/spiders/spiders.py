#coding=utf8
import scrapy

from Sina_spider.TextInfoItem import TextInfoItem


class NewsSpider3(scrapy.Spider):

    name='sinaSpider'


    ##主站链接
    base_site='http://www.cbdio.com/'

    start_urls=[
        'http://www.cbdio.com/node_2570.htm'
    ]

    def parse(self, response):
        liList= response.css('.cb-media>ul>li')
        for str in liList:
            url=str.xpath('p/a/@href').extract_first()
            url=self.base_site+url
            yield scrapy.Request(url,callback=self.getInfo)

    def getInfo(self,response):
        item=TextInfoItem()
        item['title']= response.css(".cb-article-title").extract_first(),
        item['time'] = response.css(".cb-article-info>span:nth-child(2)").extract_first()
        return item


