from urllib.request import urlopen
from bs4 import BeautifulSoup
from models.db_article import Article
import mlab
from datetime import datetime

url = 'http://genk.vn/co-1000-usd-ban-se-lam-gi-xiaomi-goi-y-ban-quat-pocophone-f1-ngon-hon-bo-tien-mua-iphone-2018-20180913185721318.chn'
mlab.connect()

html_content = urlopen(url).read().decode('UTF-8')
soup = BeautifulSoup(html_content,'html.parser')

title = soup.find('h1', 'kbwc-title clearfix').string.replace('\r\n', '')
sapo = soup.find('h2', 'knc-sapo').string
thumbnail = (soup.find('div', 'VCSortableInPreviewMode noCaption active').find('div').find('img'))['src']
contents = soup.find('div', 'knc-content').find_all('p', '')
content = ""
for i in contents:
    content = content + str(i)
author = soup.find('span', 'kbwcm-author').string
str_time = (soup.find('span', 'kbwcm-time'))['title'].replace("T", " ").replace("+07:00", "")
time = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')

new_article = Article(
    title = title,
    sapo = sapo,
    thumbnail = thumbnail,
    content = content,
    author = author,
    time = time,
    category = "Tech"
)

new_article.save()