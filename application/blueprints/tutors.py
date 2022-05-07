from flask import Blueprint, render_template

bp = Blueprint("tutors", __name__, url_prefix="/tutors/")

@bp.route("/register", methods=("GET", "POST"))
def tutor_reg():
    return render_template("tutors/register.html")

@bp.route("/dashboard", methods=("GET",))
def tutor_dashboard():
    return render_template("tutors/dashboard.html")