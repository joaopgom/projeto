from flask_web.database import Model, Base
from sqlalchemy import Column, String, Integer, Boolean


class User(Model, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False,)
    email = Column(String(200), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(8), nullable=False)
    is_admin = Column(Boolean, nullable=False, server_default='0')

    def __init__(self, name, email, username, password, is_admin=0):
        self.name = name
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.email = email

#class Group(database.Model):
#    permissions = None


