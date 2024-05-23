# tests/test_password.py
from psyche_system.password import PasswordManager

def test_create_password():
    pm = PasswordManager()
    password = "securepassword"
    stored = pm.create_password(password)
    assert stored is not None
    assert isinstance(stored, str)

def test_verify_password():
    pm = PasswordManager()
    password = "securepassword"
    stored = pm.create_password(password)
    assert pm.verify_password(stored, password) == True
    assert pm.verify_password(stored, "wrongpassword") == False
