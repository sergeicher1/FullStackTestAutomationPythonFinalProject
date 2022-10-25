# Author      : Sergei Chernyahovsky
# Date        : 2022-10-23 08:55
# Language    : Python
# Version     : 3.10
# WebDriver   : Appium
# Version     : 1.3.0
# Selenium Ver: 3.141.0
# Title       : Full Stack test Automation Infrastructure
# Description : API Test Cases
# ----------------------------------------------------------------------------------------
import allure

from Extensions.Verifications import Verifications
from Utilities.CommonOps import LogMessage, GetData
from Workflows.ApiFlows import ApiFlows

url = GetData("URLAPI")
resource = GetData("APIResource")


class Test_API:

    @allure.title("Test Case 01: Get values from API response")
    @allure.description("This test receives values from api request")
    def test_TC01GetValues(self):
        LogMessage(message="Test Case 01: Getting values from API request")
        nodes = ["data", 0, "first_name"]  # Change here for specific extraction of data from response
        response = ApiFlows.GetValuesFromAPI(url + resource, nodes=nodes)
        print(response)

    @allure.title("Test Case 02: Post new record")
    @allure.description("This test creates a new record")
    def test_TC02CreateNewRecord(self):
        LogMessage(message="Test Case 02: Getting values from API request")
        response = ApiFlows.CreateANewRecord(url + resource, "Sergei", "QA Automation")
        Verifications.VerifyEquals(response, 201)

    @allure.title("Test Case 03: Update a record")
    @allure.description("This test updates a record")
    def test_TC03UpdateAndVerify(self):
        LogMessage(message="Test Case 03: Updating a record")
        response = ApiFlows.UpdateRecord(url + resource, "1", "Sergei", "Automation")
        Verifications.VerifyEquals(response, 201)

    @allure.title("Test Case 04: Delete record")
    @allure.description("This test deletes a record and verifies")
    def test_TC04DeleteAndVerify(self):
        LogMessage(message="Test Case 04: Delete record")
        response = ApiFlows.DeleteRecord(url + resource, "1")
        print(response)
