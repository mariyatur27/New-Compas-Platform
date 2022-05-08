from flask import Blueprint, render_template, redirect, url_for
from application.models.student_registration_form import StudentRegistrationForm


bp = Blueprint("students", __name__, url_prefix="/students/")


@bp.route("/register", methods=("GET", "POST"))
def student_reg():
    form = StudentRegistrationForm()

    if form.validate_on_submit():
        return redirect(url_for('index'))

    return render_template("students/register.html", form=form)


@bp.route("/dashboard", methods=("GET",))
def student_dashboard():
    return render_template("students/dashboard.html")
