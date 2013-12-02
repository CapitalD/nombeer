import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'development_key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'nombeer.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
