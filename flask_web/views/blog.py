from flask_web import app
from flask import Blueprint, render_template

mod = Blueprint('blog', __name__)

@app.route('/')
def index():
    return render_template('index.html')