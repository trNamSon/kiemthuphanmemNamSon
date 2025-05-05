from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Khởi tạo WebDriver
driver = webdriver.Chrome()

try:
    # 1. Mở Google
    driver.get("https://www.google.com")

    # 2. Tìm ô nhập tìm kiếm
    search_box = driver.find_element(By.NAME, "q")

    # 3. Nhập từ khóa cần tìm và nhấn Enter
    search_box.send_keys("Selenium WebDriver")
    search_box.send_keys(Keys.RETURN)

    # 4. Chờ vài giây cho kết quả hiển thị
    time.sleep(3)

    # 5. Kiểm tra xem kết quả đầu tiên có chứa từ "Selenium"
    first_result = driver.find_element(By.XPATH, "(//h3)[1]").text

    if "Selenium" in first_result:
        print("Test Passed: Kết quả đầu tiên có chứa 'Selenium'")
    else:
        print("Test Failed: Kết quả đầu tiên không liên quan")

finally:
    # 6. Đóng trình duyệt sau 10 giây để quan sát
    time.sleep(10)
    driver.quit()
