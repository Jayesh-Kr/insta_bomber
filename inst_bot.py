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

def navigate_and_start_message(driver, recipient):
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
            
            # Wait for the search results to appear and click the first result
            search_results = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div[@role='button']"))
            )
            search_results.click()
            time.sleep(1)

        except Exception as e:
            print(f"Error entering recipient: {e}")
            raise

    except Exception as e:
        print(f"Error in navigation process: {e}")
        raise

def main():
    # Your Instagram credentials
    USERNAME = 'rj.tk_'
    PASSWORD = '@raj1234'
    RECIPIENT = 'Fucker'

    # Initialize Edge WebDriver
    service = Service(r"C:\\Users\\HP\\Downloads\\edgedriver_win32\\msedgedriver.exe")  # Replace with your Edge driver path
    driver = webdriver.Edge(service=service)
    
    try:
        # Set window size and implicit wait
        driver.set_window_size(1200, 800)
        driver.implicitly_wait(5)

        # Execute login and navigation
        login_to_instagram(driver, USERNAME, PASSWORD)
        navigate_and_start_message(driver, RECIPIENT)
        
        # Keep the browser open for a few seconds to see the result
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()