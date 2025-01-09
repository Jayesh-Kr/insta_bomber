from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Your Instagram credentials
INSTAGRAM_USERNAME = 'rj.tk_'
INSTAGRAM_PASSWORD = 'password'

def login(driver):
    print("Navigating to Instagram login page...")
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(5)

    # Enter username
    print("Entering username...")
    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys(INSTAGRAM_USERNAME)

    # Enter password
    print("Entering password...")
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(INSTAGRAM_PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)
    print("Login successful.")

def send_message(driver, recipient, message, repeat_count=10):
    print("Navigating to the new message page...")
    driver.get('https://www.instagram.com/direct/new/')
    time.sleep(5)

    # Handle the "Turn on Notifications" popup
    try:
        print("Checking for 'Not Now' popup...")
        not_now_button = driver.find_element(By.XPATH, '//button[text()="Not Now"]')
        not_now_button.click()
        print("'Not Now' popup closed.")
        time.sleep(2)
    except Exception as e:
        print("No 'Not Now' popup found or it was already handled.")

    # Enter recipient's username
    print(f"Entering recipient username: {recipient}...")
    recipient_input = driver.find_element(By.NAME, 'queryBox')
    recipient_input.send_keys(recipient)
    time.sleep(2)
    recipient_input.send_keys(Keys.ENTER)
    time.sleep(1)

    # Confirm recipient
    print("Confirming recipient...")
    next_button = driver.find_element(By.XPATH, '//button[text()="Next"]')
    next_button.click()
    time.sleep(5)
    print("Recipient confirmed.")

    # Send the message multiple times
    print(f"Sending message '{message}' to {recipient}...")
    for i in range(repeat_count):
        try:
            message_input = driver.find_element(By.TAG_NAME, 'textarea')
            message_input.send_keys(message)
            message_input.send_keys(Keys.RETURN)
            print(f"Message {i + 1} sent.")
            time.sleep(1)
        except Exception as e:
            print(f"Error sending message {i + 1}: {e}")

if __name__ == '__main__':
    # Initialize WebDriver for Edge
    service = Service(r"C:\\Users\\HP\\Downloads\\edgedriver_win32\\msedgedriver.exe")  # Replace with the actual path to msedgedriver.exe
    driver = webdriver.Edge(service=service)

    try:
        login(driver)
        send_message(driver, 'Fucker', 'Hello, Fucker! This is a test message!', 1)
    finally:
        print("Closing the browser...")
        driver.quit()
        print("Browser closed.")
