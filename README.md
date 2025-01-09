# Instagram Bot

This project is an Instagram bot that automates sending messages using Selenium WebDriver.

## Prerequisites

1. **Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Selenium**: Install Selenium using pip:
    ```sh
    pip install selenium
    ```

3. **Microsoft Edge WebDriver**:
    - Check your Microsoft Edge version by navigating to `edge://settings/help` in the Edge browser.
    - Download the corresponding version of Edge WebDriver from [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
    - Extract the downloaded WebDriver to a directory of your choice.

4. **Set Environment Variable**:
    - Add the directory containing `msedgedriver.exe` to your system's PATH environment variable.
    - On Windows:
        1. Open the Start Search, type in "env", and select "Edit the system environment variables".
        2. In the System Properties window, click on the "Environment Variables" button.
        3. In the Environment Variables window, find the "Path" variable in the "System variables" section and click "Edit".
        4. Click "New" and add the path to the directory containing `msedgedriver.exe`.
        5. Click "OK" to close all windows.

## Running the Script

1. Clone this repository:
    ```sh
    git clone https://github.com/yourusername/insta-bot.git
    cd insta-bot
    ```

2. Run the script:
    ```sh
    python inst_bot.py
    ```

3. Follow the prompts to enter your Instagram username, password, recipient's username, message, and the number of times to send the message.

## Additional Notes

- Ensure your Instagram account is not protected by two-factor authentication, or handle the 2FA process within the script.
- Be aware of Instagram's rate limits and usage policies to avoid getting your account temporarily blocked.

## Disclaimer

This script is for educational purposes only. Use it responsibly and at your own risk.