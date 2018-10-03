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
<<<<<<< HEAD
    view_count = IntField(default = 0)
=======
    view_count = IntField(default=0)
>>>>>>> 48bfe39d0290fdcf1ee4c0ebec1165c9ed6694a2
# 0 là chưa duyệt, 1 là đã duyệt và có thể hiển thị