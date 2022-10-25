# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-24 13:15
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5
# Title       : Full Stack test Automation Infrastructure
# Description : Desktop flows (dirty work) of test cases
# ----------------------------------------------------------------------------------------
import allure

from Extensions.UiActions import UiActions
from Utilities.CommonOps import LogMessage
from Utilities import ManagePages


class DesktopFlows:

    @staticmethod
    @allure.step("Click the checkbox")
    def ClickCheckboxFlow():
        LogMessage(message="Clicking the check box flow")
        UiActions.Click(ManagePages.myAppWPF.GetCheckBox())

    @staticmethod
    @allure.step("Insert text to text box flow")
    def InsertTextFlow(value: str):
        LogMessage(message="Insert text to text box flow")
        UiActions.Clear(ManagePages.myAppWPF.GetTextBox())
        UiActions.UpdateText(ManagePages.myAppWPF.GetTextBox(), value=value)

    @staticmethod
    @allure.step("Click the radio button")
    def ClickRadioBtnFlow():
        LogMessage(message="Clicking the radio button flow")
        UiActions.Click(ManagePages.myAppWPF.GetRadioButton())

    @staticmethod
    @allure.step("Hover and click flow")
    def HoverAndClickFlow():
        LogMessage(message="Hovering and clicking flow")
        UiActions.MouseHoverTooltip(ManagePages.myAppWPF.GetButton())
        UiActions.Click(ManagePages.myAppWPF.GetRadioButton())  # To remove the pointer from button to see effect

