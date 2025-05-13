from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time  # Import time for adding delays
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


username=input("Enter your username:")
password=input("Enter your password:")
# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()  # Ensure the WebDriver is in PATH or provide the full path

# Open the page
driver.get("https://lms.nust.edu.pk/portal/login/index.php")


# Locate the username input field and enter the username
username_field = driver.find_element(By.ID, "username")
username_field.send_keys(username)  # Replace 'your_username' with your actual username

# Locate the password input field and enter the password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)  # Replace 'your_password' with your actual password

# Locate the login button and click it
login_button = driver.find_element(By.ID, "loginbtn")
login_button.click()

# Print the page title after login
print("Page title after login:", driver.title)

# Wait for the course elements to load
course_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.aalink.coursename"))
)

# Create a dictionary to associate course names with their links
course_links = {}
for element in course_elements:
    # Get the href attribute of the <a> tag
    href = element.get_attribute("href")
    
    course_name = element.text.strip()  # Get the text of the <span> and strip any extra whitespace
    print(course_name+"1")
    
    # Add the course name and link to the dictionary
    course_links[course_name] = href
    print(href)

# Prompt the user to enter the name of the course
course_input = input("Enter the name of the course: ").strip().lower()

# Function to calculate a similarity score
def similarity_score(input_text, course_name):
    input_words = set(input_text.split())
    course_words = set(course_name.lower().split())
    matching_words = input_words & course_words
    score = len(matching_words) / max(len(input_words), len(course_words))  # Normalize by the larger set
    print(f"Matching '{input_text}' with '{course_name}'")
    print(f"Input Words: {input_words}, Course Words: {course_words}, Matching Words: {matching_words}, Score: {score}")
    return score

# Find the best match based on word overlap
# Find the best match based on similarity score
best_match = None
best_score = 0.0
for course_name, href in course_links.items():
    score = similarity_score(course_input, course_name)
    if score > best_score:
        best_match = href
        best_score = score

# Click the link for the best match
if best_match:
    driver.get(best_match)  # Navigate to the link
else:
    print("No matching course found.")
    

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