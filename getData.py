#! /usr/bin/env python3
# coding: gbk
import requests
from bs4 import BeautifulSoup 

def main():
    C_CHAR = '��'
    hdr = {
            'Accept'            :   '*/*',
            'Accept-Encoding'   :   'gzip, deflate, br',
            'Accept-Language'   :   'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection'        :   'keep-alive',
            'User-Agent'        :   'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
    }
    req = requests.get("http://www.weather.com.cn/weather/101010100.shtml", headers=hdr)
    req.encoding='utf-8'
    soup = BeautifulSoup(req.text, features='html.parser')
    day = soup.find('li', class_='sky skyid lv1 on')
    wea = day.find('p', class_='wea')['title']
    tems = day.find('p', class_='tem')
    daytem = int(tems.find('span').text)
    nigtem = int(tems.find('i').text[:-1])
    
    wea = wea.replace('��', 'S')
    wae = wea.replace('����', 'C')
    wea = wea.replace('��', 'G')
    wea = wea.replace('С��', 'r')
    wea = wea.replace('����', 'R')
    wea = wea.replace('����', 's')
    wea = wea.replace('ת', ' ')
    return wea, daytem, nigtem, C_CHAR


if __name__=='__main__':
    print(main())

