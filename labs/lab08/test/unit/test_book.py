# tests/test_unit/test_book.py
from app.book_management import validate_book_data

def test_validate_book_data_success():
    """Test case 1: Dữ liệu sách hợp lệ."""
    is_valid, message = validate_book_data("Lập trình Python", "Guido van Rossum", "978-0134076431")
    assert is_valid is True

def test_validate_book_data_missing_field():
    """Test case 2: Thiếu trường bắt buộc (tiêu đề)."""
    is_valid, message = validate_book_data("", "Một Tác Giả", "978-0134076431")
    assert is_valid is False
    assert "Tiêu đề và tác giả không được để trống" in message

def test_validate_book_data_invalid_isbn():
    """Test case 3: ISBN không hợp lệ."""
    is_valid, message = validate_book_data("Một Cuốn Sách", "Một Tác Giả", "12345")
    assert is_valid is False
    assert "ISBN không hợp lệ" in message