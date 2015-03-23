from flask_web import app
from sqlalchemy import create_engine, event, Column, Integer, String, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(app.config['DATABASE_URI'],
                                convert_unicode=True,
                                **app.config['DATABASE_OPTIONS'])

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,))



Model = declarative_base()
Model.query = db_session.query_property()

def init_db():
    from flask_web.auth.models import User
    from flask_web.blog.models import Post, Comment, Type, Category, assoc_post_commment
    Model.metadata.create_all(engine)
#event.listen(db_session, 'after_flush',)





