from flask import Flask, current_app, g
from flask_sqlalchemy import SQLAlchemy


def get_db():
    if 'db' not in g:
        g.db = SQLAlchemy(current_app)
    return g.db


def close_db(e=None):
    db: SQLAlchemy = g.pop('db', None)
    if db is not None:
        db.session.dispose()
        db.get_engine(current_app).dispose()


def init_db(app: Flask):
    app.teardown_appcontext(close_db)
