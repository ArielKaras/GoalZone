from flask import Flask
from landing_page.views.routes import main_bp, register


def create_flask_app():
    app = Flask(__name__)  # Create a Flask app
    app.config.from_object('landing_page.config')  # Load the configuration from the config.py file
    app.add_url_rule('/register', view_func=register, methods=['POST'])  # Add a URL rule for the register function
    app.register_blueprint(main_bp)  # Register the main_bp Blueprint
    return app


app = create_flask_app()
