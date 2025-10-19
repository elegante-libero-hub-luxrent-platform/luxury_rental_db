import mysql.connector

try:
    conn = mysql.connector.connect(
        host="136.115.72.72",
        user="admin",
        password="Your$trongP@ssw0rd",
        database="user_profile_db",
        port=3306,
        connection_timeout=10
    )
    if conn.is_connected():
        print("Connected to MySQL on GCP VM!")
        cur = conn.cursor()
        cur.execute("SHOW DATABASES;")
        for (db_name,) in cur.fetchall():
            print(db_name)
finally:
    try:
        cur.close()
        conn.close()
    except Exception:
        pass