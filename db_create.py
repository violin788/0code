exec(open('util.py').read())
def db_create(inp):
	
	import sqlite3

	# Establish a connection to the database file
	conn = sqlite3.connect('example.db')

	# Create a cursor object to execute SQL commands
	cursor = conn.cursor()

	# Create a table
	cursor.execute('''CREATE TABLE IF NOT EXISTS users (
	                id INTEGER PRIMARY KEY,
	                name TEXT,
	                age INTEGER)''')

	# Insert some data into the table
	users_data = [
	    ('Alice', 30),
	    ('Bob', 25),
	    ('Charlie', 35)
	]

	cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', users_data)

	# Commit changes
	conn.commit()

	# Close the cursor and connection
	cursor.close()
	conn.close()


inp = []
db_create(inp)