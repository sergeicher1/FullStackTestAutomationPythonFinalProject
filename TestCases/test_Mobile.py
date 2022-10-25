# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-23 00:06
# Language    : Python
# Version     : 3.10
# WebDriver   : Appium
# Version     : 1.3.0
# Selenium Ver: 3.141.0
# Title       : Full Stack test Automation Infrastructure
# Description : Test Cases clean -> Using other scripts as helpers
# ----------------------------------------------------------------------------------------

import allure
import pytest

from Utilities.CommonOps import LogMessage
from Workflows.MobileFlows import MobileFlows


@pytest.mark.usefixtures("InitMobileDriver")
class Test_Mobile:

    @allure.title("Test Case 01: Change signature")
    @allure.description("This test changes the signature of the app")
    def test_TC01ChangeSignature(self):
        LogMessage(message="Signature flow")
        MobileFlows.SignatureFlow(value="Sergei")

    @allure.title("Test Case 02: Change default reply action")
    @allure.description("This test changes default replay action")
    def test_TC02ChangeReplyAction(self):
        LogMessage(message="Change default reply action")
        MobileFlows.ChangeDefaultReplyFlow()
