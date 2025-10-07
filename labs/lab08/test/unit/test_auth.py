# tests/test_unit/test_auth.py
from app.auth import hash_password, verify_password

def test_verify_password_correct():
    """Test case 1: Kiểm tra mật khẩu ĐÚNG."""
    password = "MyStrongPassword123"
    hashed = hash_password(password)
    assert verify_password(password, hashed) is True

def test_verify_password_incorrect():
    """Test case 2: Kiểm tra mật khẩu SAI."""
    password = "MyStrongPassword123"
    hashed = hash_password(password)
    assert verify_password("WrongPassword", hashed) is False