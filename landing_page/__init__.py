"""
This is the main file of the application.
It contains the application factory function.
"""

from flask import Flask
from landing_page.views.routes import main_bp, register  # Import the blueprint


def create_flask_app():
    app = Flask(__name__)
    app.config.from_object('landing_page.config')  # Load the configuration settings from the config.py file
    # main_bp.config['MAINTENANCE_MODE'] = False  # Set the maintenance mode to False
    app.add_url_rule('/register', view_func=register, methods=['POST'])
    app.register_blueprint(main_bp)  # Register the blueprint

    return app


if __name__ == '__main__':
    app = create_flask_app()
    app.run(debug=True)
