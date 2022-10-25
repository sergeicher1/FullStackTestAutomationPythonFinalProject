# --------------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-24 14:51
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Database Actions for Web, In future other platforms can Inherit from it
# --------------------------------------------------------------------------------------------

import allure

from TestCases import conftest
from Utilities.CommonOps import LogMessage


class DbActions:

    @staticmethod
    @allure.step("Query builder")
    # Example : "SELECT firstName,lastName FROM userdata"
    def QueryBuilder(columns, table):
        LogMessage(message="Building the sql query")
        cols = ",".join(columns)
        query = "SELECT " + cols + " FROM " + table
        return query

    @staticmethod
    @allure.step("Get query result")
    def GetQueryResult(columns, table):
        query = DbActions.QueryBuilder(columns=columns, table=table)
        dbCursor = conftest.dbConnector.cursor()
        dbCursor.execute(query)
        result = dbCursor.fetchall()
        return result  # Returns List of Tuples
