from flask import Flask
from flask_cors import CORS
from app.routes.auth_routes import auth_bp
from app.routes.member_routes import member_bp
from app.routes.menu_routes import menu_bp
from app.routes.location_routes import location_bp
import os

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.secret_key = os.environ.get("SECRET_KEY", "supersecret")

    @app.route("/")
    def home():
        return {"status": "Coffee Club API running"}

    app.register_blueprint(auth_bp)
    app.register_blueprint(member_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(location_bp)

    return app
