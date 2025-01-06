from app.db_connection import db


class Trail(db.Model):
    __tablename__ = 'Trail'

    TrailID = db.Column(db.Integer, primary_key = True)
    TrailName = db.Column(db.String(255), nullable = False)
    TrailSummary = db.Column(db.String(255))
    TrailDescription = db.Column(db.Text)
    Difficulty = db.Column(db.String(50))
    Location = db.Column(db.String(255))
    Length = db.Column(db.Float)
    ElevationGain = db.Column(db.Integer)
    RouteType = db.Column(db.String(50))
    OwnerID = db.Column(db.Integer)
