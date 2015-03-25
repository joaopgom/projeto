import os

_basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = 'mysql://root:root@localhost:3306/projeto'
DATABASE_OPTIONS = {}
DEBUG = False

#template_folder =  _basedir + '/templates'