# password.py
import hashlib
import os
import base64

class PasswordManager:
    def create_password(self, password):
        salt = os.urandom(16)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        storage = base64.b64encode(salt + key).decode('utf-8')
        return storage

    def verify_password(self, stored_password, provided_password):
        decoded = base64.b64decode(stored_password)
        salt = decoded[:16]
        key = decoded[16:]
        new_key = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
        return new_key == key
