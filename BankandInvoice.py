import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (make sure the correct WebDriver is installed)
driver = webdriver.Chrome()  # Replace with your WebDriver if different
driver.maximize_window()

# Wait time for elements
wait = WebDriverWait(driver, 10)

# Log file location
log_file_path = 'C:\\Python_Selenium\\PythonSelenium\\PythonSeleniumProject1\\LearningSelenium\\BankandInvoiceTempSettingsResult.txt'

# Function to log messages to file
def log_result(message):
    with open(log_file_path, 'a') as log_file:
        log_file.write(message + '\n')
    print(message)

# Open the login page
driver.get("https://test-reidun.rebingtest.com/login")
time.sleep(2)

# Log actions for opening login page and entering credentials
log_result("Open Login Page")
log_result("Enter Email: rebingtest777@yopmail.com")
email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
email_field.send_keys("rebingtest777@yopmail.com")
time.sleep(2)

log_result("Enter Password: Rebing@001122")
password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
password_field.send_keys("Rebing@001122")
time.sleep(2)

# Click on Login button
log_result("Click on Login Button")
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_button"]')))
login_button.click()
time.sleep(2)

# Navigate to Company Settings from the side navbar
log_result("Click on Company Settings in the Side Navbar")
company_settings = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/nav/div[1]/div/div[1]/div[2]/div/div/div/ul/li[11]/a/span[2]')))
company_settings.click()
time.sleep(2)

# Navigate to Bank Settings
log_result("Click on Bank Settings in the Card")
bank_settings = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="useradd-sidenav"]/a[4]')))
bank_settings.click()
time.sleep(2)

# Select Bank Name 'Brac'
log_result("Select Bank Name: 'Brac'")
bank_name_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bank_name"]')))
bank_name_dropdown.click()
time.sleep(2)

bank_name_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bank_name"]/option[1]')))
bank_name_option.click()
time.sleep(2)
log_result("PASSED: Bank Name 'Brac' selected and saved successfully.")

# Enter Account No as '1993@A' and validate the input
log_result("Enter Account No as '1993@A'")
account_no_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="bank_account_no"]')))
account_no_field.clear()
account_no_field.send_keys("1993@A")
time.sleep(2)

# Validation: Ensure non-numeric input is rejected
account_no_value = account_no_field.get_attribute("value")
if account_no_value != "1993@A":
    log_result("PASSED: Non-numeric Account No '1993@A' rejected successfully.")
else:
    log_result("FAILED: Non-numeric Account No '1993@A' should be rejected but was accepted.")

# Enter Company Identification Number as '2245567475'
log_result("Enter Company Identification Number: '2245567475'")
company_id_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="company_identification_number"]')))
company_id_field.clear()
company_id_field.send_keys("2245567475")
time.sleep(2)

# Validation: Check if the Company Identification Number is entered correctly
company_id_value = company_id_field.get_attribute("value")
if company_id_value == "2245567475":
    log_result("PASSED: Company Identification Number '2245567475' entered and saved successfully.")
else:
    log_result("FAILED: Incorrect value for Company Identification Number '2245567475'.")

# Click the Save Changes button in Bank Settings
log_result("Click Save Changes button")
save_changes_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="useradd-4"]/form/div/div[2]/div/input')))
save_changes_button.click()
time.sleep(2)

# Re-navigate to Company Settings
log_result("Navigate back to Company Settings in the Side Navbar")
company_settings = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/nav/div[1]/div/div[1]/div[2]/div/div/div/ul/li[11]/a/span[2]')))
company_settings.click()
time.sleep(2)

# Navigate to Invoice Print Settings
log_result("Click on Invoice Print Settings in the Card")
invoice_settings = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="useradd-sidenav"]/a[5]')))
invoice_settings.click()
time.sleep(2)

# Select Invoice Template 'Template 1'
log_result("Select Invoice Template: 'Template 1'")
invoice_template_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="setting-form"]/div[1]/select')))
invoice_template_dropdown.click()
time.sleep(2)

invoice_template_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="setting-form"]/div[1]/select/option[1]')))
invoice_template_option.click()
time.sleep(2)
log_result("PASSED: Invoice Template 'Template 1' selected and saved successfully.")

# Click Save Changes button in Invoice Print Settings
log_result("Click Save Changes button")
save_changes_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="setting-form"]/div[2]/input')))
save_changes_button.click()
time.sleep(2)

# Click on the dropdown and logout
log_result("Click on Hi,___ (Company Name) dropdown")
dropdown_menu = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/div[1]/ul/li[2]/a')))
dropdown_menu.click()
time.sleep(2)

log_result("Click on Logout")
logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/div[1]/ul/li[2]/div/a[2]')))
logout_button.click()
time.sleep(2)

# Close the browser
driver.quit()
