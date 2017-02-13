from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://www.google.se')
time.sleep(3)

# This method is broken in Chrome
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get('http://twitter.com')
time.sleep(3)

driver.execute_script("window.open('');")  # Opens a new tab using JavaScript, does not swap focus to it.
driver.get("http://stackoverflow.com")
driver.close()  # Close the active window, does not set a new active window.
driver.switch_to.window(driver.window_handles[0])  # Select a window from the window handler
driver.get("http://google.se")
driver.close()  # Close the last tab and the browser as it's the last one.
