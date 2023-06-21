import sqlite3

# Create a conection
connection = sqlite3.connect("teste.db")

# Create a cursor
db = connection.cursor()


# Commit the commands to the database
connection.commit()

# Close the connection
connection.close()
