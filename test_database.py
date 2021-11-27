
user = "alice"
password = "password123"

def test_add_user(db):
    # Test adding user
    assert db.add_user(user, password) == True

    # Test adding user with username that already exists
    assert db.add_user(user, password) == False


def test_remove_user(db):
    assert db.remove_user("test") == True
    assert db.remove_user("notest") == False


def test_adding_removing_user(db):
    # Test adding user when the user does not exist
    assert db.add_user(user, password) == True
    db.commit()

    # Test adding user when user does exist
    assert db.add_user(user, password) == False
    db.commit()

    # Test removing user when user does exist
    assert db.remove_user(user) == True
    db.commit()

    # Test removing user when user does not exist
    assert db.remove_user(user) == False
    db.commit()


def test_edit_payment_info(db):
    assert db.edit_payment_info("test", "2142335") == True
    assert db.edit_payment_info("notest", "2142335") == False


def test_edit_shipping_address(db):
    assert db.edit_shipping_address("test", "123 ABC Street") == True
    assert db.edit_shipping_address("notest", "123 ABC Street") == False


def test_user_exists(db):
    assert db.is_user_exists("test", "test") == True
    assert db.is_user_exists("test", "notest") == False
    assert db.is_user_exists("notest", "notest") == False
