#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import httplib2 as httplib2

from web.models import Good


def parse_taobao(shop):
    url = re.search('https://.*\..*\.com', shop.url).group()
    host = url[8:]
    referer = 'http://' + host
    print host
    print referer
    http = httplib2.Http()
    http.follow_all_redirects = False

    headers_template = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Charset': 'UTF-8,*;q=0.5',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': host,
        'Referer': referer,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'cookie2=9cd772dd187e165d8d9cbba701b935b5; t=65af5e3ef1b39313d58971b6b638418f; _tb_token_=cYDIh0Iv0L88;',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36',
    }

    headers = headers_template.copy()
    resp, content = http.request(shop.url, 'GET', headers=headers)

    if resp['status'] == '302':
        headers = headers_template.copy()
        headers['Cookie'] = resp['set-cookie']
        resp, content = http.request(resp['location'], headers=headers)

    goods = []
    for each_content in re.finditer('<a [^>/]*?class=\\\\"J_TGoldData\\\\".*?<\/a>', content):
        good = Good()
        good.url = re.search('href=\\\\".*?\\\\"', each_content.group()).group().lstrip('href=\\"//').rstrip('\\"')
        good.img = re.search('lazyload=\\\\".*?\\\\"', each_content.group()).group().lstrip('lazyload=\\"//').rstrip('\\"')
        goods.append(good)
    return goods