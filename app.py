import sqlite3

class Inventory_Manager:
    def __init__(self):
        pass

    def get_db_cursor(self):
        db = sqlite3.connect('products.db')
        cursor = db.cursor()
        return cursor

    def create_item(self, new_item):
        command = "INSERT INTO Item (category,name,price,location) VALUES (%s , %s, %s, %s)"
        cursor = self.get_db_cursor()
        try:
            cursor.execute(command, new_item)
        except Exception as e:
            return e
        return cursor.lastrowid

    def edit_item(self, name, info):
        command = "UPDATE Item SET category = %s ,name = %s, price = %s, location = %s WHERE name = {}".format(name)
        row = (info[0], info[1], info[2])
        cursor = self.get_db_cursor()
        try:
            cursor.execute(command, row)
        except Exception as e:
            return e

    def deletion_message(self):
        com_db = sqlite3.connect('comments.db')
        com_cursor = com_db.cursor()
        user_name = input('Please enter your name: ' )
        message = input('You can enter your comment: ')
        command = "INSERT INTO Comment (user_name, message) VALUES (%s , %s)"
        input_db = (user_name, message)
        com_cursor.execute(command, input_db)


    def delete_item(self, name):
        command = "DELETE FROM Item WHERE name = {}".format(name)
        cursor = self.get_db_cursor()
        try:
            cursor.execute(command)
        except Exception as e:
            return e
        prompt = input('Do you want to leave a message Y/N: ')
        if prompt is 'N':
            return ("Item deleted successfully!")
        elif prompt is 'Y':
            self.deletion_message()


    def view_item_names(self):
        # returning a python list to view all the inventory items in our database
        cursor = self.get_db_cursor()
        try:
            cursor.execute("SELECT name FROM Item")
            all_data = cursor.fetchall()
        except Exception as e:
            return e
        # only get the string portion of the values in the database
        all_data = [str(val[0]) for val in all_data]
        print('View the inventory item names')
        for data in all_data:
            print(data)

    def view_all_items(self):
        cursor = self.get_db_cursor()
        try:
            cursor.execute("SELECT * FROM Item")
            result = cursor.fetchall()
        except Exception as e:
            return e
        return result

def main():
   im = Inventory_Manager()
   im.get_list_of_inventories()

if __name__ == "__main__":
    main()