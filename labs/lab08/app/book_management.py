# app/book_management.py

def validate_book_data(title, author, isbn):
    """
    Kiểm tra dữ liệu đầu vào của sách.
    Trả về (True, "Success") nếu hợp lệ, ngược lại (False, "Error Message").
    """
    if not title or not author:
        return (False, "Tiêu đề và tác giả không được để trống.")

    if isbn:
        cleaned_isbn = isbn.replace('-', '')
    else:
        cleaned_isbn = ""

    if not cleaned_isbn or len(cleaned_isbn) not in [10, 13]:
        return (False, "ISBN không hợp lệ.")
        
    return (True, "Dữ liệu hợp lệ.")