# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-20 08:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Test Cases clean -> Using other scripts as helpers
# ----------------------------------------------------------------------------------------

import allure
import pytest

from Utilities.CommonOps import *
from Workflows.Webflows import *


@pytest.mark.usefixtures("InitWebDriver")
class Test_Web:

    @allure.title("Test Case 01: Verify Login")
    @allure.description("This test verifies Login to Orange HRM")
    def test_TC01VerifyLogin(self):
        LogMessage(message="Test Case 01: Verifies Login to Orange HRM")
        # if data not entered:
        # should retrieve from login page or put in xml and use: GetData("UserName"), GetData("Password")
        WebFlows.LoginFlow()
        WebFlows.VerifyTitle("PIM")

    @allure.title("Test Case 02:  Verify Elements on Left Menu Bar Orange HRM – HR Management")
    @allure.description("This test verifies presentation of element on left menu bar")
    def test_TC02VerifyLeftMenuElements(self):
        LogMessage(message="Test Case 02: Verifying presentation of elements on left menu bar")
        WebFlows.VerifyElementsLeftMenuBar()

    @allure.title("Test Case 03: Verify Elements on Upper Menu")
    @allure.description("This test verifies presentation of elements on upper menu bar")
    def test_TC03VerifyUpperMenuElements(self):
        LogMessage(message="Test Case 03: Verifying elements in upper menu bar")
        WebFlows.VerifyElementsUpperMenuDropdown()

    @allure.title("Test Case 04: Create new employee and verify it was created")
    @allure.description("This test creates a new employee and verifies it was created")
    def test_TC04AddNewAndVerify(self):
        LogMessage(message="Test case 04: Create new employee and verify it was created")
        WebFlows.CreateAndVerifyNewEmployeeFlow(value1="Adam", value2="Sandler", ID="1")

    @allure.title("Test Case 05: Create  employees, using data driven test")
    @allure.description("This test created  employees, using data driven test")
    @pytest.mark.parametrize("value1, value2", testData)
    def test_TC05CreateEmployeesDataDriven(self, value1, value2):
        LogMessage(message="creating  employees, using data driven test")
        UiActions.Click(ManagePages.pimPage.GetEmployeeList())
        WebFlows.CreateAndVerifyNewEmployeeFlow(value1=value1, value2=value2, ID="10")

    @allure.title("Test Case 06: Delete employee by ID")
    @allure.description("This test filters employees by ID, deletes it and verify it was deleted")
    def test_TC06DeleteEmployeeByID(self):
        LogMessage(message="Filtering by employee ID, and then delete it")
        WebFlows.DeleteByID("0001")  # Should be entered, in future can be added to data driven

    @allure.title("Test Case 07: Visual Testing")
    @allure.description(
        "This visual test, mostly will fail because of orange always updated by others,"
        " or not executed because of limitation of applitools ")
    @pytest.mark.skipif(GetData("ExecuteApplitools").lower() == "no",
                        reason="Limit execution of applitools, if needed change to yes in data.xml")
    def test_TC07VisualTestLeftSidebarLogo(self):
        LogMessage(message="Visual testing of left sidebar being executed")
        WebFlows.ExpandLeftSidebar()
        conf.eyes.open(conf.driver, "Orange HRM", "Visual testing left sidebar")
        conf.eyes.check_window("Left sidebar logo")
