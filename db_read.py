exec(open('util.py').read())
def db_read(inp):
	
	import sqlite3

	# Establish a connection to the database file
	conn = sqlite3.connect('example.db')

	# Create a cursor object to execute SQL commands
	cursor = conn.cursor()

	# Execute a SQL query to select data from a table
	cursor.execute("SELECT * FROM users")

	# Fetch all the rows from the result set
	rows = cursor.fetchall()

	# Iterate over the rows and print each row
	for row in rows:
	    print(row)

	# Close the cursor and connection
	cursor.close()
	conn.close()
	
	
inp = []
db_read(inp)