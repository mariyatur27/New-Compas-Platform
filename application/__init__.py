from flask import Flask
import configs

def create_app():
    app = Flask(__name__)
    app.config.from_object(configs)

    with app.app_context():
        from application.blueprints import index, students
        from application.models.database import init_db

        app.register_blueprint(index.bp)
        app.register_blueprint(students.bp)
        init_db(app)

    return app
