from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Khởi động trình duyệt Chrome
driver = webdriver.Chrome()

# Mở trang web
driver.get("https://demoqa.com/automation-practice-form")

# Tăng kích thước cửa sổ để tránh lỗi ẩn phần tử
driver.maximize_window()

# Chờ tối đa 10 giây để phần tử xuất hiện
wait = WebDriverWait(driver, 10)

# Điền First Name
name_field = wait.until(EC.presence_of_element_located((By.ID, "firstName")))
name_field.send_keys("Nguyen Van A")

# Điền Last Name
last_name_field = driver.find_element(By.ID, "lastName")
last_name_field.send_keys("Test")

# Điền Email
email_field = driver.find_element(By.ID, "userEmail")
email_field.send_keys("testemail@example.com")

# Chọn giới tính: Male (giá trị 'Male', 'Female', hoặc 'Other')
gender_radio = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
gender_radio.click()

# Điền số điện thoại
phone_field = driver.find_element(By.ID, "userNumber")
phone_field.send_keys("0123456789")

# Chọn ngày sinh
date_input = driver.find_element(By.ID, "dateOfBirthInput")
date_input.click()

# Chọn tháng và năm (ví dụ: tháng 5 năm 1995)
month_select = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
month_select.send_keys("May")

year_select = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
year_select.send_keys("1995")

# Chọn ngày (ví dụ ngày 15)
day = driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='15']")
day.click()

# Điền địa chỉ
address_field = driver.find_element(By.ID, "currentAddress")
address_field.send_keys("123 Nguyen Trai, Hanoi")

# (Tuỳ chọn) Dừng vài giây để quan sát trước khi đóng
time.sleep(3)

# Đóng trình duyệt
driver.quit()
