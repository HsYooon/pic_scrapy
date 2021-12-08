from urllib import response
from flask import Flask
import datetime
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import logging

import requests
import json

from pic_scrapy.pic_scrapy.spiders.myspider import MyspiderSpider

app = Flask(__name__)

url = 'https://unsplash.com/s/photos/summer'

@app.route('/')
def home():
    logging.info('------home()----->')
    result = fetch()
    logging.info(f'------result: {result}')
    return "home"

def fetch():
    logging.info('------fetch()----->')
    params = {
        'spider_name' : 'myspider',
        'start_requests' : True,
        'url' : url
    }
    response = requests.get('http://localhost:9080/crawl.json', params)
    data = json.loads(response.text)
    data_list = []
    for item in data["items"]:
        data_list.append(item["img"].strip())
    print(data_list)
    return data_list

if __name__ == '__main__':
    app.run()
