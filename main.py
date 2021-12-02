from urllib import response
from flask import Flask
import datetime
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

import requests
import json

from pic_scrapy.pic_scrapy.spiders.myspider import MyspiderSpider

app = Flask(__name__)

@app.route('/')
def home():
    return 'ttttttttttttt'

@app.route('/second')
def second():
    params = {
        'spider_name' : 'myspider',
        'start_requests' : True
    }
    response = requests.get('http://localhost:9080/crawl.json', params)
    data = json.loads(response.text)
    src_list = []
    for item in data["items"]:
        src_list.append(item["img"].strip())
    print(src_list)
    return "response"

if __name__ == '__main__':
    app.run()
