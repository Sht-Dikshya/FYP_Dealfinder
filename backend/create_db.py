import MySQLdb

try:
    db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", port=3306)
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS dealfinder_db;")
    print("Database dealfinder_db created or already exists.")
    db.close()
except Exception as e:
    print(f"Error creating database: {e}")
