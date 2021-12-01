# Methods_And_Tools_Project
This project is an implementation of the requirements for the group project assigned in Methods and Tools in SW Development.

## Requirements
- [Python 3.9+](https://www.python.org/downloads/)
- [PostgreSQL 14.1](https://www.postgresql.org/download/)
    - pgAdmin4 (Included with EDB installer for PostgreSQL 14.1)

## Install
1. Clone or download the repositiory
2. Go the cloned/downloaded repositiory
3. Run these commands:
```
$ python -m venv env
$ ./env/Scripts/activate
$ pip install -r requirements.txt
$ python setup.py
```
4. Setup PostgreSQL and open pgAdmin4
5. Create a database
6. Open query tool on newly created database
7. Copy and paste text from `sql-queries.txt` to query editor and run the query
8. Edit settings/db_settings.json
    - Replace "DATABASE" with the name of the database
    - Replace "PASSWORD" with the password to access the database
    - (Optional) Replace "postgres" with the username to access the database assuming using a different username
9. Run `python driver.py`

## Team
Group Number: 18 
- Henry Nhan (hjn31)
- Andrew Hsu (aeh458)
- Will Cozart (wec125)
- Matthew Gaines (mcg440)