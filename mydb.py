#  """
#   This function creates a new database using a MySQL connector.

#   Args:
#       database_name (str): The name of the database to create.
#       host (str, optional): The hostname or IP address of the MySQL server. Defaults to 'localhost'.
#       user (str, optional): The username to connect to the MySQL server. Defaults to 'root'.
#       password (str, optional): The password to connect to the MySQL server. Defaults to 'lujianheng554' (Please replace with a secure password).

#   Returns:
#       None: This function doesn't return any value, it creates the database as a side effect.

#   Raises:
#       Exception: If any error occurs during the database creation process.
#   """
import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'lujianheng554',

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
