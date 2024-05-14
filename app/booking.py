from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def book_gym(email, password, booking_time):
    driver = webdriver.Chrome()
    driver.get("https://gym-booking-website.com")

    driver.find_element_by_id("username").send_keys(email)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("login-button").click()

    time.sleep(2)  # Adjust based on site load time

    # Navigate and book
    # Example:
    driver.find_element_by_id("desired_time").send_keys(booking_time)
    driver.find_element_by_id("book_button").click()

    time.sleep(2)  # Adjust based on confirmation load time
    driver.quit()
