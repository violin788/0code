exec(open('util.py').read())
def mysql(inp):
	
	from getpass import getpass
	from mysql.connector import connect, Error

	try:
	    with connect(
	        host="localhost",
	        user=input("Enter username: "),
	        password=getpass("Enter password: "),
	        database="online_movie_rating",
	    ) as connection:
	        print(connection)
	except Error as e:
	    print(e)

inp = []
mysql(inp)