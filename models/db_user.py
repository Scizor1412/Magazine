from mongoengine import *

class User(Document):
    fullname = StringField()
    yob = IntField()
    email = EmailField()
    password = StringField()
    level = IntField()