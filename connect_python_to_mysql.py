import mysql.connector
conn = mysql.connector.connect(
    host = "localhost", user = "root", 
    passwd = " ", database = "world"
)
my_cursor = conn.cursor()

conn.commit()
conn.close()

print("Connection succesfully created")