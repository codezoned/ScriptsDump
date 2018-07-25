import unittest
from selenium import webdriver
from  selenium.webdriver.support.ui import WebDriverWait
#author rahul
#It test the fb login without getting landed to captcha verification
class FBlogintest(unittest.TestCase):
    #ADD the location of geekodriver.exe
    def setUp(self):
        self.driver=webdriver.Firefox(executable_path="C:\\geckodriver")
        self.driver.get("http://www.facebook.com")

    def test_login(self):
        #add the email and pass
        driver=self.driver
        facebookUsername ="replace and Put your emailId i.e fb id"
        facebookPassword="replace and Put your fb pass"

        emailFieldID='email'
        passFieldID='pass'
        loginButtonXpath='//input[@value="Log In"]'
        fbLogoXpath = '(//a[contains(@href,"logo")[1]'

        emailFieldElement = WebDriverWait(driver,10).until(lambda  driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver,10).until(lambda  driver: driver.find_element_by_id(passFieldID))
        loginButtonElement=WebDriverWait(driver,10).until(lambda  driver: driver.find_element_by_xpath(loginButtonXpath))
        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        loginButtonElement.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
        unittest.main()
