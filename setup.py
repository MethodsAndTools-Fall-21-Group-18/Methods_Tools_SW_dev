import json


def generate_db_settings():
    generated = {"database": "DATABASE", "user": "postgres", "password" : "PASSWORD"}
    f = open("settings/db_settings.json", 'w')
    json.dump(generated, f, indent=4)

if __name__ == "__main__":
    generate_db_settings()