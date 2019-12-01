from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


# your path to ChromeDriver
path = r"/Path/chromedriver"

# your user name and password
user_name = ''
password = ''

# initializing webdriver
driver = webdriver.Chrome(path)

def spam(target_id, text, n):
    messenger_login = 'https://www.messenger.com/t/' + target_id
    driver.get(messenger_login)

    # when there are spaces in class name, just remove them and put . in between
    user_box = driver.find_element_by_css_selector('input.inputtext._55r1._43di')
    password_box = driver.find_element_by_css_selector('input[type=password]')

    # sending user name and password to the boxes
    password_box.send_keys(password)
    user_box.send_keys(user_name)

    #hitting enter to login
    password_box.send_keys(Keys.ENTER)

    driver.find_element_by_xpath("//*[@data-editor]").click()
    actions = ActionChains(driver)
    actions.perform()

    for i in range(n):
        actions.send_keys(text)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(0.5)

# now it's time to spam'em    
spam('your target_id', 'Spamming you', 20)
