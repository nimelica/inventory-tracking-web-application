import sqlite3

class Inventory_Manager:
    def __init__(self):
        pass

<<<<<<< HEAD
    # add a new created item
    def create_item(self, new_item):
        cat, name, price, loc = new_item[0], new_item[1], new_item[2], new_item[3]
        command = 'INSERT INTO Item (category,name,price,location) VALUES (?, ?, ?, ?);'
        data_tube = (cat, name, price, loc)
        db = sqlite3.connect('databases/products.db')
        cursor = db.cursor()
        try:
            cursor.execute(command, data_tube)
            db.commit()
            print ("added successfully")
=======
    # helper function to get products database cursor
    def get_db_cursor(self):
        db = sqlite3.connect('databases/products.db')
        cursor = db.cursor()
        return cursor

    # add a new created item
    def create_item(self, new_item):
        row = ((new_item[0]), (new_item[1]), (new_item[2]), (new_item[3]))
        command = 'INSERT INTO Item (category,name,price,location) VALUES (%s , %s, %s, %s)'
        cursor = self.get_db_cursor()
        try:
            cursor.execute(command, row)
>>>>>>> 536bb7a7b055a7c556e67a82b102263fc4b78386
        except Exception as e:
            print ("error in operation")
            db.rollback()
            return e
        db.close()
        return cursor.lastrowid

    # update/edit an item
    def edit_item(self, name, info):
<<<<<<< HEAD
        command = "UPDATE Item SET category = ? ,name = ?, price = ?, location = ? WHERE name = {}".format(name)
        cat, name_, price, loc = info[0], info[1], info[2], info[3]
        data_tube = (cat, name_, price, loc)
        db = sqlite3.connect('databases/products.db')
        cursor = db.cursor()
=======
        command = "UPDATE Item SET category = %s ,name = %s, price = %s, location = %s WHERE name = {}".format(name)
        row = (info[0], info[1], info[2], info[3])
        cursor = self.get_db_cursor()
>>>>>>> 536bb7a7b055a7c556e67a82b102263fc4b78386
        try:
            cursor.execute(command, data_tube)
            db.commit()
        except Exception as e:
            db.rollback()
            return e
        db.close()

    # when deleting an item, allow deletion comments
    def deletion_message(self):
        com_db = sqlite3.connect('comments.db')
        com_cursor = com_db.cursor()
        user_name = input('Please enter your name: ' )
        message = input('You can enter your comment: ')
        command = "INSERT INTO Comment (user_name, message) VALUES (?, ?);"
        input_db = (user_name, message)
        try:
            com_cursor.execute(command, input_db)
            com_db.commit()
        except Exception as e:
            com_db.rollback()
            return e
        com_db.close()

    # when deleting an item, allow undeletion of a comment 
    def delete_comment(self):
        user_name = input('Please enter your name: ' )
        command = "DELETE FROM Comment WHERE user_name = {}".format(user_name)
        com_db = sqlite3.connect('comments.db')
        com_cursor = com_db.cursor()
        try:
            com_cursor.execute(command)
<<<<<<< HEAD
            com_db.commit()
            print('Your comment is deleted!')
        except Exception as e:
            com_db.rollback()
            return e
        com_db.close()
=======
            print('Your comment is deleted!')
        except Exception as e:
            return e
>>>>>>> 536bb7a7b055a7c556e67a82b102263fc4b78386

    # delete an item
    def delete_item(self, name):
        command = "DELETE FROM Item WHERE name = ?"
        db = sqlite3.connect('databases/products.db')
        cursor = db.cursor()
        try:
            cursor.execute(command, (name,))
            db.commit()
            print("record deleted successfully")
            prompt = input('Do you want to leave a message Y/N: ')
            if prompt == 'N':
                return ("Item deleted successfully!")
            elif prompt == 'Y':
                self.deletion_message()
        except Exception as e:
            print("error in operation")
            db.rollback()
            return e
<<<<<<< HEAD
        db.close()


=======
        prompt = input('Do you want to leave a message Y/N: ')
        if prompt == 'N':
            return ("Item deleted successfully!")
        elif prompt == 'Y':
            self.deletion_message()

>>>>>>> 536bb7a7b055a7c556e67a82b102263fc4b78386
    # view the list of item names
    def view_item_names(self):
        # returning a python list to view all the inventory items in our database
        db = sqlite3.connect('databases/products.db')
        cursor = db.cursor()
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

    # view the list of the items in details
    def view_all_items(self):
        db = sqlite3.connect('databases/products.db')
        cursor = db.cursor()
        try:
            cursor.execute("SELECT * FROM Item")
            result = cursor.fetchall()
        except Exception as e:
            return e
        return result


def main():
   im = Inventory_Manager()
<<<<<<< HEAD
   # print(im.create_item(('Candy','Nerds',7.0, 'Phoneix, AZ')))
   im.view_item_names()
   # print(im.view_all_items())
   # im.delete_item('Nerds')
   # im.view_item_names()
   im.deletion_message()
=======
   print(im.create_item(('Candy','Nerds',7.0, 'Phoneix, AZ')))
   im.view_item_names()
   # print(im.view_all_items())
   # print(im.edit_item('Oreo', ('Snack', 'Oreo Biscuits', 7.0, 'Newark, NY')))
   # print(im.view_all_items())
   # im.delete_item('Candy')
>>>>>>> 536bb7a7b055a7c556e67a82b102263fc4b78386
   


if __name__ == "__main__":
    main()