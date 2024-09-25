from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()  # Maximize the browser window
driver.get("https://test-reidun.rebingtest.com/login")

# Logging result file setup
test_result_path = r"C:\\Users\\akifh\Desktop\\Flask App\\my_flask_app\\BrndSettingsTestResult.txt"
tester_name = "Ashraful Hasan"
test_date = datetime.now().strftime("%dth %B, %Y")
result = f"Tester's Name: {tester_name}\nTest Date: {test_date}\n\n"

# Function to log results
def log_result(message):
    global result
    result += message + "\n"
    with open(test_result_path, "w") as file:
        file.write(result)
    print(message)  # Print messages to the console

# Function to handle errors and continue
def perform_action(action, success_message, failure_message):
    try:
        action()
        log_result(success_message)
    except Exception as e:
        log_result(failure_message + f" - Error: {str(e)}")

# Function to wait for element to be clickable
def wait_for_clickable(xpath, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))

# Function to login
def login():
    try:
        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
        email_input.clear()
        email_input.send_keys("rebingtest777@yopmail.com")
        time.sleep(1)

        password_input = driver.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys("Rebing@001122")
        time.sleep(1)

        login_button = driver.find_element(By.ID, 'login_button')
        login_button.click()
        time.sleep(1)

        log_result('<strong class="text-success">PASSED::</strong>Entered email, password, and clicked login button. Login successful.')
    except Exception as e:
        log_result(f'<strong class="text-danger">FAILED::</strong>Login failed - Error: {str(e)}')

# Function to update Title Text
# Function to update Title Text with validation and logging
def update_title_text():
    title_text_xpath = '//*[@id="title_text"]'
    title_text_inputs = [
        "Test", "Example@#$", "Special$Chars%", "1234567890", "TitleTest",
        "LongTitle-" * 30, "Short", "Title#@!", "Numbers1234", "Title!@#"
    ]

    for text in title_text_inputs:
        try:
            # Find the title input field and scroll into view
            title_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, title_text_xpath)))
            driver.execute_script("arguments[0].scrollIntoView(true);", title_input)
            time.sleep(1)  # Allow time for scrolling

            # Clear the field and input the text
            title_input.clear()
            title_input.send_keys(text)
            time.sleep(1)

            # Click the Save Changes button
            save_button = wait_for_clickable('//*[@id="useradd-1"]/form/div[2]/div/div[3]/div/input')
            save_button.click()
            time.sleep(1)

            # Validate if the input contains only alphabets
            if text.isalpha():
                log_result(f'<strong class="text-success">PASSED::</strong> Entered title text: "{text}". Save Changes button clicked. Title text updated and saved successfully.')
            else:
                reason = "Title should have only alphabet."
                log_result(f'<strong class="text-danger">FAILED::</strong> Entered title text: "{text}". Save Changes button clicked. <strong class="text-danger">Reason::</strong> {reason}')
        except Exception as e:
            log_result(f'<strong class="text-danger">FAILED::</strong>Failed to update title text with "{text}" - Error: {str(e)}')


# Function to toggle Dark Layout checkbox
# Function to toggle Dark Layout checkbox
def toggle_dark_layout():
    dark_layout_xpath = '//*[@id="cust-darklayout"]'
    try:
        for _ in range(2):
            # Locate the checkbox each time
            dark_layout_checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, dark_layout_xpath)))
            driver.execute_script("arguments[0].scrollIntoView(true);", dark_layout_checkbox)
            time.sleep(1)  # Allow time for scrolling

            dark_layout_checkbox.click()
            time.sleep(1)

            save_button = wait_for_clickable('//*[@id="useradd-1"]/form/div[2]/div/div[3]/div/input')
            save_button.click()
            time.sleep(1)

        log_result('<strong class="text-success">PASSED::</strong>Dark Layout checkbox clicked twice and Save Changes button clicked after each toggle.')
    except Exception as e:
        log_result(f'<strong class="text-danger">FAILED::</strong>Failed to toggle Dark Layout - Error: {str(e)}')


# Function to change theme colors
def change_theme_color(theme_xpath, theme_number):
    try:
        theme = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, theme_xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", theme)
        time.sleep(1)  # Allow time for scrolling

        theme.click()
        time.sleep(1)

        save_button = wait_for_clickable('//*[@id="useradd-1"]/form/div[2]/div/div[3]/div/input')
        save_button.click()
        time.sleep(1)

        log_result(f'<strong class="text-success">PASSED::</strong>Theme {theme_number} clicked and Save Changes button clicked.')
    except Exception as e:
        log_result(f'<strong class="text-danger">FAILED::</strong>Failed to change to Theme {theme_number} - Error: {str(e)}')

# Function to logout
def logout():
    try:
        dropdown = wait_for_clickable('/html/body/header/div/div[1]/ul/li[2]/a')
        dropdown.click()
        time.sleep(2)

        logout_option = wait_for_clickable('/html/body/header/div/div[1]/ul/li[2]/div/a[2]')
        logout_option.click()
        time.sleep(2)

        log_result('<strong class="text-success">PASSED::</strong>Logout successful.')
    except Exception as e:
        log_result(f'<strong class="text-danger">FAILED::</strong>Logout failed - Error: {str(e)}')

# Perform the actions in sequence
login()

# Click on Company Settings and Brand Settings
perform_action(
    lambda: driver.find_element(By.XPATH, '/html/body/nav/div[1]/div/div[1]/div[2]/div/div/div/ul/li[11]/a/span[2]').click(),
    "<strong>Navigated to Company Settings.</strong>",
    "<strong>Failed to navigate to Company Settings.</strong>"
)

perform_action(
    lambda: driver.find_element(By.XPATH, '//*[@id="useradd-sidenav"]/a[1]').click(),
    "<strong>Navigated to Brand Settings.</strong>",
    "<strong>Failed to navigate to Brand Settings.</strong>"
)

# Update title text and click Save Changes after each input
update_title_text()

# Toggle dark layout twice and click Save Changes
toggle_dark_layout()

# Test all theme colors
theme_xpaths = [
    '//*[@id="useradd-1"]/form/div[2]/div/div[2]/div/div[1]/div/a[1]',
    '//*[@id="useradd-1"]/form/div[2]/div/div[2]/div/div[1]/div/a[2]',
    '//*[@id="useradd-1"]/form/div[2]/div/div[2]/div/div[1]/div/a[3]',
    '//*[@id="useradd-1"]/form/div[2]/div/div[2]/div/div[1]/div/a[4]',
    '//*[@id="useradd-1"]/form/div[2]/div/div[2]/div/div[1]/div/a[5]',
    '//*[@id="useradd-1"]/form/div[2]/div/div[2]/div/div[1]/div/a[6]',
    '//*[@id="useradd-1"]/form/div[2]/div/div[2]/div/div[1]/div/a[7]',
    '//*[@id="useradd-1"]/form/div[2]/div/div[2]/div/div[1]/div/a[8]',
    '//*[@id="useradd-1"]/form/div[2]/div/div[2]/div/div[1]/div/a[9]',
    '//*[@id="useradd-1"]/form/div[2]/div/div[2]/div/div[1]/div/a[10]'
]

for i, theme_xpath in enumerate(theme_xpaths, start=1):
    change_theme_color(theme_xpath, i)

# Logout
logout()

# Quit the browser
driver.quit()