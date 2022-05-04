from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from application.blueprints import index, students
        app.register_blueprint(index.bp)
        app.register_blueprint(students.bp)
    
    return app