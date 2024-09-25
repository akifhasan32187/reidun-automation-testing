from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up WebDriver and maximize window
driver = webdriver.Chrome()
driver.maximize_window()

# Open the login page
driver.get("https://test-reidun.rebingtest.com/login")
print('<strong class="text-success">PASSED::</strong>Opened login page.')

# Enter email
email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
email_field.send_keys('rebingtest777@yopmail.com')
print('<strong class="text-success">PASSED::</strong>Entered email.')

# Enter password
password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
password_field.send_keys('Rebing@001122')
print('<strong class="text-success">PASSED::</strong>Entered password.')

# Click login button
login_button = driver.find_element(By.XPATH, '//*[@id="login_button"]')
login_button.click()
print('<strong class="text-success">PASSED::</strong>Clicked login button.')

time.sleep(2)

# Function to perform the settings actions for each iteration
def perform_settings_iteration(iteration, currency_symbol_position_xpath, amount_format_xpath, date_format_xpath, time_format_xpath,
                                currency, currency_symbol, outgoing_invoice_prefix, outgoing_invoice_starting_number,
                                incoming_invoice_prefix, incoming_invoice_starting_number, customer_prefix,
                                supplier_prefix, footer_notes):
    print(f'<strong class="text-success">PASSED::</strong>Starting iteration {iteration}...')

    # Click on Company Settings
    company_settings_xpath = '/html/body/nav/div[1]/div/div[1]/div[2]/div/div/div/ul/li[11]/a/span[2]'
    company_settings = driver.find_element(By.XPATH, company_settings_xpath)
    company_settings.click()
    print('<strong class="text-success">PASSED::</strong>Clicked on Company Settings.')

    time.sleep(1)

    # Click on System Settings
    system_settings_xpath = '//*[@id="useradd-sidenav"]/a[2]'
    system_settings = driver.find_element(By.XPATH, system_settings_xpath)
    system_settings.click()
    print('<strong class="text-success">PASSED::</strong>Clicked on System Settings.')

    time.sleep(1)

    # Click Currency Symbol Position
    currency_symbol_position_element = driver.find_element(By.XPATH, currency_symbol_position_xpath)
    currency_symbol_position_text = currency_symbol_position_element.text
    currency_symbol_position_element.click()
    print(f'<strong class="text-success">PASSED::</strong>Selected Currency Symbol Position as ')


    time.sleep(1)

    # Click Amount Format
    amount_format_2_xpath = '//*[@id="useradd-2"]/form/div[1]/div/div[2]/div/div[1]'
    amount_format_element = driver.find_element(By.XPATH, amount_format_2_xpath)
    amount_format_element.click()
    #print(f"Selected Amount Format using XPath: {amount_format_2_xpath}")

    # Click Amount Format
    #amount_format_xpath = '//*[@id="useradd-2"]/form/div[1]/div/div[2]/div/div[1]'
    amount_format_element = driver.find_element(By.XPATH, amount_format_xpath)
    amount_format_text = amount_format_element.text
    amount_format_element.click()
    print(f'<strong class="text-success">PASSED::</strong>Selected Amount Format as "{amount_format_text}"')

    time.sleep(1)

    # Enter Currency
    currency_input_xpath = '//*[@id="site_currency"]'
    currency_input = driver.find_element(By.XPATH, currency_input_xpath)
    currency_input.clear()  # Clear previous input
    currency_input.send_keys(currency)
    print(f'<strong class="text-success">PASSED::</strong>Entered Currency as "{currency}"')

    time.sleep(1)

    # Enter Currency Symbol
    currency_symbol_xpath = '//*[@id="site_currency_symbol"]'
    currency_symbol_element = driver.find_element(By.XPATH, currency_symbol_xpath)
    currency_symbol_element.clear()  # Clear previous input
    currency_symbol_element.send_keys(currency_symbol)
    print(f'<strong class="text-success">PASSED::</strong>Entered Currency Symbol as "{currency_symbol}"')

    time.sleep(1)

    # Select Date Format
    date_format_element = driver.find_element(By.XPATH, date_format_xpath)
    date_format_text = date_format_element.text
    date_format_element.click()
    print(f'<strong class="text-success">PASSED::</strong>Selected Date Format as "{date_format_text}"')

    time.sleep(1)

    # Select Time Format
    time_format_element = driver.find_element(By.XPATH, time_format_xpath)
    time_format_text = time_format_element.text
    time_format_element.click()
    print(f'<strong class="text-success">PASSED::</strong>Selected Time Format as "{time_format_text}"')

    time.sleep(1)

    # Enter Outgoing Invoice Prefix
    outgoing_invoice_prefix_xpath = '//*[@id="invoice_prefix"]'
    outgoing_invoice_prefix_element = driver.find_element(By.XPATH, outgoing_invoice_prefix_xpath)
    outgoing_invoice_prefix_element.clear()  # Clear previous input
    outgoing_invoice_prefix_element.send_keys(outgoing_invoice_prefix)
    print(f'<strong class="text-success">PASSED::</strong>Entered Outgoing Invoice Prefix as "{outgoing_invoice_prefix}"')

    time.sleep(1)

    # Enter Outgoing Invoice Starting Number
    # Assuming this is fixed or needs no interaction
    print(f'<strong class="text-success">PASSED::</strong>Outgoing Invoice Starting Number is Fixed as "{outgoing_invoice_starting_number}"')

    time.sleep(1)

    # Enter Incoming Invoice Prefix
    incoming_invoice_prefix_xpath = '//*[@id="bill_prefix"]'
    incoming_invoice_prefix_element = driver.find_element(By.XPATH, incoming_invoice_prefix_xpath)
    incoming_invoice_prefix_element.clear()  # Clear previous input
    incoming_invoice_prefix_element.send_keys(incoming_invoice_prefix)
    print(f'<strong class="text-success">PASSED::</strong>Entered Incoming Invoice Prefix as "{incoming_invoice_prefix}"')

    time.sleep(1)

    # Enter Incoming Invoice Starting Number
    # Assuming this is fixed or needs no interaction
    print(f'<strong class="text-success">PASSED::</strong>Incoming Invoice Starting Number is Fixed as "{incoming_invoice_starting_number}"')

    time.sleep(1)

    # Enter Customer Prefix
    customer_prefix_xpath = '//*[@id="customer_prefix"]'
    customer_prefix_element = driver.find_element(By.XPATH, customer_prefix_xpath)
    customer_prefix_element.clear()  # Clear previous input
    customer_prefix_element.send_keys(customer_prefix)
    print(f'<strong class="text-success">PASSED::</strong>Entered Customer Prefix as "{customer_prefix}"')

    time.sleep(1)

    # Enter Supplier Prefix
    supplier_prefix_xpath = '//*[@id="supplier_prefix"]'
    supplier_prefix_element = driver.find_element(By.XPATH, supplier_prefix_xpath)
    supplier_prefix_element.clear()  # Clear previous input
    supplier_prefix_element.send_keys(supplier_prefix)
    print(f'<strong class="text-success">PASSED::</strong>Entered Supplier Prefix as "{supplier_prefix}"')

    time.sleep(1)

    # Enter Invoice/Bill Footer Notes
    footer_notes_xpath = '//*[@id="footer_notes"]'
    footer_notes_element = driver.find_element(By.XPATH, footer_notes_xpath)
    footer_notes_element.clear()  # Clear previous input
    footer_notes_element.send_keys(footer_notes)
    print(f'<strong class="text-success">PASSED::</strong>Entered Invoice/Bill Footer Notes as "{footer_notes}"')

    time.sleep(1)

    # Scroll to the 'Save Changes' button and click it
    save_changes_xpath = '//*[@id="useradd-2"]/form/div[2]/div/input'
    save_changes = driver.find_element(By.XPATH, save_changes_xpath)
    driver.execute_script("arguments[0].scrollIntoView(true);", save_changes)
    time.sleep(2)  # Add a small delay to ensure the scroll completes
    save_changes.click()
    print('<strong class="text-success">PASSED::</strong>Clicked Save Changes.')

    time.sleep(1)

    print(f'<strong class="text-success">PASSED::</strong>Completed iteration {iteration}.')
    print('<strong class="text-success">PASSED::</strong>Waiting for 3 seconds before next iteration.')
    time.sleep(1)

# Perform 5 iterations with the specified parameters
perform_settings_iteration(1,
    '//*[@id="flexCheckDefault"]',  # Currency Symbol Position = 'Pre'
    '//*[@id="choices--amount_format-item-choice-1"]',  # Amount Format = '000 000 000,00'
    '//*[@id="site_date_format"]/option[1]',  # Date Format = '01.01.2023'
    '//*[@id="site_time_format"]/option[1]',  # Time Format = '10:30 PM'
    'Money', '$', 'ARHH##$$%%', '3141', 'ARHH##$$%%', '1234', 'Sakib', 'Rafiul70', 'Please pay'
)

perform_settings_iteration(2,
    '//*[@id="flexCheckChecked"]',  # Currency Symbol Position = 'Post'
    '//*[@id="choices--amount_format-item-choice-2"]',  # Amount Format = '00,000.00'
    '//*[@id="site_date_format"]/option[2]',  # Date Format = 'Jan 1, 2015'
    '//*[@id="site_time_format"]/option[2]',  # Time Format = '10:30 pm'
    'Dollar', '€', 'JJYY##$$%%', '4455', 'Aqqqqqq$$%%', '7896', 'John', 'Roy', 'Thanks'
)

perform_settings_iteration(3,
    '//*[@id="flexCheckDefault"]',  # Currency Symbol Position = 'Pre'
    '//*[@id="choices--amount_format-item-choice-1"]',  # Amount Format = '000 000 000,00'
    '//*[@id="site_date_format"]/option[3]',  # Date Format = 'dd-mm-yyyy'
    '//*[@id="site_time_format"]/option[3]',  # Time Format = '22:30'
    'Euro', '£', 'TTTUU**&&&&', '9254564564564', '##RRTTGG', '420', 'Saif', 'Noban', 'Thanks for paying'
)

perform_settings_iteration(4,
    '//*[@id="flexCheckChecked"]',  # Currency Symbol Position = 'Post'
    '//*[@id="choices--amount_format-item-choice-2"]',  # Amount Format = '00,000.00'
    '//*[@id="site_date_format"]/option[4]',  # Date Format = 'mm-dd-yyyy'
    '//*[@id="site_time_format"]/option[1]',  # Time Format = '10:30 PM'
    'Pound', '¥', 'TTTUU+++', '92500000564', 'RakiG', '420000000', 'Afnan', 'Dip', 'Reinnnnnnnnnnnnnndddddddddddddd'
)


print("<strong>All iterations complete.</strong>")

# Now click the dropdown to open the logout option
dropdown_xpath = '/html/body/header/div/div[1]/ul/li[2]/a'
dropdown = driver.find_element(By.XPATH, dropdown_xpath)
dropdown.click()
print('<strong class="text-success">PASSED::</strong>Clicked on the "Hi, ___ (Company Name)" dropdown.')

time.sleep(2)

# Click the logout option
logout_xpath = '/html/body/header/div/div[1]/ul/li[2]/div/a[2]'
logout = driver.find_element(By.XPATH, logout_xpath)
logout.click()
print('<strong class="text-success">PASSED::</strong>Clicked on Logout.')

# Close the browser
time.sleep(2)
driver.quit()
print('<strong class="text-success">PASSED::</strong>Closed the browser.')
