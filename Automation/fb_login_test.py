"""
#Written by Rahul Krishnan @rahulkrishnan221
This script will test Facebook's lofin without landing into the captcha verification
This script is just for education purposes.
"""
import unittest
from selenium import webdriver
from  selenium.webdriver.support.ui import WebDriverWait

class FBlogintest(unittest.TestCase):
    #Add the location of geekodriver.exe
    def setUp(self):
        self.driver=webdriver.Firefox(executable_path="C:\\geckodriver")
        self.driver.get("http://www.facebook.com")

    def test_login(self):
        #Add the Email ID and the Password
        driver=self.driver
        facebookUsername ="replace and Put your emailId i.e fb id"
        facebookPassword="replace and Put your fb pass"

        emailFieldID='email'
        passFieldID='pass'
        loginButtonXpath='//input[@value="Log In"]'
        fbLogoXpath = '(//a[contains(@href,"logo")[1]'

        #Giving a delay of 10 seconds

        emailFieldElement = WebDriverWait(driver,10).until(lambda  driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver,10).until(lambda  driver: driver.find_element_by_id(passFieldID))
        loginButtonElement=WebDriverWait(driver,10).until(lambda  driver: driver.find_element_by_xpath(loginButtonXpath))
        emailFieldElement.clear()
        #Sending the credentials
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        loginButtonElement.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))

    def tearDown(self):
        self.driver.quit()

        #init

if __name__=="__main__":
        unittest.main()
