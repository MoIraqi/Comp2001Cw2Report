import pyodbc

# Database connection details
server = 'DIST-6-505.uopnet.plymouth.ac.uk'
database = 'COMP2001_MIraqi'
username = 'MIraqi'
password = 'GpkK182+'

connection = None  # Initialize the connection variable

try:
    # Establishing connection
    connection = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )
    print("Connection successful!")

    # Create a cursor object
    cursor = connection.cursor()

    # SQL query to perform a JOIN between tables in the CW2 schema
    query = """
    SELECT 
        Trail.TrailID, 
        Trail.TrailName, 
        LocationPoint.Description AS LocationDescription,
        Feature.FeatureName
    FROM 
        CW2.Trail
    INNER JOIN 
        CW2.LocationPoint ON Trail.TrailID = LocationPoint.TrailID
    INNER JOIN 
        CW2.Feature ON Feature.FeatureID = LocationPoint.TrailID
    """

    # Execute the query
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the data
    print("Joined Table Data:\n")
    for row in rows:
        print(f"TrailID: {row.TrailID}, TrailName: {row.TrailName}, "
              f"LocationDescription: {row.LocationDescription}, FeatureName: {row.FeatureName}")

except pyodbc.Error as e:
    print(f"Error connecting to the database: {e}")

finally:
    # Close the connection if it was created
    if connection:
        connection.close()
        print("Connection closed.")
