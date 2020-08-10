"""
This program allows to you to wish your FB friends automatically. You can create .exe file of this program
and set up a task in task manager to execute it everyday.

This is basic program where we are hard-coding the user name and password.

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome("C:/Python/Scripts/chromedriver.exe")
browser.maximize_window()
# open facebook.com
browser.get('https://www.facebook.com/')

# Here enter your FB account username
username = "****enter your facebook username here****"

# Here enter your FB account username
password = "***enter your facebook password***"

print("Let's Begin")

element = browser.find_elements_by_xpath('//*[@id ="email"]')
element[0].send_keys(username)

print("You have entered the username")

element = browser.find_element_by_xpath('//*[@id ="pass"]')
element.send_keys(password)

print("You have entered the password")

# logging in
log_in = browser.find_elements_by_id('loginbutton')
log_in[0].click()

print("Login is Successful")

browser.get('https://www.facebook.com/events/birthdays/')

feed = 'Wish you Happy Birthday....'

element = browser.find_elements_by_xpath("//*[@class ='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")
#print(element)
count = 0

for el in element:
    count += 1
    element_id = str(el.get_attribute('id'))
    XPATH = '//*[@id ="' + element_id + '"]'
    fb_post_field = browser.find_element_by_xpath(XPATH)
    fb_post_field.send_keys(feed)
    fb_post_field.send_keys(Keys.RETURN)
    print("Total wishes: " + str(cnt))

# Close the browser
browser.close()