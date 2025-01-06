# Trail Microservice

This is a RESTful microservice for managing trails.

## Features
- CRUD operations on trails.
- Authentication with JWT tokens.
- Python-based implementation.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Apply SQL schema from `sql/schema.sql`.
3. Insert sample data with `sql/sample_data.sql`.
4. Run the app: `python app/trail_microservice.py`.
5. Test endpoints with Postman or Swagger.

## Security
- Uses JWT for role-based access control.
- Follows OWASP best practices for secure RESTful APIs.
