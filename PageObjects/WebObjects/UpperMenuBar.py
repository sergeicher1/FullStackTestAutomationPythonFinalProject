# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-21 11:15
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Page Objects that are located on Upper Navigation Bar
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By
from Utilities.CommonOps import LogMessage

dropDown = (By.XPATH, "//li/span[@class='oxd-userdropdown-tab']")
listDropdown = (By.XPATH, "//ul[@class='oxd-dropdown-menu']/li")
about = (By.XPATH, "//ul[@class='oxd-dropdown-menu']/li[1]")
support = (By.XPATH, "//ul[@class='oxd-dropdown-menu']/li[2]")
changePassword = (By.XPATH, "//ul[@class='oxd-dropdown-menu']/li[3]")
logout = (By.XPATH, "//ul[@class='oxd-dropdown-menu']/li[4]")


class UpperMenuBar:

    def __init__(self, driver):
        LogMessage(message="Constructor __init__ of UpperMenu")
        self.driver = driver

    def GetDropDown(self):
        LogMessage(message="Locating dropdown menu")
        return self.driver.find_element(dropDown[0], dropDown[1])

    def GetDropDownElements(self):
        LogMessage(message="Locating dropdown elements")
        return self.driver.find_elements(listDropdown[0], listDropdown[1])

    def GetAbout(self):
        LogMessage(message="Locating about element")
        return self.driver.find_element(about[0], about[1])

    def GetSupport(self):
        LogMessage(message="Locating support element")
        return self.driver.find_element(support[0], support[1])

    def GetChangePass(self):
        LogMessage(message="Locating change password element")
        return self.driver.find_element(changePassword[0], changePassword[1])

    def GetLogout(self):
        LogMessage(message="Locating logout element")
        return self.driver.find_element(logout[0], logout[1])
