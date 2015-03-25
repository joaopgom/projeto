__author__ = 'john'

from datetime import datetime
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.types import Integer, DateTime, Boolean, String
from sqlalchemy.orm import relationship, sessionmaker, backref
from flask_web.database import Base, Model



assoc_post_commment = Table('assoc_post_categories', Model.metadata,
                          Column('posts_id', Integer, ForeignKey('posts.id')),
                          Column('categories_id', Integer, ForeignKey('categories.id')))


class Category(Model, Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    post = relationship('Post', secondary=assoc_post_commment, backref=backref('categories', uselist=True))

    def __init__(self, name):
        self.name = name

class Post(Model, Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    content = Column(String(5000), nullable=False)
    created_at = Column(DateTime, nullable=False)
    visit_count = Column(Integer, server_default='0')
    category = relationship('Category', secondary=assoc_post_commment, backref=backref('categories', uselist=True))
    is_replied = Column(Boolean, server_default='0')
    author = Column(ForeignKey('users.id'), nullable=False)
    type = Column(ForeignKey('types.id'), nullable=False)

    def __init__(self, title, content, visit_count, category, is_replied, author, type):
        self.title = title
        self.created_at = datetime.now()
        self.content = content
        self.visit_count = visit_count
        self.category = category
        self.is_replied = is_replied
        self.author = author
        self.type = type

class Comment(Model, Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String(1000), nullable=False)
    author = Column(ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    post = Column(ForeignKey('posts.id'), nullable=False)
    comment = Column(ForeignKey('comments.id'), nullable=False)

    def __init__(self, content, author, post, comment):
        self.content = content
        self.author = author
        self.post = post
        self.comment = comment
        self.created_at = datetime.now()


class Type(Model, Base):
    __tablename__ = 'types'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)

    def __init__(self, name):
        self.name = name