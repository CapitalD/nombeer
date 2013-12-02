from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models



#@app.teardown_appcontext


@app.template_filter()
def datetimeformat(epoch):
    return datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d')



if __name__ == '__main__':
    app.run()
