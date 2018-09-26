from urllib.request import urlopen
from bs4 import BeautifulSoup
from models.db_article import Article
import mlab

url = 'http://bongdanet.vn/tuong-thuat/u16-chau-a-2018-u16-thai-lan-vs-u16-tajikistan-15h30-ngay-26-9-tbd72636'
conn = urlopen(url)
mlab.connect()

html_content = urlopen(url).read().decode('UTF-8')
soup = BeautifulSoup(html_content, 'html.parser')

info = soup.find('div', 'article-text-info')
meta = info.find('meta', itemprop = 'author')
meta2 = info.find('meta', itemprop = "datePublished")
img = soup.find("img", "img-detail-news")
body = soup.find ('div', 'article-body')
contents = body.find_all('p')
content = []
for i in contents:
    content.append(i.string)
print (content)

new_article = Article(
    title = soup.find("h1", 'title-news').string,
    sapo = soup.find("p", 'content-brief').string,
    thumbnail = img['src'],
    content = content,
    author = meta['content'],
    time = meta2['content'],
)
