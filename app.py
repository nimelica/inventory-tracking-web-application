import sqlite3
from flask import Flask, jsonify, request, g
from inventory_list import all_items 

app = Flask(__name__)
app.secret_key = "CooKIEmONSter123xy0&!#usL*txGha_bsnSb72shjkshME42"

@app.route("/")
def index():
    return "SHOPIFY BACKEND CHALLENGE"


print(all_items)


@app.route("/products")
def get_list_of_inventories():
    # returning a python list to view all the inventory items in our database
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('products.db')
        cursor = db.cursor()
        # groceries is the table name of our inventory_list database
        cursor.execute("SELECT name FROM Item")
        all_data = cursor.fetchall()
        # only get the string portion of the values in the database
        all_data = [str(val[0]) for val in all_data]
    return (str(all_data))


@app.route("/products", methods=["POST"])
def add_item():
    new_product = {
        'category': request.json['category'],
        'name': request.json['name'],
        'price': request.json['price'],
        'location': request.json['location']
    }
    all_items.append(new_product)
    message = 'added ' + str(new_product)
    return message

# Update Data Route
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in all_items if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['category'] = request.json['category']
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['location'] = request.json['location']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product Not found'})

# DELETE Data Route
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in all_items if product['name'] == product_name]
    if len(productsFound) > 0:
        all_items.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': all_items
        })


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True, port=4000)