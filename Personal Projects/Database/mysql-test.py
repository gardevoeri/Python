import mysql.connector

connection = mysql.connector.connect(
    host="localhost", password="Je@112358", user="root", database="learning"
)

db = connection.cursor()

# if connection.is_connected():
#    print("Connection estabilished...")

db.execute("SELECT * FROM student")

for i in db:
    print(i)
