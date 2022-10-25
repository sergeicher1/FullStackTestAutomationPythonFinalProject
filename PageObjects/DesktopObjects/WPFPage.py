# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-24 13:08
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : WPF page objects
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

from Utilities.CommonOps import LogMessage

checkBox = (By.CLASS_NAME, "CheckBox")
textBox = (By.CLASS_NAME, "TextBox")
radioBtn = (By.CLASS_NAME, "RadioButton")
buttonToCLick = (By.CLASS_NAME, "Button")


class WPFPage:

    def __init__(self, driver):
        LogMessage(message="Constructor __init__ of WPF page")
        self.driver = driver

    def GetCheckBox(self):
        LogMessage(message="Locating check box element")
        return self.driver.find_element(checkBox[0], checkBox[1])

    def GetTextBox(self):
        LogMessage(message="Locating text box element")
        return self.driver.find_element(textBox[0], textBox[1])

    def GetRadioButton(self):
        LogMessage(message="Locating radio button")
        return self.driver.find_element(radioBtn[0], radioBtn[1])

    def GetButton(self):
        LogMessage(message="Locating the button")
        return self.driver.find_element(buttonToCLick[0], buttonToCLick[1])

