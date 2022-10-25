# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-24 13:31
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Test Cases clean -> Using other scripts as helpers
# ----------------------------------------------------------------------------------------

import allure
import pytest

from Utilities.CommonOps import LogMessage
from Workflows.DesktopFlows import DesktopFlows


@pytest.mark.usefixtures("InitDesktopDriver")
class Test_DesktopMyApp:

    @allure.title("Test Case 01: Verify the checkbox")
    @allure.description("This test verifies on the checkbox")
    def test_TC01ClickCheckbox(self):
        LogMessage(message="Test Case 01: Verifying the check box")
        DesktopFlows.ClickCheckboxFlow()

    @allure.title("Test Case 02: Insert text to text box")
    @allure.description("This test inserts text to text box")
    def test_TC02InsertText(self):
        LogMessage(message="Test Case 03: Inserting new text to text box")
        DesktopFlows.InsertTextFlow("This is a new text")

    @allure.title("Test Case 03: Verify the radio button")
    @allure.description("This test verifies on the radio button")
    def test_TC03ClickRadioBtn(self):
        LogMessage(message="Test Case 03: Verifying the radio button")
        DesktopFlows.ClickRadioBtnFlow()

    @allure.title("Test Case 04: Hover to see effect and click to see effect")
    @allure.description("This test hovers and clicks the button")
    def test_TC04HoverClick(self):
        LogMessage(message="Test Case 04: Hovers and clicks to see effect")
        DesktopFlows.HoverAndClickFlow()
