from mongoengine import *

class Article(Document):
    title = StringField()
    sapo = StringField()
    thumbnail = StringField()
    content = StringField()
    time = StringField()
    author = StringField()