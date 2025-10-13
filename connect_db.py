import mysql.connector

conn = mysql.connector.connect(
    host="104.198.31.98",
    user="admin",
    password="StrongPassw0rd!",
    database="user_profile_db"
)

if conn.is_connected():
    print("Connected to Cloud SQL!")
    cur = conn.cursor()
    cur.execute("SHOW DATABASES;")
    for db in cur.fetchall():
        print(db)
    cur.close()
    conn.close()
else:
    print("Connection failed.")

