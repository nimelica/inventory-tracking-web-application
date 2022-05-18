# Shopify-inventory-tracking-CRUD-Application
A CRUD Application for inventory tracking 

## Operations
* Create
* Read
* Update
* Delete

## Additional Operations
* When deleting, allow adding deletion comments and undeletion them

## Project Structure
* We used two SQLite databases in this project: **products.db** & **comments.db**
* The _products.db_ collected data from the **products.json** file, while _comments.db_ is used to process user comments when deleting an item.
* These databases and their relational tables are created in the **db_managers** directory.
* We have an **Inventory_Manager** class in _app.py_ and with this class we can perform **CRUD** operations by calling its object in the main function

## CRUD Operations
### In **Inventory_Manager** class
* _def create_item_: adding a new item to _Item table_ in products.db
* _def edit_item_: updating an existing item in _Item table_ in products.db
* _def delete_item_: deleting an existing item in _Item table_ in products.db
* _def view_item_names_: view all the item names in the products.db

**Also some extra method:**
* _def add_comment_: allow user to add comments - comments are saved in _comments.db_
* _def uncomment_: allow user to uncomment an existing comment
* _def view_all_items_: view all items in detailed version

## Project Usage
* You can call any CRUD operation function in the main function of the app.py file.

## Optional Usage
### Using Flask to be able to see the final result through a Web-Page using routes
#### Example Code:

```
# Create instance of Flask by calling its class constructor
app = Flask(__name__)
app.secret_key = "WRITE A CUSTOM SECRET KEY HERE"

@app.route("/")
def get_list_of_inventories():
    all_items = get_db()
    print("View a list of Inventory Items")
    # returning a python list to view all the inventory items in our database
    return str(all_items)

# an helper function to be able to access the raw data of our database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('products.db')
        cursor = db.cursor()
        cursor.execute("SELECT name FROM Item")
        all_data = cursor.fetchall()
        # only get the string portion of the values in the database
        all_data = [str(val[0]) for val in all_data]
    return (str(all_data))
    
# this function is terminating our database connection
# once we are done with using it
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
# run app
if __name__ == '__main__':
	app.run(debug=True)

```

