import psycopg2

class Database:
    def __init__(self, database, user, password):
        self._connection = psycopg2.connect(database=database, user=user, password=password)
        self._cursor = self._connection.cursor()
    
    def execute(self, query, vals = ()):
        self._cursor.execute(query, vals)

    def commit(self):
        self._connection.commit()
    
    def close(self):
        self._connection.close()

    """Adds user and returns if adding user is success"""
    def add_user(self, username, password):
        try:
            self._cursor.execute("INSERT INTO users VALUES (%s, %s)", (username, password))
        except:
            return False
        return True
    
    """Removes user and returns if removing user is success"""
    def remove_user(self, username):
        if not self.is_username_exists(username):
            return False
        vals = (username,)
        self._cursor.execute("DELETE FROM order_items WHERE userid=%s", vals)
        self._cursor.execute("DELETE FROM orders WHERE userid=%s", vals)
        self._cursor.execute("DELETE FROM cart_items WHERE username=%s", vals)
        self._cursor.execute("DELETE FROM users WHERE username=%s", vals)
        return True
    
    """Fetches payment info and shipping addreess of an user"""
    def fetch_account_details(self, username):
        self._check_user_in_database(username)
        self._cursor.execute("SELECT paymentinfo, shippingaddress FROM users WHERE username = %s", (username,))
        result = self._cursor.fetchone()
        return result[0], result[1]

    """Edits user's payment info and returns if editing payment info is success"""
    def edit_payment_info(self, username, payment_info):
        if not self.is_username_exists(username):
            return False
        self._cursor.execute("UPDATE users SET paymentinfo = %s WHERE username = %s", (payment_info, username))
        return True
    
    """Edits user's shipping address and returns if editing shipping address is success"""
    def edit_shipping_address(self, username, shipping_address):
        if not self.is_username_exists(username):
            return False
        self._cursor.execute("UPDATE users SET shippingaddress = %s WHERE username = %s", (shipping_address, username))
        return True
    
    """Adds item to the cart based on the username, item id, and quantity"""
    def add_cart_item(self, username, item_id, quantity):
        if quantity <= 0:
            raise Exception("Quantity for adding cart item must be non-negative non-zero number")

        self._check_user_in_database(username)
        self._cursor.execute("SELECT quantity FROM cart_items WHERE username = %s AND itemid = %s", (username, item_id))
        result = self._cursor.fetchone()

        if result is None:
            try:
                self._cursor.execute("INSERT INTO cart_items VALUES (%s, %s, %s)", (username, item_id, quantity))
            except:
                raise Exception("Item id %s does not exist in the database" % (item_id))
        else:
            final_quantity = str(int(quantity) + int(result[0]))
            self._cursor.execute("UPDATE cart_items SET quantity = %s WHERE username = %s AND itemid = %s", (final_quantity, username, item_id))
    
    """Removes item from the cart based on the username, item id, and quantity"""
    def remove_cart_item(self, username, item_id, quantity):
        if quantity <= 0:
            raise Exception("Quantity for adding cart item must be non-negative non-zero number")
        self._check_user_in_database(username)

        self._cursor.execute("SELECT quantity FROM cart_items WHERE username = %s AND itemid = %s", (username, item_id))
        result = self._cursor.fetchone()
        if result is None:
            raise Exception("No item with id %s exists in the cart" % (item_id))
        
        result_quantity = result[0]
        final_quantity = result_quantity - int(quantity)

        if final_quantity == 0:
            self._cursor.execute("DELETE FROM cart_items WHERE username = %s AND itemid = %s", (username, item_id))
        elif final_quantity > 0:
            self._cursor.execute("UPDATE cart_items SET quantity = %s WHERE username = %s AND itemid = %s", (final_quantity, username, item_id))
        else:
            raise Exception("Final quantity cannot be negative")
    
    """Fetch cart items based on username"""
    def fetch_cart_items(self, username):
        self._cursor.execute(
            "SELECT I._id, I.name, I.price, C.quantity "
            "FROM inventory AS I, cart_items AS C "
            "WHERE I._id = C.itemid AND C.username = %s ",
            (username,)
        )
        cart_item_list = []
        for row in self._cursor.fetchall():
            cart_item_dict = {"id": row[0], "name": row[1], "price": row[2], "quantity": row[3]}
            cart_item_list.append(cart_item_dict)
        return cart_item_list
    
    """Returns whether the username exists in the database"""
    def is_username_exists(self, username):
        self._cursor.execute("SELECT username FROM users WHERE username LIKE %s", (username,))
        results = self._cursor.fetchall()
        return len(results) > 0
    
    """Returns if the user login match"""
    def is_user_exists(self, username, password):
        query = "SELECT username, password FROM users WHERE username LIKE %s AND password LIKE %s"
        vals = (username, password)
        self._cursor.execute(query, vals)
        result = self._cursor.fetchone()

        if result is None:
            return False
        return result[0] == username and result[1] == password
    
    def _check_user_in_database(self, username):
        if not self.is_username_exists(username):
            raise Exception("Username %s does not exist in the database" % (username))

