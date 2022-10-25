# Author      : Sergei Chernyahovsky
# Date        : 2022-10-23 08:25
# Language    : Python
# Version     : 3.10
# WebDriver   : Appium
# Version     : 1.3.0
# Selenium Ver: 3.141.0
# Title       : Full Stack test Automation Infrastructure
# Description : API Actions
# ----------------------------------------------------------------------------------------

import allure
import requests

from Utilities.CommonOps import LogMessage

header = {"Content-type": "application/json"}


class ApiActions:

    @staticmethod
    @allure.step("Get Request")
    def Get(path):
        LogMessage(message="Using get request")
        response = requests.get(path)
        return response

    @staticmethod
    @allure.step("Extract value from response")
    def ExtractValueFromResponse(response, nodes):
        LogMessage(message="Extracting value from response")
        extractedValue = None
        rJSON = response.json()
        if len(nodes) == 1:
            extractedValue = rJSON[nodes[0]]
        elif len(nodes) == 2:
            extractedValue = rJSON[(nodes[0])][(nodes[1])]
        elif len(nodes) == 3:
            extractedValue = rJSON[(nodes[0])][(nodes[1])][(nodes[2])]
        return extractedValue

    @staticmethod
    @allure.step("Post Request")
    def Post(path, payload):
        LogMessage(message="Post request")
        response = requests.post(path, json=payload, headers=header)
        return response.status_code

    @staticmethod
    @allure.step("Put Request")
    def Put(path, payload):
        LogMessage(message="Put request")
        response = requests.put(path, json=payload, headers=header)
        return response.status_code

    @staticmethod
    @allure.step("Delete Request")
    def Delete(path, ID):
        LogMessage(message="Delete request")
        response = requests.delete(path, ID)
        return response.status_code
