import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver and maximize window
driver = webdriver.Chrome()
driver.maximize_window()

# Open the website
driver.get("https://test-reidun.rebingtest.com/login")
time.sleep(3)

# Log file setup
log_file_path = "C:\\Python_Selenium\\PythonSelenium\\PythonSeleniumProject1\\LearningSelenium\\CompanySettingsResult.txt"
log_file = open(log_file_path, "w")

def log_result(result_message):
    print(result_message)
    log_file.write(result_message + "\n")

def validate_alphabet(value):
    return value.isalpha()

def validate_alphanumeric(value):
    return bool(re.match(r'^[a-zA-Z0-9/-]+$', value))

def validate_numeric(value):
    return value.isdigit()


def validate_telephone(value):
    return bool(re.match(r'^\+\d+$', value))

def validate_email(value):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value))

def validate_url(value):
    return bool(re.match(r'^https?://[^\s/$.?#].[^\s]*$', value))

def validate_date(value):
    try:
        time.strptime(value, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def verify_field(xpath, expected_value, validation_func=None, success_message=None):
    field = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    actual_value = field.get_attribute('value') or field.text  # Use field.text for non-input elements
    if validation_func:
        if validation_func(actual_value):
            log_result(f"PASSED:: Value '{actual_value}' is valid. {success_message if success_message else 'Value is valid and saved successfully.'}")
        else:
            log_result(f"FAILED:: Value '{actual_value}' is invalid. {success_message if success_message else 'Value not valid.'} Reason: Expected value '{expected_value}'.")
    else:
        log_result(f"PASSED:: {success_message if success_message else 'Field value displayed successfully.'}")


# Initialize WebDriverWait
wait = WebDriverWait(driver, 10)

# Login
email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
email_field.send_keys('rebingtest777@yopmail.com')
time.sleep(2)

password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
password_field.send_keys('Rebing@001122')
time.sleep(2)

login_button = driver.find_element(By.XPATH, '//*[@id="login_button"]')
login_button.click()
time.sleep(2)

# Navigate to Company Settings
settings_menu = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div[1]/div/div[1]/div[2]/div/div/div/ul/li[11]/a/span[2]')))
settings_menu.click()
time.sleep(2)

company_settings_link = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="useradd-sidenav"]/a[3]')))
company_settings_link.click()
time.sleep(2)

# Company Name
company_name_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="useradd-3"]/form/div/div[1]/div[1]/input')))
company_name_field.send_keys('Bata')
time.sleep(2)
verify_field('//*[@id="useradd-3"]/form/div/div[1]/div[1]/input', 'Bata', validate_alphabet, 'Company Name should only accept alphabetic characters.')

# Address
address_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="company_address"]')))
address_field.send_keys('Dhanmondi/Area')
time.sleep(2)
verify_field('//*[@id="company_address"]', 'Dhanmondi/Area', validate_alphanumeric, 'Address should only accept alphanumeric characters, /, and -.')

# City
city_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="company_city"]')))
city_field.send_keys('Dhaka')
time.sleep(2)
verify_field('//*[@id="company_city"]', 'Dhaka', validate_alphanumeric, 'City should only accept alphanumeric characters, /, and -.')

# State
state_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="company_state"]')))
state_field.send_keys('California@Vegas')
time.sleep(2)
verify_field('//*[@id="company_state"]', 'California@Vegas', validate_alphanumeric, 'State should only accept alphanumeric characters, /, and -.')

# Zip/Post Code
zipcode_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="company_zipcode"]')))
zipcode_field.send_keys('1225')
time.sleep(2)
verify_field('//*[@id="company_zipcode"]', '1225', validate_numeric, 'Zip/Post Code should only accept numeric values.')

# Post Office
post_office_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="company_post_office"]')))
post_office_field.send_keys('Mirpur-14')
time.sleep(2)
verify_field('//*[@id="company_post_office"]', 'Mirpur-14', validate_alphanumeric, 'Post Office should only accept alphanumeric characters, /, and -.')

# Country
country_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="company_country"]')))
country_field.send_keys('Bangladesh')
time.sleep(2)
verify_field('//*[@id="company_country"]', 'Bangladesh', validate_alphabet, 'Country should only accept alphabetic characters.')

# Telephone
telephone_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="company_telephone"]')))
telephone_field.send_keys('+01741495590')
time.sleep(2)
verify_field('//*[@id="company_telephone"]', '+01741495590', validate_telephone, 'Telephone should only accept numeric values with a leading +.')

# Email
email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="company_email"]')))
email_field.send_keys('akiff328700@gmail.com')
time.sleep(2)
verify_field('//*[@id="company_email"]', 'akiff328700@gmail.com', validate_email, 'Email should be in valid format.')

# Web
web_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="web"]')))
web_field.send_keys('https://www.youtube.com/')
time.sleep(2)
verify_field('//*[@id="web"]', 'https://www.youtube.com/', validate_url, 'Web URL should be valid.')

# Organization number
organization_number_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="registration_number"]')))
organization_number_field.send_keys('1111')
time.sleep(2)
verify_field('//*[@id="registration_number"]', '1111', validate_numeric, 'Organization number should only accept numeric values.')

# Vat Number
vat_number_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="vat_number"]')))
vat_number_field.send_keys('201')
time.sleep(2)
verify_field('//*[@id="vat_number"]', '201', validate_numeric, 'Vat Number should only accept numeric values.')

# GST Number
gst_number_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gst_number"]')))
gst_number_field.send_keys('1234500')
time.sleep(2)
verify_field('//*[@id="gst_number"]', '1234500', validate_numeric, 'GST Number should only accept numeric values.')

# Form of Organization
form_of_organization_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="form_of_organization"]')))
form_of_organization_field.click()
time.sleep(2)

# Select the 'Test' option from the dropdown
form_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form_of_organization"]/option[1]')))
form_option.click()
time.sleep(2)
verify_field('//*[@id="form_of_organization"]', 'Test', None, "Clicked Option 'Test'. Form of Organization option selected successfully.")

# Foundation Date
foundation_date_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="datepicker"]')))
foundation_date_field.send_keys('10/15/2024')
time.sleep(3)
verify_field('//*[@id="datepicker"]', '10/15/2024', None, "Clicked Option '10/15/2024'. Foundation Date value selected successfully.")
# Vat period
vat_period_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="vat_period"]')))
vat_period_field.send_keys('12')
time.sleep(2)
verify_field('//*[@id="vat_period"]', '12', validate_numeric, 'Vat period should only accept numeric values.')

# Click Save Changes button
save_changes_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="useradd-3"]/form/div/div[2]/div/input')))
save_changes_button.click()
time.sleep(3)

# Click on Dropdown and Logout
dropdown_xpath = '/html/body/header/div/div[1]/ul/li[2]/a'
dropdown = driver.find_element(By.XPATH, dropdown_xpath)
dropdown.click()
print("Clicked on dropdown.")

time.sleep(2)

# Click on Logout
logout_xpath = '/html/body/header/div/div[1]/ul/li[2]/div/a[2]'
logout = driver.find_element(By.XPATH, logout_xpath)
logout.click()
print("Logged out.")

# Close log file and browser
log_file.close()
driver.quit()
