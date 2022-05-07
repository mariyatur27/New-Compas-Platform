from flask import Blueprint, render_template

bp = Blueprint("index", __name__, url_prefix="/")

@bp.route("/", methods=("GET",))
def home():
    return render_template("index.html")

@bp.route("/login", methods=("GET",))
def login():
    return render_template("login.html")