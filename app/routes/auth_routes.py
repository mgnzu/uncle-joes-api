from flask import Blueprint, request, jsonify, session
from app.services.auth_service import login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = login_user(data["email"], data["password"])

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    session["user"] = user
    return jsonify(user)
