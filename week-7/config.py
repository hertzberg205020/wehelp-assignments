import hashlib

SECRET_KEY = hashlib.sha256(b"123456").hexdigest()