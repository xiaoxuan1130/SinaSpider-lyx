#coding=utf8
import scrapy

from Sina_spider.StudentInfoItem import StudentInfoItem


class XuexinSpiders(scrapy.Spider):

    name='xuexinSpider'


    ##主站链接
    base_site='https://account.chsi.com.cn'

    start_urls=[
        'https://account.chsi.com.cn/account/account!show.action'
    ]

    def parse(self, response):
        item=StudentInfoItem()
        item['no']=response.css('.right-box>ul>li:nth-child(1)>strong>text()').extract_first()
        item['name']=response.css('#setName>strong').extract_first()
        return item


