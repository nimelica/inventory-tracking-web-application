import sqlite3

# Create an empty database 
connection = sqlite3.connect('comments.db')
# communication with database via cursor with SQL commands
cursor = connection.cursor()

# be sure table is not already exists
cursor.execute('DROP TABLE IF EXISTS Comment')

# create a table named "Items" in "products.db" database
cursor.execute('CREATE TABLE Comment (user_name TEXT, message TEXT)')

# Do not forget to save (commit) and close the database connection
connection.commit()
connection.close()