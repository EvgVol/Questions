from urllib.request import urlopen
from bs4 import BeautifulSoup


# html =  urlopen("https://www.pythonscraping.com/pages/warandpeace.html")
# bs = BeautifulSoup(html, "html.parser")


# ****************************************************************************

# поиск на странице по тегу
# ---------------------------
# nameList = bs.find_all('span', {'class': 'green'})
# for name in nameList:
#     print(name.get_text())


# ****************************************************************************

# поиск по слову
# ---------------------------
# nameList = bs.find_all(string="the prince")
# print(len(nameList))


# ****************************************************************************

# поиск по атрибуту
# ---------------------------
# title = bs.find_all(attrs={'id':'text'})
# print(title)


# ****************************************************************************

# поиск по атрибуту
# ---------------------------
# title = bs.find_all(attrs={'class': "red"})
# print(len(title))


# ****************************************************************************

# поиск по потомкам
# ---------------------------
# html =  urlopen("https://www.pythonscraping.com/pages/page3.html")
# bs = BeautifulSoup(html, "html.parser")
# s = []

# for child in bs.find("table", {'id':'giftList'}).children:
#     s.append(child)

# print(len(s))


# ****************************************************************************

# сбор данных из таблиц
# ---------------------------
# html =  urlopen("https://www.pythonscraping.com/pages/page3.html")
# bs = BeautifulSoup(html, "html.parser")
# for sibling in bs.find("table", {'id':'giftList'}).tr.next_siblings:
#     print(sibling)

#короткая форма
# for sibling in bs.table.tr.next_siblings: 
#     print(sibling)


# ****************************************************************************

# получение текста в предыдущем сиблинге
# ---------------------------
# html =  urlopen("https://www.pythonscraping.com/pages/page3.html")
# bs = BeautifulSoup(html, "html.parser")
# print(bs.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())


# ****************************************************************************


# вывод url изображений, используя регулярное выражение
# ---------------------------

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
# images = bs.find_all('img', {'src': re.compile('..\/img\/gifts/img.*.jpg')})
# for image in images:
#     print(image['src'])


# ****************************************************************************


