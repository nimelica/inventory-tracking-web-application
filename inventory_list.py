import sqlite3, json

# read json data into a list
with open('products.json') as f:
    data = json.load(f)

# Create an empty database 
connection = sqlite3.connect('products.db')

# communication with database via cursor with SQL commands
cursor = connection.cursor()

# be sure table is not already exists
cursor.execute('DROP TABLE IF EXISTS Item')

# create a table named "Items" in "products.db" database
cursor.execute('CREATE TABLE Item (category TEXT, name TEXT, price REAL, location TEXT)')

# get the list of the dictionaries
all_items = data['products']

# fill the Item table by looping through the product dictionaries
for i in range(len(all_items)):
    product = all_items[i]
    cursor.execute("INSERT INTO Item VALUES (?, ?, ?, ?)", (product['category'], product['name'], product['price'], product['location']))
    print('added', product)

# Do not forget to save (commit) and close the database connection
connection.commit()
connection.close()

