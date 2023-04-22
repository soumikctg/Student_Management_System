import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE studentdb")

print("done") 