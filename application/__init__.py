from flask import Flask
import configs
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_object(configs)
    csrf.init_app(app)
    app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

    with app.app_context():
        from application.blueprints import index, students, tutors
        from application.models.database import init_db

        app.register_blueprint(index.bp)
        app.register_blueprint(students.bp)
        app.register_blueprint(tutors.bp)
        init_db(app)

    return app
