
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
