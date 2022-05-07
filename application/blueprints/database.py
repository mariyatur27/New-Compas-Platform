from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


bp = Blueprint("index", __name__, url_prefix="/")

bp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(bp)