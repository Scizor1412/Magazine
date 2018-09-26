from mongoengine import *

class Article(Document):
    title = StringField()
    sapo = StringField()
    thumbnail = StringField()
    content = StringField()
    time = StringField()
    author = StringField()
    level = IntField()
# 0 là chưa duyệt, 1 là đã duyệt và có thể hiển thị