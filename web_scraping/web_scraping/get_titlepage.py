from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.h1
    except AttributeError as e:
        return None
    return title


title = getTitle('http://pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)
