import ecommerce

STATE_LOGIN = 0
STATE_EXIT = 1
STATE_MAIN = 2
STATE_ACCOUNT_SETTINGS = 3
STATE_CART_INFO = 4
STATE_REMOVE_CART_ITEM = 5
STATE_ADD_CART_ITEM = 6

INPUT_ERROR_MSG = "Input must be a number"


def yes_or_no_prompt(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please answer 'y' or 'n'.")


def login(state, user):
    print("Login")
    print("-----------------")
    print("1. Login")
    print("2. Create Account")
    print("3. Exit Program")

    try:
        user_input = int(input("> "))

        if user_input == 1 or user_input == 2:
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            user.username = username
            user.password = password
            
            if user_input == 1:
                if user.verify_login():
                    print("Login successful")
                    state = STATE_MAIN
                else:
                    print("Login failed")
            elif user_input == 2:
                if user.create_account():
                    print("New account created")
                    state = STATE_MAIN
                else:
                    print("Username %s has been taken" % username)

        if user_input == 3:
            state = STATE_EXIT
    except ValueError:
        print(INPUT_ERROR_MSG)
    return state


def main_menu(state, user):
    print("Main Menu")
    print("--------------------")
    print("1. View Items")
    print("2. Cart Information")
    print("3. Order History")
    print("4. Account Settings")
    print("5. Logout")
    print("6. Exit Program")

    try:
        user_input = int(input("> "))

        if user_input == 1:
            inventory = ecommerce.Inventory(0)
            items = inventory.fetch()
            for item in items:
                print(item)
        if user_input == 2:
            state = STATE_CART_INFO
        if user_input == 3:
            user.view_orders()
        if user_input == 4:
            state = STATE_ACCOUNT_SETTINGS
        if user_input == 5:
            state = STATE_LOGIN
        if user_input == 6:
            state = STATE_EXIT
    except ValueError:
        print(INPUT_ERROR_MSG)
    return state


def account_settings(state, user):
    user.view_account_details()
    print("1. Edit shipping information")
    print("2. Edit payment information")
    print("3. Delete Account")
    print("4. Go Back")

    try:
        user_input = int(input("> "))

        if user_input == 1:
            new_shipping_address = input("Enter new shipping address: ")
            user.edit_shipping_address(new_shipping_address)
        if user_input == 2:
            new_payment_info = input("Enter new payment info: ")
            user.edit_payment_info(new_payment_info)
        if user_input == 3 and yes_or_no_prompt("Do you want to delete your account?"):
            user.delete_account()
            state = STATE_LOGIN
        if user_input == 4:
            state = STATE_MAIN
    except ValueError:
        print(INPUT_ERROR_MSG)
    return state


def cart_information(state, user):
    print("Cart Information")
    print("------------------------")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Checkout")
    print("5. Go Back")

    try:
        user_input = int(input("> "))

        if user_input == 1:
            state = STATE_ADD_CART_ITEM
        if user_input == 2:
            state = STATE_REMOVE_CART_ITEM
        if user_input == 3:
            user.view_cart()
        if user_input == 4:
            if user.cart_empty():
                print("Cannot checkout a cart that is empty")
            elif yes_or_no_prompt("Do you want to checkout?"):
                user.checkout_cart()
                print("Cart has been checkout. Order has been generated")
        if user_input == 5:
            state = STATE_MAIN
    except ValueError:
        print(INPUT_ERROR_MSG)
    return state


def add_cart_item(state, user):
    print("Add cart item")
    print("----------------------")

    inventory = ecommerce.Inventory(0)
    items = inventory.fetch()

    for i in range(len(items)):
        print("{}. {}".format(str(i+1), items[i]))
    print("{}. Go Back".format(str(len(items) + 1)))

    try:
        user_input = int(input("> ")) - 1

        if user_input >= 0 and user_input < len(items):
            items[user_input].add_to_cart(user.username, 1)
            state = STATE_CART_INFO
        if user_input == len(items):
            state = STATE_CART_INFO
    except ValueError:
        print(INPUT_ERROR_MSG)
    return state


def remove_cart_item(state, user):
    print("Remove cart item")
    print("----------------------")

    items = user.fetch_cart_items()
    for i in range(len(items)):
        print("{}. {}".format(str(i+1), items[i]))
    print("{}. Go Back".format(str(len(items) + 1)))

    try:
        user_input = int(input("> ")) - 1

        if user_input >= 0 and user_input < len(items):
            items[user_input].remove_from_cart(user.username, 1)
            state = STATE_CART_INFO
        if user_input == len(items):
            state = STATE_CART_INFO
    except ValueError:
        print(INPUT_ERROR_MSG)
    return state


if __name__ == "__main__":
    current_state = STATE_LOGIN
    user = ecommerce.User("", "")
    
    while (current_state != STATE_EXIT):
        if current_state == STATE_LOGIN:
            current_state = login(current_state, user)
        if current_state == STATE_MAIN:
            current_state = main_menu(current_state, user)
        if current_state == STATE_ACCOUNT_SETTINGS:
            current_state = account_settings(current_state, user)
        if current_state == STATE_CART_INFO:
            current_state = cart_information(current_state, user)
        if current_state == STATE_ADD_CART_ITEM:
            current_state = add_cart_item(current_state, user)
        if current_state == STATE_REMOVE_CART_ITEM:
            current_state = remove_cart_item(current_state, user)
    ecommerce.DB.close()