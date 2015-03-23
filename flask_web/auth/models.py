from flask_web.database import Model
from sqlalchemy import Column, String, Integer, Boolean

class User(Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False,)
    email = Column(String(200), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(8), nullable=False)
    is_admin = Column(Boolean, nullable=False, server_default='0')

#class Group(database.Model):
#    permissions = None


