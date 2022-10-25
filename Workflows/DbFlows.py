# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-24 15:15
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5
# Title       : Full Stack test Automation Infrastructure
# Description : Database flows (dirty work) of test cases
# ----------------------------------------------------------------------------------------
import allure

from Extensions.DbActions import DbActions
from Utilities.CommonOps import LogMessage
from Workflows.Webflows import WebFlows


class DbFlows:

    @staticmethod
    @allure.step("Login to Orange HRM and create new users stored in data base")
    def LoginAndCreateWithDatabaseFlow():
        LogMessage(message="Login and create new employees using data from database flow")
        columns = ["fitstName", "lastName"]
        result = DbActions.GetQueryResult(columns, "userdata")
        WebFlows.LoginFlow()
        WebFlows.CreateAndVerifyNewEmployeeFlow(result[0][0],
                                                result[0][1])  # change here the resulted list from database

