# app/db_connection.py

import pyodbc

from flask_jwt_extended import create_access_token
from flask import jsonify, request


def generate_token(user_id):
    token = create_access_token(identity = user_id)
    return token


def get_db_connection():
    connection_string = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DIST-6-505.uopnet.plymouth.ac.uk;"
        "Database=COMP2001_MIraqi;"
        "UID=MIraqi;"
        "PWD=GpkK182+;"
    )
    return pyodbc.connect(connection_string)
