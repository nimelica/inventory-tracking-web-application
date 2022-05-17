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

all_items = data['products']

# fill the Item table
for i in range(len(all_items)):
    product = all_items[i]
    print(product)
    cursor.execute("INSERT INTO Item VALUES (?, ?, ?, ?)", (product['category'], product['name'], product['price'], product['location']))

# Do not forget to save (commit) and close the database connection
connection.commit()
connection.close()

