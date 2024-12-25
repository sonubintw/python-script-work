from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

try:
    # Open the website
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.in/")
    # Wait for the page to load
    time.sleep(5)  # Adjust this based on your website's loading time

    # Locate the button (update selector as needed)
    button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/a[1]")  # Replace 'button-id' with the actual ID or use other selectors

    # Click the button
    button.click()

    print("Button clicked successfully!")

    # Optional: Wait before closing the browser
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()

