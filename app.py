import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "CooKIEmONSter123xy0&!#usL*txGha_bsnSb72shjkshME42"

@app.route("/")
def index():
    return "SHOPIFY BACKEND CHALLENGE"

@app.route("/view")
def get_list_of_inventories():
    all_items = get_db()
    print("View a list of Inventory Items")
    # returning a python list to view all the inventory items in our database
    return str(all_items)

# an helper function to be able to access the raw data of our database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('inventory_list.db')
        cursor = db.cursor()
        # groceries is the table name of our inventory_list database
        cursor.execute("select name from groceries")
        all_data = cursor.fetchall()
        # only get the string portion of the values in the database
        all_data = [str(val[0]) for val in all_data]
    return all_data

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()