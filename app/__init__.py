from flask import Flask
from flask_cors import CORS
from app.routes.auth_routes import auth_bp
from app.routes.member_routes import member_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def home():
        return {"status": "Coffee Club API running"}

    app.register_blueprint(auth_bp)
    app.register_blueprint(member_bp)
    app.secret_key = "supersecret"

    return app
