from flask import Blueprint, jsonify
from app.services.location_service import get_locations

location_bp = Blueprint("locations", __name__)

@location_bp.route("/locations", methods=["GET"])
def locations():
    return jsonify(get_locations())
