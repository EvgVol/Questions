import re
import datetime
import random
from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup

random.seed(datetime.datetime.now().timestamp())

pages = set()

def getLinks(pageUrl):
    global pages

    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')

    elements = bs.find_all('a', href=re.compile('^(/wiki/)'))

    try:
        try:
            print(bs.h1.get_text())
            print(bs.find(id ='mw-content-text').find_all('p')[0])
            print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
        except AttributeError:
            print('This page is missing something!Continuing.')
        for link in elements:
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    newPage = link.attrs['href']
                    print('-'*20)
                    print(newPage)
                    pages.add(newPage)
                    getLinks(newPage)
    except HTTPError:
        pass


getLinks('')