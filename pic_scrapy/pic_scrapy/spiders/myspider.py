import scrapy
import json
from bs4 import BeautifulSoup

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    #start_urls = ['https://unsplash.com/s/photos/winter']

    # def __init__(self, category=None, *args, **kwargs):
    #     super(MyspiderSpider,self).__init__(*args, **kwargs)
    #     self.start_urls = []
    def parse(self, response):
        print("------spider.parse 실행 ---> ")
        for src in response.css('img.YVj9w::attr(srcset)'):
            temp = src.get().split(',')
            yield {
               'img' : temp[3]
            }

    def start_requests(self, request):
        url = request.url
        print("accept_request.rul ---> ")
        print(url)
        yield scrapy.Request(url=url, callback=self.parse)