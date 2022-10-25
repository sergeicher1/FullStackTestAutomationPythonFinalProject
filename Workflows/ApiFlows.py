# Author      : Sergei Chernyahovsky
# Date        : 2022-10-23 08:47
# Language    : Python
# Version     : 3.10
# WebDriver   : Appium
# Version     : 1.3.0
# Selenium Ver: 3.141.0
# Title       : Full Stack test Automation Infrastructure
# Description : API Flows (dirty work) for test cases
# ----------------------------------------------------------------------------------------

import allure
import requests

from Extensions.ApiActions import ApiActions
from Utilities.CommonOps import GetData, LogMessage


class ApiFlows:

    @staticmethod
    @allure.step("Get values from response")
    def GetValuesFromAPI(path, nodes):
        LogMessage(message="Getting values from response")
        response = ApiActions.Get(path)
        return ApiActions.ExtractValueFromResponse(response, nodes)

    @staticmethod
    @allure.step("Post a new data to server")
    def CreateANewRecord(path, name: str, job: str):
        LogMessage(message="Creating a new data")
        payload = {
            "name": name, "job": job
        }
        response = ApiActions.Post(path, payload)
        return response

    @staticmethod
    @allure.step("Update a record")
    def UpdateRecord(path, ID: str, name: str, job: str):
        LogMessage(message="Updating data")
        payload = {
            "name": name, "job": job
        }
        response = ApiActions.Post(path + "/" + ID, payload)
        return response

    @staticmethod
    @allure.step("Delete record by ID")
    def DeleteRecord(path, ID: str):
        LogMessage(message="Deleting record by ID")
        response = requests.delete(path + "/" + ID)
        return response
