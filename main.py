from urllib import response
from flask import Flask
import datetime
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import requests
import json

from pic_scrapy.pic_scrapy.spiders.myspider import MyspiderSpider

app = Flask(__name__)

@app.route('/')
def home():
    return "home"

@app.route('/red')
def red():
    print('------red()시작----->')
    # params = {
    #     'spider_name' : 'myspider',
    #     'url' : url
    # }
    #response = requests.get('http://localhost:9080/crawl.json', params)
    response = requests.get('http://localhost:9080/crawl.json?spider_name=myspider&callback=parse&url=https://unsplash.com/s/photos/red')
    data = json.loads(response.text)
    data_list = []
    dict = {}
    id = 0
    for item in data["items"]:
        dict['src'] = item["img"].strip().split(' ')[0]
        dict['id'] = id
        dict['sort'] = 'red'
        data_list.append(dict)
        dict={}
        id += 1
    print(data_list)
    return json.dumps(data_list)

@app.route('/yellow')
def yellow():
    print('------yellow()시작----->')
    # params = {
    #     'spider_name' : 'myspider',
    #     'url' : url
    # }
    #response = requests.get('http://localhost:9080/crawl.json', params)
    response = requests.get('http://localhost:9080/crawl.json?spider_name=myspider&callback=parse&url=https://unsplash.com/s/photos/yellow')
    data = json.loads(response.text)
    data_list = []
    dict = {}
    id = 0
    for item in data["items"]:
        dict['src'] = item["img"].strip().split(' ')[0]
        dict['id'] = id
        dict['sort'] = 'yellow'
        data_list.append(dict)
        dict={}
        id += 1
    print(data_list)
    return json.dumps(data_list)

@app.route('/green')
def green():
    print('------green()시작----->')
    # params = {
    #     'spider_name' : 'myspider',
    #     'url' : url
    # }
    #response = requests.get('http://localhost:9080/crawl.json', params)
    response = requests.get('http://localhost:9080/crawl.json?spider_name=myspider&callback=parse&url=https://unsplash.com/s/photos/green')
    data = json.loads(response.text)
    data_list = []
    dict = {}
    id = 0
    for item in data["items"]:
        dict['src'] = item["img"].strip().split(' ')[0]
        dict['id'] = id
        dict['sort'] = 'green'
        data_list.append(dict)
        dict={}
        id += 1
    print(data_list)
    return json.dumps(data_list)

@app.route('/purple')
def purple():
    print('------purple()시작----->')
    # params = {
    #     'spider_name' : 'myspider',
    #     'url' : url
    # }
    #response = requests.get('http://localhost:9080/crawl.json', params)
    response = requests.get('http://localhost:9080/crawl.json?spider_name=myspider&callback=parse&url=https://unsplash.com/s/photos/purple')
    data = json.loads(response.text)
    data_list = []
    dict = {}
    id = 0
    for item in data["items"]:
        dict['src'] = item["img"].strip().split(' ')[0]
        dict['id'] = id
        dict['sort'] = 'purple'
        data_list.append(dict)
        dict={}
        id += 1
    print(data_list)
    return json.dumps(data_list)

if __name__ == '__main__':
    app.run(host='192.168.0.19', debug=True)
