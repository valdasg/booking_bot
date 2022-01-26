import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys #for using keyboard keys


url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html/'

# os.environ['PATH'] += r;'C:/SeleniumDrivers/'
# driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path=r"C:\SeleniumDrivers\chromedriver.exe")
driver.get(url)
driver.implicitly_wait(3) # wait for browser to load, can wait less if browser is loaded. To wait .sleep() used. Sets
# wait for whole project.

##Clicking button, waiting for response and feedback in class
element = driver.find_element(By.ID, "mc-embedded-subscribe")
element.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'class_name_value')
    )
)


##filling the forms
sum1 = driver.find_element(By.ID, 'sum1')
sum2 = driver.find_element(By.ID, 'sum2')

sum1.send_keys(Keys.NUMPAD4, Keys.NUMPAD7) #=47
sum1.send_keys(10)

## Handle pop ups
try:
    no_button = driver.find_element(By.CLASS_NAME, 'no-thanks')
    no_button.click()
except:
    print('No element with this class name. Skipping....')

btn = driver.find_element(By.CSS_SELECTOR, 'button[on_click = "return_total()"]') #celectors https://www.w3schools.com/cssref/css_selectors.asp
btn.click()

#driver.close() Closes tab
#driver.quit() Close browser