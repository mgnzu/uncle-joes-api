from flask import Blueprint, jsonify
from app.services.member_service import get_orders, get_points

member_bp = Blueprint("member", __name__)

@member_bp.route("/members/<member_id>/orders", methods=["GET"])
def orders(member_id):
    return jsonify(get_orders(member_id))

@member_bp.route("/members/<member_id>/points", methods=["GET"])
def points(member_id):
    return jsonify({"points": get_points(member_id)})
