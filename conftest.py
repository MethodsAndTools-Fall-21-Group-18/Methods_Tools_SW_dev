import pytest
import database
import json_loader

@pytest.fixture
def db():
    db_settings = json_loader.decode_json("settings/db_settings.json")
    return database.Database(db_settings["database"], db_settings["user"], db_settings["password"])