import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up the custom download directory
download_dir = "D:/CourseFiles/Prob&Stats"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Configure Chrome options
chrome_options = Options()
prefs = {
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open the page
driver.get("https://lms.nust.edu.pk/portal/course/view.php?id=55621")

# Log in
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("msaif.bese23seecs")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("Seecs@27")
login_button = driver.find_element(By.ID, "loginbtn")
login_button.click()

# Wait for the page to load
time.sleep(2)

aalink_elements = driver.find_elements(By.CLASS_NAME, "aalink")

# Create a dictionary where the instance name is the key and the href is the value
aalink_urls = {}
for element in aalink_elements:
    href = element.get_attribute("href")  # Get the href attribute
    span = element.find_element(By.CLASS_NAME, "instancename")  # Find the <span> with class "instancename"
    instance_name = span.text.strip()  # Get the text of the <span> and strip any extra whitespace
    aalink_urls[instance_name] = href  # Add to the dictionary


# Convert Selenium cookies to a dictionary for requests
selenium_cookies = driver.get_cookies()
cookies = {cookie['name']: cookie['value'] for cookie in selenium_cookies}

# Use requests to download the files
for instance_name, url in aalink_urls.items():
    print(f"Downloading: {instance_name} from {url}")
    response = requests.get(url, cookies=cookies)  # Pass cookies for authentication

    # Check if the server provides the file name in the Content-Disposition header
    content_disposition = response.headers.get("Content-Disposition")
    if content_disposition and "filename=" in content_disposition:
        # Extract the file name from the Content-Disposition header
        filename = content_disposition.split("filename=")[-1].strip('"')
    else:
        # Fallback: Use the instance name with a generic extension
        filename = f"{instance_name}.file"

    # Construct the full file path
    file_path = os.path.join(download_dir, filename)
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"Downloaded: {file_path}")

# Close the browser
driver.quit()