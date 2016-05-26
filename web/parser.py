#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import httplib2 as httplib2
import requests

from web.models import Good
http = httplib2.Http()

def parse_taobao(shop):
    shop_index_url = re.search('https://.*\..*\.com', shop.url).group()
    session = requests.Session()
    session.headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}
    session.get(shop_index_url)
    r = session.get(shop.url)

    goods = []
    for each_content in re.finditer('<a [^>/]*?class=\\\\"J_TGoldData\\\\".*?<\/a>', r.text):
        good = Good()
        good.url = re.search('href=\\\\".*?\\\\"', each_content.group()).group().lstrip('href=\\"//').rstrip('\\"')
        good.img = re.search('lazyload=\\\\".*?\\\\"', each_content.group()).group().lstrip('lazyload=\\"//').rstrip('\\"')
        goods.append(good)
    return goods