# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-22 23:55
# Language    : Python
# Version     : 3.10
# WebDriver   : Appium
# Version     : 1.3.0
# Selenium Ver: 3.141.0
# Title       : Full Stack test Automation Infrastructure
# Description : Mobile flows (dirty work) of test cases
# ----------------------------------------------------------------------------------------
from time import sleep

import allure

from Extensions.MobileActions import MobileActions
from Utilities import ManagePages
from Utilities.CommonOps import LogMessage


# Mobile business flow

class MobileFlows:

    @staticmethod
    @allure.step("Set signature flow")
    def SignatureFlow(value: str):
        LogMessage(message="Changing signature in the app")
        MobileActions.Click(ManagePages.settingMobilePage.GetSignature())
        sleep(0.5)
        ManagePages.settingMobilePage.GetEditField().send_keys(value)
        MobileActions.Click(ManagePages.settingMobilePage.GetOkBtn())

    @staticmethod
    @allure.step("Change default reply action")
    def ChangeDefaultReplyFlow():
        LogMessage(message="Changing default reply action to reply to all")
        MobileActions.Click(ManagePages.settingMobilePage.GetDefReply())
        MobileActions.Click(ManagePages.settingMobilePage.GetReplyToAll())
