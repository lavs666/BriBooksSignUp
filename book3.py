import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException

# Set up the Chrome WebDriver and options


try:
    try:
        chrome_driver_path = "C:\\Users\\trive\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe"
        service = Service(chrome_driver_path)  # Update the path to your chromedriver
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=service, options=options)

        # Navigate to the Bribooks website
        driver.get('https://www.bribooks.com/signup')

        # Set up explicit wait
        wait = WebDriverWait(driver, 10)  # 10 seconds timeout
    except Exception as e:
        print(f"An unexpected error occurred in launch driver : {e}")
        raise "Failed to launch driver"

    try:
        username_field = wait.until(EC.visibility_of_element_located((By.ID, 'formName')))
        username_field.send_keys('your_username')
    except (TimeoutException, NoSuchElementException):
        print("Username field not found or not visible.")
        raise "Failed to find username"


    # Enter email in the 'formEmail' field
    try:
        email_field = wait.until(EC.visibility_of_element_located((By.ID, 'formEmail')))
        email_field.send_keys('your_username@gmail.com')
    except (TimeoutException, NoSuchElementException):
        print("Email field not found or not visible.")
        raise "Failed to find email"

    # Enter phone number
    try:
        phone_xpath = "//*[@id='__next']/div/main/div[1]/div/div/div[2]/div/div[2]/div/div/form/div/div[3]/div/input"
        phone_field = wait.until(EC.visibility_of_element_located((By.XPATH, phone_xpath)))
        phone_field.send_keys('12334856')
    except (TimeoutException, NoSuchElementException):
        print("Phone field not found or not visible.")
        raise "Failed to find phone"

    # Click the OTP button
    try:
        otp_button_xpath = "/html/body/div[1]/div/main/div[1]/div/div/div[2]/div/div[2]/div/div/form/div/div[3]/button"
        otp_button = wait.until(EC.element_to_be_clickable((By.XPATH, otp_button_xpath)))
        otp_button.click()
    except (TimeoutException, ElementNotInteractableException):
        print("OTP button not found or not clickable.")
        raise "Failed to find otp"
    # time.sleep(30)

    try:
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id=\"__next\"]/div/main/div[1]/div/div/div[2]/div/div[2]/div/div/div[2]/label[1]")))
    except TimeoutException:
        print("OTP completion step not found or not visible.")
    # time.sleep(30)


except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # Clean up and close the browser
    driver.quit()
