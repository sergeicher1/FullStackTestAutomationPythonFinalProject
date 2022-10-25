# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-20 13:45
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Page Objects that are located on PIM (Add Employee) Page
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

from Utilities.CommonOps import LogMessage

firstName = (By.XPATH, "//input[@name='firstName']")
middleName = (By.XPATH, "//input[@name='middleName']")
lastName = (By.XPATH, "//input[@name='lastName']")
cancelBtn = (By.XPATH, "//button[text()=' Cancel ']")
saveBtn = (By.XPATH, "//button[text()=' Save ']")
ID = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input")


class PimAddEmployeePage:

    def __init__(self, driver):
        LogMessage(message="Constructor __init__ of PIM add employee Page")
        self.driver = driver

    def GetFirstName(self):
        LogMessage(message="Locating first name field")
        return self.driver.find_element(firstName[0], firstName[1])

    def GetMiddleName(self):
        LogMessage(message="Locating middle name field")
        return self.driver.find_element(middleName[0], middleName[1])

    def GetLastName(self):
        LogMessage(message="Locating last name field")
        return self.driver.find_element(lastName[0], lastName[1])

    def GetCancelBtn(self):
        LogMessage(message="Locating cancel button")
        return self.driver.find_element(cancelBtn[0], cancelBtn[1])

    def GetSaveBtn(self):
        LogMessage(message="Locating save button")
        return self.driver.find_element(saveBtn[0], saveBtn[1])

    def GetID(self):
        LogMessage(message="Locating id")
        return self.driver.find_element(ID[0], ID[1])
