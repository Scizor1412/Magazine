from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://tructiep24h.com/la-liga/bang-xep-hang-la-liga-2018-19-barca-real-de-tho-dau-mua-24h2835'
conn = urlopen(url)

html_content = urlopen(url).read().decode('UTF-8')
soup = BeautifulSoup(html_content, 'html.parser')

title = soup.find("h1", 'title-news')
sapo = soup.find("p", 'content-brief')
thumbnail = soup.find("img", "img-detail-news").src