from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# your path
path = r"/chromedriver"
twitter_login = 'https://twitter.com'

#user name and password
user_name = ''
password = ''

driver = webdriver.Chrome(path)


driver.get(twitter_login)

# when there are spaces in class name, just remove them and put . in between
user_box = driver.find_element_by_css_selector('input.text-input.email-input.js-signin-email')
password_box = driver.find_element_by_css_selector('input[type=password]')

password_box.send_keys(password)
user_box.send_keys(user_name)

password_box.send_keys(Keys.ENTER)


