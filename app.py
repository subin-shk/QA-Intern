from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Use GeckoDriverManager to automatically manage the driver
service = Service(GeckoDriverManager().install())

# Initialize Firefox WebDriver
browser = webdriver.Firefox(service=service)

# Open Google
browser.get("https://www.google.com")

# Print the page title to confirm Selenium is working
print("Page Title:", browser.title)

# Close the browser after a few seconds
import time
time.sleep(5)
browser.quit()
