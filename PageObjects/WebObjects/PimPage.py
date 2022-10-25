# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-20 13:45
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Page Objects that are located on PIM Page
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By

from Utilities.CommonOps import LogMessage

title = (By.XPATH, "//h6")
configuration = (By.XPATH, "//span[text()='Configuration ']")
employeeList = (By.XPATH, "//a[text()='Employee List']")
addEmployee = (By.XPATH, "//a[text()='Add Employee']")
resetButton = (By.XPATH, "//button[text()=' Reset ']")
searchButton = (By.XPATH, "//button[text()=' Search ']")
addButton = (By.XPATH, "//button[text()=' Add ']")
resultsFound = (By.XPATH, "//div/span[@class='oxd-text oxd-text--span']")
employeeName = (By.XPATH, "//input[@placeholder='Type for hints...']")
employeeID = (By.XPATH, "//div/input[@class='oxd-input oxd-input--active']")
trashDelete = (By.XPATH, "//div/button/i[@class='oxd-icon bi-trash']")
trashConfirmDel = (By.XPATH, "//button[text()=' Yes, Delete ']")


class PimPage:

    def __init__(self, driver):
        LogMessage(message="Constructor __init__ of PIM Page")
        self.driver = driver

    def GetHeader(self):
        LogMessage(message="Locating and reading header of the PIM Page")
        header = self.driver.find_element(title[0], title[1]).text
        return header

    def GetConfigurationButton(self):
        LogMessage(message="Locating configuration element")
        return self.driver.find_element(configuration[0], configuration[1])

    def GetEmployeeList(self):
        LogMessage(message="Locating employee list element")
        return self.driver.find_element(employeeList[0], employeeList[1])

    def GetAddEmployee(self):
        LogMessage(message="Locating add employee element")
        return self.driver.find_element(addEmployee[0], addEmployee[1])

    def GetResetBtn(self):
        LogMessage(message="Locating reset button")
        return self.driver.find_element(resetButton[0], resetButton[1])

    def GetSearchBtn(self):
        LogMessage(message="Locating search button")
        return self.driver.find_element(searchButton[0], searchButton[1])

    def GetAddBtn(self):
        LogMessage(message="Locating add button")
        return self.driver.find_element(addButton[0], addButton[1])

    def GetResultsFound(self):
        LogMessage(message="Locating results found element")
        return self.driver.find_element(resultsFound[0], resultsFound[1])

    def GetEmployeeName(self):
        LogMessage(message="Locating employee name for search")
        return self.driver.find_element(employeeName[0], employeeName[1])

    def GetTrashDelete(self):
        LogMessage(message="Locating trash for delete")
        return self.driver.find_element(trashDelete[0], trashDelete[1])

    def GetConfirmDelete(self):
        LogMessage(message="Locating confirm delete button")
        return self.driver.find_element(trashConfirmDel[0], trashConfirmDel[1])

    def GetEmployeeID(self):
        LogMessage(message="Locating Employee ID field")
        return self.driver.find_element(employeeID[0], employeeID[1])
