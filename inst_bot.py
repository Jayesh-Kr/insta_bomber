from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import time

def login_to_instagram(driver, username, password):
    """Login to Instagram account"""
    try:
        # Navigate to Instagram login page
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)  # Wait for page to load

        # Enter username
        username_input = driver.find_element(By.NAME, 'username')
        username_input.send_keys(username)

        # Enter password
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)
        password_input.submit()

        # Wait for login to complete
        time.sleep(5)
        
    except Exception as e:
        print(f"Error during login: {e}")
        raise

def navigate_and_start_message(driver, recipient, message, repeat_count):
    """Navigate to new message page, handle popup, and start new message"""
    try:
        # Go to new message page
        driver.get('https://www.instagram.com/direct/new/')
        time.sleep(3)

        # Handle notification popup if it appears
        try:
            notification_popup = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//button[text()="Not Now"]'))
            )
            notification_popup.click()
            time.sleep(2)
        except:
            print("No notification popup found or already handled")

        # Click on "Send message" div
        try:
            send_message_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[text()='Send message']"))
            )
            send_message_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error clicking Send message: {e}")
            raise

        # Find and fill the recipient input field
        try:
            recipient_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'queryBox'))
            )
            recipient_input.send_keys(recipient)
            time.sleep(2)
            
            # Find and click the first checkbox in the search results
            first_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']"))
            )
            first_checkbox.click()
            time.sleep(1)

            # Click on the Chat div
            chat_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[text()='Chat']"))
            )
            chat_button.click()
            time.sleep(2)

            # Send the message multiple times
            try:
                message_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-placeholder="Message..."]'))
                )
                
                for i in range(repeat_count):
                    message_input.send_keys(message)
                    message_input.send_keys(Keys.RETURN)
                    print(f"Message {i + 1} sent: {message}")
                    time.sleep(0.25)  # Wait between messages to avoid rate limiting
                
                print(f"All {repeat_count} messages sent successfully!")

            except Exception as e:
                print(f"Error sending messages: {e}")
                raise

        except Exception as e:
            print(f"Error in recipient selection process: {e}")
            raise

    except Exception as e:
        print(f"Error in navigation process: {e}")
        raise

def get_user_input():
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    recipient = input("Enter recipient's username: ")
    message = input("Enter the message to send: ")
    
    while True:
        try:
            repeat_count = int(input("Enter number of times to send message: "))
            if repeat_count > 0:
                break
            print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")
    
    return username, password, recipient, message, repeat_count


def main():
    # Get user inputs
    USERNAME, PASSWORD, RECIPIENT, MESSAGE, REPEAT_COUNT = get_user_input()

    # Initialize Edge WebDriver
    service = Service(r"C:\\Users\\HP\\Downloads\\edgedriver_win32\\msedgedriver.exe")  # Replace with your Edge driver path
    driver = webdriver.Edge(service=service)
    
    try:
        # Set window size and implicit wait
        driver.set_window_size(1200, 800)
        driver.implicitly_wait(5)

        # Execute login and navigation
        login_to_instagram(driver, USERNAME, PASSWORD)
        navigate_and_start_message(driver, RECIPIENT, MESSAGE, REPEAT_COUNT)
        
        # Keep the browser open for a few seconds to see the result
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()