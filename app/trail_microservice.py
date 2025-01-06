from flask import Blueprint, request, jsonify
from app.db_connection import db
from app.models import Trail
from flask_jwt_extended import jwt_required

trail_bp = Blueprint('trail_bp', __name__)


@trail_bp.route('', methods = ['GET'])
@jwt_required()
def get_trails():
    try:
        trails = Trail.query.all()
        trail_list = [
            {
                "TrailID": trail.TrailID,
                "TrailName": trail.TrailName,
                "TrailSummary": trail.TrailSummary,
                "TrailDescription": trail.TrailDescription,
                "Difficulty": trail.Difficulty,
                "Location": trail.Location,
                "Length": trail.Length,
                "ElevationGain": trail.ElevationGain,
                "RouteType": trail.RouteType,
                "OwnerID": trail.OwnerID,
            }
            for trail in trails
        ]
        return jsonify(trail_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@trail_bp.route('', methods = ['POST'])
@jwt_required()
def create_trail():
    try:
        data = request.json
        new_trail = Trail(
            TrailName = data.get('TrailName'),
            TrailSummary = data.get('TrailSummary'),
            TrailDescription = data.get('TrailDescription'),
            Difficulty = data.get('Difficulty'),
            Location = data.get('Location'),
            Length = data.get('Length'),
            ElevationGain = data.get('ElevationGain'),
            RouteType = data.get('RouteType'),
            OwnerID = data.get('OwnerID'),
        )
        db.session.add(new_trail)
        db.session.commit()
        return jsonify({"message": "Trail created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@trail_bp.route('/<int:trail_id>', methods = ['GET'])
@jwt_required()
def get_trail(trail_id):
    try:
        trail = Trail.query.get(trail_id)
        if not trail:
            return jsonify({"error": "Trail not found"}), 404
        trail_data = {
            "TrailID": trail.TrailID,
            "TrailName": trail.TrailName,
            "TrailSummary": trail.TrailSummary,
            "TrailDescription": trail.TrailDescription,
            "Difficulty": trail.Difficulty,
            "Location": trail.Location,
            "Length": trail.Length,
            "ElevationGain": trail.ElevationGain,
            "RouteType": trail.RouteType,
            "OwnerID": trail.OwnerID,
        }
        return jsonify(trail_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@trail_bp.route('/<int:trail_id>', methods = ['PUT'])
@jwt_required()
def update_trail(trail_id):
    try:
        data = request.json
        trail = Trail.query.get(trail_id)
        if not trail:
            return jsonify({"error": "Trail not found"}), 404

        trail.TrailName = data.get('TrailName', trail.TrailName)
        trail.TrailSummary = data.get('TrailSummary', trail.TrailSummary)
        trail.TrailDescription = data.get('TrailDescription', trail.TrailDescription)
        trail.Difficulty = data.get('Difficulty', trail.Difficulty)
        trail.Location = data.get('Location', trail.Location)
        trail.Length = data.get('Length', trail.Length)
        trail.ElevationGain = data.get('ElevationGain', trail.ElevationGain)
        trail.RouteType = data.get('RouteType', trail.RouteType)
        trail.OwnerID = data.get('OwnerID', trail.OwnerID)

        db.session.commit()
        return jsonify({"message": "Trail updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@trail_bp.route('/<int:trail_id>', methods = ['DELETE'])
@jwt_required()
def delete_trail(trail_id):
    try:
        trail = Trail.query.get(trail_id)
        if not trail:
            return jsonify({"error": "Trail not found"}), 404

        db.session.delete(trail)
        db.session.commit()
        return jsonify({"message": "Trail deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
