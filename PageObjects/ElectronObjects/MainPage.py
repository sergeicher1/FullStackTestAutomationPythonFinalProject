# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-23 12:55
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Electron my app Main page objects
# ----------------------------------------------------------------------------------------


from selenium.webdriver.common.by import By

from Utilities.CommonOps import LogMessage

header = (By.XPATH, "/html/body/h1")
labelCel = (By.XPATH, "//label[text()='Celsius:']")
inputCel = (By.XPATH, "//input[@id='celcius']")
labelFahr = (By.XPATH, "//label[text()='Fahrengeit:']")
inputFahr = (By.XPATH, "//input[@id='fahrenheit']")


class MainPage:

    def __init__(self, driver):
        LogMessage(message="Constructor __init__ of Main page")
        self.driver = driver

    def GetHeader(self):
        LogMessage(message="Locating header")
        return self.driver.find_element(header[0], header[1])

    def GetLabelCel(self):
        LogMessage(message="Locating label Celsius")
        return self.driver.find_element(labelCel[0], labelCel[1])

    def GetInputCel(self):
        LogMessage(message="Locating input celsius")
        return self.driver.find_element(inputCel[0], inputCel[1])

    def GetlLabelFahr(self):
        LogMessage(message="Locating label fahrenheit")
        return self.driver.find_element(labelFahr[0], labelFahr[1])

    def GetInputFahr(self):
        LogMessage(message="Locating input fahrenheit")
        return self.driver.find_element(inputFahr[0], inputFahr[1])
