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

@bp.route("/payment_history", method=("GET"))
def payment_history():
    return render_template("students/payment_history.html")

@bp.route("/free_assessment_registration", method=("GET"))
def assessment_reg():
    return render_template("students/assessment_reg.html")

@bp.route("/tutoring_session_registration", method=("GET"))
def session_reg():
    return render_template("students/session_registration.html")

@bp.route("/session_time_table", method=("GET"))
def time_table():
    return render_template("students/time_table.html")

@bp.route("/registration_history", method=("GET"))
def reg_history():
    return render_template("students/registration_history.html")