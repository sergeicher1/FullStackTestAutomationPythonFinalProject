# --------------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-20 10:48
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : WEB flows (dirty work) of test cases
# --------------------------------------------------------------------------------------------

from time import sleep

import allure

from Extensions.UiActions import UiActions
from Extensions.Verifications import Verifications
from PageObjects.WebObjects import PimPage
from Utilities import ManagePages
from Utilities.CommonOps import *

# list of data for data driven testing, will be used in test_Web.filtering
data = ReadCsv(GetData("CSVLocation"))
testData = [
    (data[0][0], data[0][1]),
    (data[1][0], data[1][1]),
    (data[2][0], data[2][1]),
    (data[3][0], data[3][1])
]


# Web Business flows
class WebFlows:
    testData = None

    @staticmethod
    @allure.step("Login flow")
    # If not entered, will retrieve from login page
    def LoginFlow(userName="", password=""):
        if not userName and not password:
            userName = ManagePages.loginPage.RetrieveUserNameData()
            password = ManagePages.loginPage.RetrievePasswordData()
        LogMessage(message=f"Logging in with username: {userName} and password: {password}")
        UiActions.UpdateText(ManagePages.loginPage.GetUserInput(), userName)
        UiActions.UpdateText(ManagePages.loginPage.GetPassInput(), password)
        UiActions.Click(ManagePages.loginPage.GetLogBtn())

    @staticmethod
    @allure.step("Verify title after Login")
    def VerifyTitle(expected: str):
        # wait for element, otherwise can fail test
        Wait(For.elementExists, PimPage.title)
        actual = ManagePages.pimPage.GetHeader()
        LogMessage(message=f"Verifying title after Login actual: {actual} and expected: {expected}")
        Verifications.VerifyEquals(actual, expected)

    @staticmethod
    @allure.step("Very elements on left menu bar")
    def VerifyElementsLeftMenuBar():
        LogMessage(message="Verifying elements on left menu bar")
        for el in ManagePages.leftMenuBar.GetListAmount():
            print(el.text)
            LogMessage(message=f"element: {el.text}")
        elems = [
            ManagePages.leftMenuBar.GetImageBanner(),
            ManagePages.leftMenuBar.GetSearch(),
            ManagePages.leftMenuBar.GetAdmin(),
            ManagePages.leftMenuBar.GetPim(),
            ManagePages.leftMenuBar.GetLeave(),
            ManagePages.leftMenuBar.GetTime(),
            ManagePages.leftMenuBar.GetRecruitment(),
            ManagePages.leftMenuBar.GetMyInfo(),
            ManagePages.leftMenuBar.GetPerformance(),
            ManagePages.leftMenuBar.GetDashboard(),
            ManagePages.leftMenuBar.GetDirectory(),
            ManagePages.leftMenuBar.GetMaintenance(),
            ManagePages.leftMenuBar.GetBuzz()
        ]
        Verifications.SmartAssert(elems)

    @staticmethod
    @allure.step("Verify elements on upper menu dropdown")
    def VerifyElementsUpperMenuDropdown():
        LogMessage(message="Verifying elements on upper menu bar")
        UiActions.Click(ManagePages.upperMenuBar.GetDropDown())
        for el in ManagePages.upperMenuBar.GetDropDownElements():
            print(el.text)
            LogMessage(message=f"element: {el.text}")
        elems = [
            ManagePages.upperMenuBar.GetAbout(),
            ManagePages.upperMenuBar.GetSupport(),
            ManagePages.upperMenuBar.GetChangePass(),
            ManagePages.upperMenuBar.GetLogout()
        ]
        Verifications.SmartAssert(elems)

    @staticmethod
    @allure.step("Add and verify new employee flow")
    def CreateAndVerifyNewEmployeeFlow(value1: str, value2: str, ID: str):
        ID += str(int(ID) + 1)
        storeRecordsFound = ManagePages.pimPage.GetResultsFound().text.split("(")[1].split(")")[0]
        LogMessage(message=f"records found before adding: {storeRecordsFound}")
        UiActions.Click(ManagePages.pimPage.GetAddBtn())
        UiActions.UpdateText(ManagePages.pipAddEmployeePage.GetFirstName(), value1)
        UiActions.UpdateText(ManagePages.pipAddEmployeePage.GetLastName(), value2)
        UiActions.Clear(ManagePages.pipAddEmployeePage.GetID())
        UiActions.UpdateText(ManagePages.pipAddEmployeePage.GetID(), ID)
        sleep(0.5)
        UiActions.Click(ManagePages.pipAddEmployeePage.GetSaveBtn())
        UiActions.Click(ManagePages.pimPage.GetEmployeeList())
        newRecordsFound = ManagePages.pimPage.GetResultsFound().text.split("(")[1].split(")")[0]
        LogMessage(message=f"records found after adding: {newRecordsFound}")
        Verifications.VerifyEquals(int(storeRecordsFound) + 1, int(newRecordsFound))

    @staticmethod
    @allure.step("Search filtering")
    def SearchEmployeeFlow(searchValue: str):
        LogMessage(message=f"Searching for: {searchValue}")
        UiActions.Clear(ManagePages.pimPage.GetEmployeeName())
        UiActions.UpdateText(ManagePages.pimPage.GetEmployeeName(), searchValue)
        UiActions.Click(ManagePages.pimPage.GetSearchBtn())

    @staticmethod
    @allure.step("Delete employee by ID")
    def DeleteByID(ID: str):
        LogMessage(message="Deleting by ID")
        UiActions.Click(ManagePages.pimPage.GetEmployeeList())
        storeRecordsFound = ManagePages.pimPage.GetResultsFound().text.split("(")[1].split(")")[0]
        LogMessage(message=f"records found before adding: {storeRecordsFound}")
        UiActions.Click(ManagePages.leftMenuBar.GetCollapse())
        UiActions.UpdateText(ManagePages.pimPage.GetEmployeeID(), ID)
        sleep(1)
        UiActions.Click(ManagePages.pimPage.GetSearchBtn())
        newRecordsFound = ManagePages.pimPage.GetResultsFound().text.split("(")[1].split(")")[0]
        Verifications.VerifyEquals(1, int(newRecordsFound))
        sleep(1)
        UiActions.Click(ManagePages.pimPage.GetTrashDelete())
        UiActions.Click(ManagePages.pimPage.GetConfirmDelete())
        UiActions.Click(ManagePages.pimPage.GetEmployeeList())
        sleep(1)
        newRecordsFound = ManagePages.pimPage.GetResultsFound().text.split("(")[1].split(")")[0]
        Verifications.VerifyEquals(int(storeRecordsFound) - 1, int(newRecordsFound))

    @staticmethod
    @allure.step("Expand left sidebar")
    def ExpandLeftSidebar():
        LogMessage(message="Expanding left sidebar")
        UiActions.Click(ManagePages.leftMenuBar.GetExpand())
