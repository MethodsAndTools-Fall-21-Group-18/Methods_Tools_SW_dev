import ecommerce

STATE_LOGIN = 0
STATE_EXIT = 1
STATE_MAIN = 2
STATE_ACCOUNT_SETTINGS = 3
STATE_CART_INFO = 4

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


def main_menu(state):
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


if __name__ == "__main__":
    current_state = STATE_LOGIN
    user = ecommerce.User("", "")
    
    while (current_state != STATE_EXIT):
        if current_state == STATE_LOGIN:
            current_state = login(current_state, user)
        if current_state == STATE_MAIN:
            current_state = main_menu(current_state)
        if current_state == STATE_ACCOUNT_SETTINGS:
            current_state = account_settings(current_state, user)
        if current_state == STATE_CART_INFO:
            break
    ecommerce.DB.close()