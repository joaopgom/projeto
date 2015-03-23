__author__ = 'john'

from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, Table, text, func
from sqlalchemy.orm import relationship
from flask_web.database import Model



assoc_post_commment = Table('assoc_post_categories', Model.metadata,
                          Column('posts_id', Integer, ForeignKey('posts.id')),
                          Column('categories_id', Integer, ForeignKey('categories.id')))


class Post(Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    content = Column(String(5000), nullable=False)
    created_at = Column(DateTime, default=func.now())
    visit_count = Column(Integer, server_default='0')
    category = relationship('Category', secondary=assoc_post_commment)
    is_replied = Column(Boolean, server_default='0')
    author = Column(ForeignKey('users.id'), nullable=False)
    e_mail = Column(String(100), nullable=False)
    type = Column(ForeignKey('types.id'), nullable=False)

class Comment(Model):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String(1000), nullable=False)
    author = Column(ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=func.now())
    post = Column(ForeignKey('posts.id'), nullable=False)
    comment = Column(ForeignKey('comments.id'), nullable=False)

class Category(Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)

class Type(Model):
    __tablename__ = 'types'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)