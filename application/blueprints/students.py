from flask import Blueprint, render_template

bp = Blueprint("students", __name__, url_prefix="/students/")


@bp.route("/register", methods=("GET", "POST"))
def student_reg():
    # imports
    from ..forms.student_register import StudentRegister

    form = StudentRegister()

    if form.validate_on_submit():
        return redirect(url_for('index'))

    return render_template("students/register.html", form=form)


@bp.route("/dashboard", methods=("GET",))
def student_dashboard():
    return render_template("students/dashboard.html")
