from flask import Blueprint, render_template

bp = Blueprint("students", __name__, url_prefix="/students/", template_folder="../templates/students")

@bp.route("/register", methods=("GET", "POST"))
def student_reg():
    return render_template("register.html")

@bp.route("/dashboard", methods=("GET",))
def student_dashboard():
    return render_template("dashboard.html")
