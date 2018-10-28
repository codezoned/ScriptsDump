url="https://www.linkedin.com"

from selenium import webdriver
browser=webdriver.Chrome()

browser.get(url)

browser.maximize_window()#Maximizing the window

username=browser.find_element_by_id("login-email")
username.send_keys(input("Enter The Email of your LinkedIn Account"))#Enter the email of your linkedin account in the prompt


input_pass=browser.find_element_by_id("login-password")
from getpass import getpass
password=getpass("Enter the password")
input_pass.send_keys(password)#enter the password in the prompt


from selenium.webdriver.common.keys import Keys
input_pass.send_keys(Keys.ENTER)

browser.find_element_by_id('mynetwork-tab-icon').click()
cnt=0
import time
import random
for i in range(100): #Enter the number of times to reload the network-page
    if i!=0:
        browser.refresh()
    time.sleep(3)
    connections=browser.find_elements_by_class_name('artdeco-button__text')
    for i in connections:
        if i.is_displayed():
            time.sleep(random.randint(2,3))
            i.click()
            cnt+=1
            print(cnt) #Prints done for each connection made
    
    
browser.close()