from flask import Blueprint, jsonify
from app.services.menu_service import get_menu

menu_bp = Blueprint("menu", __name__)

@menu_bp.route("/menu", methods=["GET"])
def menu():
    return jsonify(get_menu())
