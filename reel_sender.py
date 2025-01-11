from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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

def navigate_to_reel(driver,recipient,num_reels):
    try:
        driver.get('https://www.instagram.com/reels/')
        time.sleep(3)
        for i in range(num_reels):
            try:
                share_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'svg[aria-label="Share"]'))
                )
                share_button.click()
                time.sleep(2)
            except:
                print("No share button found or already handled")

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

                # Click on the Send div
                send_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[text()='Send']"))
                )
                send_button.click()
                time.sleep(2)

                if i < num_reels - 1:
                    actions = ActionChains(driver)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(2)
            except Exception as e:
                print(f"Error sharing reel {i+1}: {e}")
                continue
    except:
        print('No reel section found')
        




# Get user input function
def get_user_input():
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    return username, password


def main():
    # Get user inputs
    USERNAME, PASSWORD = get_user_input()

    # Initialize Edge WebDriver
    service = Service(r"C:\\Users\\HP\\Downloads\\edgedriver_win32\\msedgedriver.exe")  # Replace with your Edge driver path
    driver = webdriver.Edge(service=service)
    
    try:
        # Set window size and implicit wait
        driver.set_window_size(1200, 800)
        driver.implicitly_wait(5)

        # Execute login and navigation
        login_to_instagram(driver, USERNAME, PASSWORD)
        navigate_to_reel(driver,'Fucker',3)
        
        # Keep the browser open for a few seconds to see the result
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()


if __name__ == "__main__":
    main()