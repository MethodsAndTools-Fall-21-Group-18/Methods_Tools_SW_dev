def welcome():
    print("Welcome to your dashboard")


def register():
    db = open("database.txt", "r")
    userName = input("Create a username:")
    passWord = input("Create password:")
    passWord1 = input("Confirm Password:")
    # Now we will match up Usernames with their corresponding password
    d = []  # Empty list to store username
    f = []  # Empty list to store password
    for i in db:
        a, b = i.split(", ")  # a,b: we want to split the text
        b = b.strip()  # We need password to stand alone: b.strip() will remove any space from comma to password
        d.append(a)  # add Username to the list
        f.append(b)  # add password to the list
    data = dict(zip(d, f))  # Combining the password and username into a Dictionary
    print(data)
    if passWord != passWord1:
        print("Passwords don't match, restart")
        register()
    else:
        if len(passWord) <= 6:
            print("Password too short, restart:")
            register()
        elif userName in d:
            print("username exists")
            register()
        else:
            db = open("database.txt", "a")
            db.write(userName+", "+passWord+"\n")
            print("Success!")


def access():
    db = open("database.txt", "r")
    userName = input("Enter your username:")
    passWord = input("Enter your password:")

    if not len(userName or passWord) < 1:
        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
            data = dict(zip(d, f))

            try:
                if data[userName]:   # check if username user entered is in the database.txt
                    try:
                        if passWord == data[userName]:  # check if the user name and password match
                            print("login success")
                            print("Hi,", userName)
                        else:
                            print("Password or Username is Incorrect.")
                    except:
                        print("Incorrect password or username.")

                else:
                    print("Username doesn't exist")
            except:
                print("Username or Password Doesn't exist.")
        else:
            print("Please enter a value.")



def home(option=None):
    welcome()
    print("Welcome, please select an option")
    option = input("Login | Signup:")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Please enter a valid parameter, this is case-sensitive")

home()