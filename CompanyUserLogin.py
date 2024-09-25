from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

# List of combinations to test in the name field
name_combinations = [
    "TestUser11", "TestUser22", "TestUser33", "TestUser44", "TestUser55"
]

# List of combinations to test in the email field
email_combinations = [
    "testuser111@example.com", "testuser22@example.com", "testuser33@example.com",
    "testuser44@example.com", "testuser55@example.com"
]

# List of combinations to test in the password field
password_combinations = [
    "Password1@", "AAkifAkifAkifAkifAkifAkifAkifAkifAkifAkifAkifQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQTTTT@#$%&&*((((*", "Password3@", "Password4@", "Password5@"
]

# Original credentials
original_name = "Original Name"
original_email = 'sajid123@yopmail.com'
original_password = 'Sajid@123859'

# Service for ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service)
driver.maximize_window()  # Maximize the browser window
driver.get("https://test-reidun.rebingtest.com/login")

# Define path for the TestResult.txt file
test_result_path = r'C:\\Users\\akifh\Desktop\\Flask App\\my_flask_app\\CompanyUserTestResult.txt'

# Define the tester's name and test date
tester_name = "Ashraful Hasan"
test_date = "4th September, 2024"

# Function to write to the TestResult.txt file
def log_to_file(message):
    with open(test_result_path, 'a') as file:
        file.write(message + '\n')

# Function to login with credentials
def login(email, password):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'login_button'))
        )
        actions = ActionChains(driver)

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        email_input.clear()
        email_input.send_keys(email)

        password_input = driver.find_element(By.ID, 'password')
        password_input.clear()
        password_input.send_keys(password)

        login_button = driver.find_element(By.ID, 'login_button')
        actions.move_to_element(login_button).click().perform()
        time.sleep(2)
        message = f'<strong class="text-success">PASSED::</strong>Logged in successfully with email: {email}'
        #message = f'<strong class="text-success">PASSED</strong> : : Logged in successfully with email: {email}'
        print(message)
        log_to_file(message)
    except Exception as e:
        message = f'<strong class="text-danger">FAILED::</strong>Error during login: {e}'
        print(message)
        log_to_file(message)

# Function to change name, email, and avatar
def change_name_email_avatar(name, email, avatar_path):
    actions = ActionChains(driver)

    try:
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/div[1]/ul/li[2]/a'))
        )
        actions.move_to_element(dropdown).click().perform()
        time.sleep(1)

        my_profile_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/div[1]/ul/li[2]/div/a[1]'))
        )
        actions.move_to_element(my_profile_option).click().perform()
        time.sleep(1)

        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="name"]'))
        )
        name_input.clear()
        name_input.send_keys(name)

        email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
        email_input.clear()
        email_input.send_keys(email)

        # Upload the avatar image
        choose_file_button = driver.find_element(By.XPATH, '//*[@id="avatar"]')
        actions.move_to_element(choose_file_button).perform()
        time.sleep(1)
        choose_file_button.send_keys(avatar_path)
        time.sleep(1)  # Pause to observe the file path being set

        # Save changes
        save_button = driver.find_element(By.XPATH, '//*[@id="personal_info"]/div[2]/form/div/div[4]/input')
        actions.move_to_element(save_button).click().perform()
        time.sleep(1)  # Observe the result after clicking save

        message = f'<strong class="text-success">PASSED::</strong>Profile updated to Name: {name}, Email: {email}'
        print(message)
        log_to_file(message)
    except Exception as e:
        message = f'<strong class="text-danger">FAILED::</strong>Error during name/email/avatar update: {e}'
        print(message)
        log_to_file(message)

# Function to change password
def change_password(old_password, new_password):
    actions = ActionChains(driver)

    try:
        old_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, old_password_xpath))
        )
        old_password_input.clear()
        old_password_input.send_keys(old_password)

        new_password_input = driver.find_element(By.XPATH, new_password_xpath)
        new_password_input.clear()
        new_password_input.send_keys(new_password)

        confirm_password_input = driver.find_element(By.XPATH, confirm_password_xpath)
        confirm_password_input.clear()
        confirm_password_input.send_keys(new_password)

        # Click Save Changes after entering the new password
        save_button = driver.find_element(By.XPATH, '//*[@id="change_password"]/div[2]/form/div/div[4]/input')
        actions.move_to_element(save_button).click().perform()
        time.sleep(1)  # Increased wait time to ensure save action completes

        message = f'<strong class="text-success">PASSED::</strong>Password was successfully updated to: {new_password}'
        print(message)
        log_to_file(message)
    except Exception as e:
        message = f'<strong class="text-danger">FAILED::</strong>Error during password update: {e}'
        print(message)
        log_to_file(message)

# Function to logout
def logout():
    actions = ActionChains(driver)

    try:
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/div[1]/ul/li[2]/a'))
        )
        actions.move_to_element(dropdown).click().perform()
        time.sleep(1)

        logout_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/div[1]/ul/li[2]/div/a[2]'))
        )
        actions.move_to_element(logout_option).click().perform()
        time.sleep(1)
        message = '<strong class="text-success">PASSED::</strong>Successfully logged out.'
        print(message)
        log_to_file(message)
    except Exception as e:
        message = f'<strong class="text-danger">FAILED::</strong>Error during logout: {e}'
        print(message)
        log_to_file(message)

# XPath for password fields
old_password_xpath = '//*[@id="current_password"]'
new_password_xpath = '//*[@id="new_password"]'
confirm_password_xpath = '//*[@id="confirm_password"]'

# Write initial test information to file
with open(test_result_path, 'w') as file:
    file.write(f"Tester's Name: {tester_name}\n")
    file.write(f"Test Date: {test_date}\n")
    file.write("=======================================\n")

# Login with original credentials
login(original_email, original_password)

# Test name, email, and avatar changes along with password
avatar_path = r'C:\Users\akifh\Desktop\New folder (4)\ronaldo.jpeg'
for i in range(5):
    name = name_combinations[i]
    email = email_combinations[i]
    password = password_combinations[i]

    # Change name, email, and avatar
    change_name_email_avatar(name, email, avatar_path)
    time.sleep(1)

    # Change password
    change_password(original_password if i == 0 else password_combinations[i-1], password)
    time.sleep(1)

    # Save changes after changing password
    save_button = driver.find_element(By.XPATH, '//*[@id="personal_info"]/div[2]/form/div/div[4]/input')
    save_button.click()
    time.sleep(1)

    # Logout after each update
    logout()

    # Re-login with the new email and password to verify
    driver.get("https://test-reidun.rebingtest.com/login")
    login(email, password)

# Revert to original name, email, and password
change_name_email_avatar(original_name, original_email, avatar_path)
time.sleep(2)

change_password(password_combinations[-1], original_password)
time.sleep(1)

# Save changes after reverting password
save_button = driver.find_element(By.XPATH, '//*[@id="personal_info"]/div[2]/form/div/div[4]/input')
save_button.click()
time.sleep(1)

# Logout
logout()

# Quit the browser
driver.quit()
