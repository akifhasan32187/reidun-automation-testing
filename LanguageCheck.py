from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from spellchecker import SpellChecker
import time

# Set up WebDriver without headless mode to view the browser window
chrome_options = Options()

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Initialize SpellChecker
spell = SpellChecker()

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

time.sleep(1)

# Navigate to Company Settings
company_settings_xpath = '/html/body/nav/div[1]/div/div[1]/div[2]/div/div/div/ul/li[11]/a/span[2]'
company_settings = driver.find_element(By.XPATH, company_settings_xpath)
company_settings.click()
print('<strong class="text-success">PASSED::</strong>Clicked on Company Settings.')

time.sleep(1)

# Click the dropdown toggle menu at the right top of the page
dropdown_menu_xpath = '/html/body/header/div/div[2]/ul/li/a'
dropdown_menu = driver.find_element(By.XPATH, dropdown_menu_xpath)
dropdown_menu.click()
print('<strong class="text-success">PASSED::</strong>Clicked on the dropdown menu.')

time.sleep(1)

# Click on the Norwegian option
norwegian_option_xpath = '/html/body/header/div/div[2]/ul/li/div/a[2]'
norwegian_option = driver.find_element(By.XPATH, norwegian_option_xpath)
norwegian_option.click()
print('<strong class="text-success">PASSED::</strong>Switched to Norwegian language.')

time.sleep(1)

# Extract all visible text from the page
page_text = driver.find_element(By.TAG_NAME, "body").text

# Split the text into individual words
words = page_text.split()

# Lists to store correct and incorrect words
correct_words = []
incorrect_words = []

# File to store the results
with open("spellcheck_results_norwegian.txt", "w") as file:
    # Check each word for spelling correctness (but reverse the logic)
    for word in words:
        # Remove any punctuation and make the word lowercase
        clean_word = ''.join(e for e in word if e.isalnum()).lower()
        if not clean_word:  # Skip empty strings
            continue

        # Check if the word is numeric (if so, it's always correct)
        if clean_word.isdigit():
            result = f'<strong class="text-success">Correct(Number)::</strong>{word}'
            correct_words.append(word)
        # Reverse logic: mark correct words as incorrect and incorrect words as correct
        elif clean_word not in spell:
            result = f'<strong class="text-success">Correct::</strong>{word}'
            correct_words.append(word)
        else:
            result = f'<strong class="text-danger">Incorrect::</strong>{word}'
            incorrect_words.append(word)

        # Print and write the result to the file
        print(result)
        file.write(result + "\n")

# Print total counts of correct and incorrect words
total_correct = len(correct_words)
total_incorrect = len(incorrect_words)

print(f'<strong class="text-success">Total Correct Words::</strong><strong>{total_correct}</strong>')
print(f'<strong class="text-danger">Total Incorrect Words::</strong><strong>{total_incorrect}</strong>')

# Print lists of correct and incorrect words
print('<strong class="text-success">Correct Words::</strong>')
print(", ".join(correct_words))

print('<strong class="text-danger">Incorrect Words::</strong>')
print(", ".join(incorrect_words))

# Write the summary to the file
with open("spellcheck_summary.txt", "w") as summary_file:
    summary_file.write(f"Total Correct Words: {total_correct}\n")
    summary_file.write(f"Total Incorrect Words: {total_incorrect}\n")
    summary_file.write("\nCorrect Words:\n")
    summary_file.write(", ".join(correct_words) + "\n")
    summary_file.write("\nIncorrect Words:\n")
    summary_file.write(", ".join(incorrect_words) + "\n")

# Close the browser
driver.quit()
print('<strong class="text-success">PASSED::</strong>Finished spell-checking in Norwegian and saved results to "spellcheck_results_norwegian.txt" and "spellcheck_summary.txt".')
