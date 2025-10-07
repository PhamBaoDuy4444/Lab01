# app/auth.py
import bcrypt

def hash_password(plain_text_password):
    """Băm mật khẩu bằng bcrypt."""
    return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())

def verify_password(plain_text_password, hashed_password):
    """Xác thực mật khẩu."""
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)