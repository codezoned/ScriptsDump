import os
import unittest
from appium import webdriver
from time import sleep
from robot.api.deco import keyword
from robot.api import logger
 

"""
Android UI automation script using Appium
This unit test runs the specified UI actions on the specified device
Most of the user actions are defined over here
""" 

class ExoPlayerTests(unittest.TestCase):
    "Class to run tests against the Exo Player App"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1.0'
        desired_caps['deviceName'] = 'Pixel'
        desired_caps['automationName'] = 'uiautomator2'
        # desired_caps['app'] = 'location_path.apk'
        desired_caps['appPackage'] = 'com.android.fun'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        #clears the logs in the terminal - include if necessary
        os.system("adb logcat -b all -c")
        
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
        os.system("adb logcat -d  | grep 'HttpSend:' > log.txt")
        print 'Inside tear down.'
        os.system("cat log.txt")
 
    def test_single_instance_mode(self):
        "Test the app launches correctly and video plays"
        allow_button = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        allow_button.click()
        print "allow button clicked"
        sleep(2)
        allow_button.click()
        print "allow button clicked"
        sleep(5)
        #choose_single = self.driver.find_element_by_id("com.android.akamai.sampleexoplayer:id/singleInstance")
        #choose_single = self.driver.findElement(By.xpath('//android.widget.ImageButton[@content-desc="Single Instance"]'))
        choose_single = self.driver.find_element_by_accessibility_id('Single Instance')
        choose_single.click()
        print "chose single mode"
        sleep(5)
        done = self.driver.find_element_by_id("com.android.akamai.sampleexoplayer:id/done")
        done.click()
        print "settings chosen"
        sleep(2)
        choose_video = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]")
        choose_video.click()
        print "chose video to play"
        sleep(20)
        video_press = self.driver.find_element_by_id("com.android.akamai.sampleexoplayer:id/exo_subtitles")
        video_press.click()
        pause_button = self.driver.find_element_by_accessibility_id('Pause')
        pause_button.click()
        print "paused video"
        sleep(5)
        play_button = self.driver.find_element_by_accessibility_id('Play')
        play_button.click()
        print "Start playing again"
        sleep(15)
        video_press.click()
        forward_button = self.driver.find_element_by_accessibility_id('Fast forward')
        forward_button.click()
        forward_button.click()
        print "Fast Forward Performed"
        sleep(15)
        video_press.click()
        rewind_button = self.driver.find_element_by_accessibility_id('Rewind')
        rewind_button.click()
        print "Rewind Performed"
        sleep(10)
        print "Locking the device for 2s"
        self.driver.lock(2)
        sleep(1)
        self.driver.back()
        print "pressed back button"
        sleep(10)
        choose_video.click()
        print "chose video to play"
        sleep(20)
        self.driver.press_keycode(3)
        print "pressing Home"
        sleep(10)
        print "app will close now"

        
 
#---START OF SCRIPT
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(ExoPlayerTests)
#     unittest.TextTestRunner(verbosity=2).run(suite)


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1'
desired_caps['deviceName'] = 'Pixel'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['app'] = 'Location.apk'
desired_caps['appPackage'] = 'com.android.fun'
desired_caps['appActivity'] = '.MainActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

