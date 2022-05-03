from flask import Blueprint, render_template

bp = Blueprint("index", __name__, url_prefix="/")

@bp.route("/", methods=("GET",))
def home():
    return render_template("index.html")

@bp.route("/student_registration", methods=("GET",))
def student_reg():
    return render_template("student_reg.html")

@bp.route("/tutor_registration", methods=("GET",))
def tutor_reg():
    return render_template("tutor_reg.html")

@bp.route("/login", methods=("GET",))
def login():
    return render_template("login.html")

@bp.route("/student_dashboard", methods=['POST'])
def student_dashboard():
    return render_template("student_dashboard.html")
