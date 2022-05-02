from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from application.blueprints import index
        app.register_blueprint(index.bp)
    
    return app