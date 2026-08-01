from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and Configure the chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the (fake) newsletter registration page
driver.get("https://app_brewery.github.io/fake-newsletter-signup/")

# find the first name, last name, and email fields
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# Fill Out this form
first_name.send_keys("Pradeep")
last_name.send_keys("BC")
email.send_keys("angel@email.com")