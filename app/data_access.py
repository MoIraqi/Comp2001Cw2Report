import pyodbc


def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=dist-6-505.uopnet.plymouth.ac.uk;'
        'DATABASE=COMP2001;'
        'UID=your_username;'
        'PWD=your_password'
    )
    return conn


def fetch_all_trails():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CW2.Trails")
    trails = cursor.fetchall()
    return [{"trail_id": trail[0], "name": trail[1], "description": trail[2]} for trail in trails]


def fetch_trail_by_id(trail_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CW2.Trails WHERE trail_id = ?", (trail_id,))
    trail = cursor.fetchone()
    if trail:
        return {"trail_id": trail[0], "name": trail[1], "description": trail[2]}
    return None


def insert_trail(name, description):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO CW2.Trails (name, description, created_by) VALUES (?, ?, ?)",
                   (name, description, "user"))
    conn.commit()
