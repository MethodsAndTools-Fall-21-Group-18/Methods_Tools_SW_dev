import psycopg2

class Database:
    def __init__(self, database, user, password):
        self._connection = psycopg2.connect(database=database, user=user, password=password)
        self._cursor = self._connection.cursor()
    
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
        self._cursor.execute("DELETE FROM users WHERE username=%s", (username,))
        return self._cursor.rowcount == 1