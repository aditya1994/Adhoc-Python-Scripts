from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace below path with the absolute path
# to chromedriver in your computer
#Put the chromedriver in the same folder as of the chrome application

driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver")

driver.get("http://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)
print('whatsapp web opened')


# Replace the below string with your own message
string = "Message from Python!"

#Replace Friend in "title" with your Friend's name
group_title = wait.until( EC.presence_of_element_located((By.XPATH, '//*[@title="Friend"]')))
if group_title:
    print('Title got from the page')
group_title.click()
inp_xpath = '//div[@class="input-container"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, '//div[@class="pluggable-input-body copyable-text selectable-text"][@dir="auto"]')))

if input_box:
    print('input box found on the page')
input_box.click()
for i in range(10):
    print (i, 'th Message sent')
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)



# #https://www.github.com/iamnosa
# #Let's import the Selenium package
# from selenium import webdriver
# import time
# #Let's use Firefox as our browser
# web = webdriver.Firefox()
# web.get('http://web.whatsapp.com')
# time.sleep(20)

# #Replace Mr Kelvin with the name of your friend to spam
# elem = web.find_element_by_xpath('//span[contains(text(),"Shef")]')
# elem.click()
# elem1 = web.find_elements_by_class_name('input')
# for i in range(0,10):
#     elem1[1].send_keys('I love you :D')
#     i=+1
# web.find_element_by_class_name('send-container').click()