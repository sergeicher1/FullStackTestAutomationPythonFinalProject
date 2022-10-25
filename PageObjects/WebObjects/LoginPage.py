# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-20 08:40
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Page Objects that are located on Login Page
# ----------------------------------------------------------------------------------------
from selenium.webdriver.common.by import By

from Utilities.CommonOps import LogMessage

# Retrieve Username from page
userName = (By.XPATH, "//div/p[@class='oxd-text oxd-text--p'][1]")
# Retrieve Password from page
password = (By.XPATH, "//div/p[@class='oxd-text oxd-text--p'][2]")

userInput = (By.XPATH, "//input[@name='username']")
passInput = (By.XPATH, "//input[@name='password']")
logBtn = (By.XPATH, "//button[@type='submit']")


class LoginPage:

    def __init__(self, driver):
        LogMessage(message="Constructor __init__ of Login Page")
        self.driver = driver

    def RetrieveUserNameData(self):
        LogMessage(message="Retrieving username data")
        userInfo = self.driver.find_element(userName[0], userName[1]).text.split(": ")[1]
        return userInfo

    def RetrievePasswordData(self):
        LogMessage(message="Retrieving password data")
        passInfo = self.driver.find_element(password[0], password[1]).text.split(": ")[1]
        return passInfo

    def GetUserInput(self):
        LogMessage(message="Locating user field")
        return self.driver.find_element(userInput[0], userInput[1])

    def GetPassInput(self):
        LogMessage(message="Locating password field")
        return self.driver.find_element(passInput[0], passInput[1])

    def GetLogBtn(self):
        LogMessage(message="Locating Login button")
        return self.driver.find_element(logBtn[0], logBtn[1])
