from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Correct import for Chrome

# Use ChromeDriverManager to automatically manage the driver
service = Service(ChromeDriverManager().install())

# Initialize Chrome WebDriver
browser = webdriver.Chrome(service=service)

# Open Google
browser.get("https://www.google.com")

# Print the page title to confirm Selenium is working
print("Page Title:", browser.title)

# Close the browser after a few seconds
import time
time.sleep(5)
browser.quit()
