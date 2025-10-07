# tests/test_integration/selenium_test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Giả sử ứng dụng web của bạn đang chạy ở địa chỉ này
BASE_URL = "http://127.0.0.1:5000"

# -- Helper Function --
def setup_driver():
    # Cấu hình để chạy Selenium, bạn có thể cần cài đặt chromedriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") # Chạy ở chế độ không giao diện
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver

def test_login_success():
    """Test case 1: Đăng nhập thành công."""
    driver = setup_driver()
    driver.get(f"{BASE_URL}/login")

    # Giả sử các input có name là 'email' và 'password'
    driver.find_element(By.NAME, "email").send_keys("admin@example.com")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1) # Chờ trang tải lại

    # Kiểm tra đã chuyển hướng đến trang dashboard và có lời chào
    assert "/dashboard" in driver.current_url
    welcome_message = driver.find_element(By.TAG_NAME, "h1").text
    assert "Chào mừng, admin" in welcome_message
    driver.quit()

def test_login_failed_wrong_password():
    """Test case 2: Đăng nhập sai mật khẩu."""
    driver = setup_driver()
    driver.get(f"{BASE_URL}/login")

    driver.find_element(By.NAME, "email").send_keys("admin@example.com")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)

    # Kiểm tra thông báo lỗi xuất hiện
    error_message = driver.find_element(By.ID, "error-message").text
    assert "Email hoặc mật khẩu không đúng" in error_message
    driver.quit()

def test_login_empty_input():
    """Test case 3: Để trống input."""
    driver = setup_driver()
    driver.get(f"{BASE_URL}/login")

    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)

    # Kiểm tra thông báo lỗi
    error_message = driver.find_element(By.ID, "error-message").text
    assert "Vui lòng điền đầy đủ thông tin" in error_message
    driver.quit()