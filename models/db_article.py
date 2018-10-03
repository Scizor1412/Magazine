from mongoengine import *

class Article(Document):
    title = StringField()
    sapo = StringField()
    thumbnail = StringField()
    content = StringField()
    time = DateTimeField()
    author = StringField()
    level = IntField()
    category = StringField()
    view_count = IntField(default=0)
# 0 là chưa duyệt, 1 là đã duyệt và có thể hiển thị