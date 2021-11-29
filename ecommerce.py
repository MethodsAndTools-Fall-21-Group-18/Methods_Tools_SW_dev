from database import Database
from json_loader import decode_json

DB_SETTINGS = decode_json("settings/db_settings.json")
DB = Database(DB_SETTINGS["database"], DB_SETTINGS["user"], DB_SETTINGS["password"])

class User:
    
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._payment_info = ""
        self._shipping_address = ""
        self._cart = ShoppingCart()
        self._orders = OrderHistory(username)

    def verify_login(self):
        if not DB.is_user_exists(self.username, self.password):
            return False
        self._payment_info, self._shipping_address = DB.fetch_account_details(self.username)
        
        if self._payment_info is None:
            self._payment_info = ""
        if self._shipping_address is None:
            self._shipping_address = ""

        return True

    def edit_payment_info(self, payment_info):
        self._payment_info = payment_info
        DB.edit_payment_info(self.username, payment_info)
        DB.commit()

    def edit_shipping_address(self, shipping_address):
        self._shipping_address = shipping_address
        DB.edit_shipping_address(self.username, shipping_address)
        DB.commit()

    def view_account_details(self):
        print("Account Details")
        print("------------------")
        print("Username: " + self.username)
        print("Payment Info: " + self._payment_info)
        print("Shipping Address: " + self._shipping_address)
    
    def create_account(self):
        result = DB.add_user(self._username, self._password)
        if result:
            DB.commit()
        return result
    
    def delete_account(self):
        result = DB.remove_user(self._username)
        if result:
            DB.commit()
        return result
    
    def checkout_cart(self):
        self._cart.checkout(self.username, self._payment_info, self._shipping_address)
    
    def view_cart(self):
        self._cart.view()

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        self._username = value
        self._orders.username = value
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value

    @property
    def cart(self):
        return self._cart

    @property
    def orders(self):
        return self._orders


class ShoppingCart:
    
    def view(self):
        raise NotImplementedError

    def checkout(self, username, payment_info, shipping_address):
        DB.checkout_cart(username, payment_info, shipping_address)


class OrderHistory:
    def __init__(self, username):
        self.username = username

    def view(self):
        raise NotImplementedError


class Inventory:
    def __init__(self, category_id):
        self.category_id = category_id
    
    def fetch(self):
        rows = DB.fetch_inventory(0)
        items = []
        for row in rows:
            item_id = row[0]
            name = row[1]
            price = row[2]
            stock = row[3]

            items.append(InventoryItem(item_id, name, price, stock))
        return items


class InventoryItem:
    def __init__(self, item_id, name, price, stock):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.stock = stock

    def add_to_cart(self, username, quantity):
        DB.add_cart_item(username, self.item_id, quantity)
    
    def remove_from_cart(self, username, quantity):
        DB.remove_cart_item(username, self.item_id, quantity)

    def __str__(self):
        return "{} | {} | {}".format(self.item_id, self.stock, self.name)
