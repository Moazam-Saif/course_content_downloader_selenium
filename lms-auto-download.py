from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time  # Import time for adding delays
from selenium.webdriver.common.by import By

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()  # Ensure the WebDriver is in PATH or provide the full path

# Open the page
driver.get("https://lms.nust.edu.pk/portal/course/view.php?id=55621")

# Locate the username input field and enter the username
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("msaif.bese23seecs")  # Replace 'your_username' with your actual username

# Locate the password input field and enter the password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("Seecs@27")  # Replace 'your_password' with your actual password

# Locate the login button and click it
login_button = driver.find_element(By.ID, "loginbtn")
login_button.click()

# Print the page title after login
print("Page title after login:", driver.title)

time.sleep(2)

# Find all <a> tags with the class "aalink"
aalink_elements = driver.find_elements(By.CLASS_NAME, "aalink")

# Create a list of the href attributes of these <a> tags
aalink_urls = [element.get_attribute("href") for element in aalink_elements]

# Print the list of URLs
print("Number of 'aalink' URLs:", len(aalink_urls))
for aalink_url in aalink_urls:
    driver.get(aalink_url)

# Close the browser
driver.quit()