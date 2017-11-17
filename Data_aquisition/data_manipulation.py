import requests
from bs4 import BeautifulSoup
import re

# scrapy returns hindi as unicode so I used bs4
html = requests.request('GET','https://hi.wikipedia.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B5_%E0%A4%95%E0%A5%87_%E0%A4%B8%E0%A4%AD%E0%A5%80_%E0%A4%A6%E0%A5%87%E0%A4%B6')
html_doc = html.content

soup = BeautifulSoup(html_doc, 'html.parser')
for link in soup.find_all('a','mw-redirect'):
    print(link.text)


''' Japanense In [24]: response.css("table.wikitable td::text").extract()
file = open('countries_japanese','rt', encoding='UTF8')
for idx, i in enumerate(file.readlines()):
    if i.find('（') is not -1:
        print(i.strip('\n').strip(',').strip(' \'').strip('（').strip('）'))
        '''

''' Korean response.css("span.flagicon a::attr(title)").extract()
file = open('countries_korean','rt', encoding='UTF8')
for idx, i in enumerate(file.readlines()):
    print(i.strip('\n').strip(',').strip(' \'').strip('（').strip('）'))'''

#English In [13]: response.css("b a::attr(title)").extract()
'''
file = open('./countries_language/countries_english','rt', encoding='UTF8')
for idx, i in enumerate(file.readlines()):
    print(i.strip('\n').strip(',').strip(' \'').strip('（').strip('）'))'''

#Urdu
'''
file = open('./countries_language/countries_urdu','rt', encoding='UTF8')
list = []
for idx, i in enumerate(file.readlines()):
    print(i.strip('\n'))
    list.append(i.strip('\n'))

for string in list:
    print(re.split(string=string,pattern='svg')[1])
'''