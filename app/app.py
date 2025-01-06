from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

# Initialize Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# Configure Database
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://MIraqi:GpkK182+@DIST-6-505.uopnet.plymouth.ac.uk/COMP2001_MIraqi?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Initialize Extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
swagger = Swagger(app)


# Trail Model
class Trail(db.Model):
    __tablename__ = 'Trail'

    TrailID = db.Column(db.Integer, primary_key = True)
    TrailName = db.Column(db.String(255))
    TrailSummary = db.Column(db.String(255))
    TrailDescription = db.Column(db.Text)
    Difficulty = db.Column(db.String(50))
    Location = db.Column(db.String(255))
    Length = db.Column(db.Float)
    ElevationGain = db.Column(db.Integer)
    RouteType = db.Column(db.String(50))
    OwnerID = db.Column(db.Integer)


# Endpoints
@app.route('/api/trails', methods = ['GET'])
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


@app.route('/api/trails', methods = ['POST'])
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


@app.route('/api/trails/<int:trail_id>', methods = ['GET'])
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


@app.route('/api/trails/<int:trail_id>', methods = ['PUT'])
@jwt_required()
def update_trail(trail_id):
    try:
        data = request.json
        trail = Trail.query.get(trail_id)
        if not trail:
            return jsonify({"error": "Trail not found"}), 404

        # Update fields
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


@app.route('/api/trails/<int:trail_id>', methods = ['DELETE'])
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


# Run the app
if __name__ == '__main__':
    app.run(debug = True)
