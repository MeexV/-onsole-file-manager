import pytest
import console_file_manager

def test_name():
    assert console_file_manager.name_creator("Voronin Maxim") == "Voronin Maxim"