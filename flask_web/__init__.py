import os
import jinja2

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

#app.jinja_loader = jinja2.FileSystemLoader(os.path.abspath(os.path.dirname(__file__)) + '/templates')

from flask_web.views import blog

app.register_blueprint(blog.mod)