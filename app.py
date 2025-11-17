from dotenv import load_dotenv
load_dotenv() # <--- Це має бути на самому верху

from flask import Flask
import logging

from controllers import api_blueprint
from utils.response_utils import error_response

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    logging.basicConfig(level=logging.INFO)

    @app.errorhandler(404)
    def not_found(error):
        return error_response(message="Resource not found", status_code=404)

    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.error(f"An unexpected error occurred: {e}", exc_info=True)
        return error_response(
            message="An internal server error occurred", 
            details=str(e), 
            status_code=500
        )

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)