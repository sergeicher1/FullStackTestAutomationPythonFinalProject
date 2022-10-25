# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-24 15:30
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Test Cases clean -> Using other scripts as helpers
# ----------------------------------------------------------------------------------------
import allure
import pytest
from time import sleep

from Utilities.CommonOps import LogMessage
from Workflows.DbFlows import DbFlows


@pytest.mark.usefixtures("InitWebDriver")
@pytest.mark.usefixtures("initDBConnection")
class Test_WebDataBase:

    @allure.title("Test Case 01: Login to orange hrm and create new employees using database")
    @allure.description("This test logins to orange hrm and creates new employees using database")
    def test_LoginCreateWithDatabase(self):
        LogMessage(message="Test Case 01: loging in to orange hrm and creates new employees using database")
        DbFlows.LoginAndCreateWithDatabaseFlow()
        sleep(3)
