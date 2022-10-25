# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-23 14:00
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Test Cases clean -> Using other scripts as helpers 1
# ----------------------------------------------------------------------------------------

import allure
import pytest

from Utilities.CommonOps import LogMessage
from Workflows.ElectronFlows import ElectronFlows


@pytest.mark.usefixtures("InitElectronDriver")
class Test_ElectronMyApp:

    @allure.title("Test Case 01: Header Verification")
    @allure.description("This test verifies the header")
    def test_TC01Header(self):
        LogMessage(message="Test Case 01: header verification")
        ElectronFlows.HeaderVerificationFlow("Temperature Converter")

    @allure.title("Test Case 02: Celsius input label verification")
    @allure.description("This test verifies the celsius input")
    def test_TC02CelLabel(self):
        LogMessage(message="Test Case 02: celsius label verification")
        ElectronFlows.FirstInputVerificationFlow("Celsius:")

    @allure.title("Test Case 03: Fahrenheit input label verification")
    @allure.description("This test verifies the Fahrenheit input")
    def test_TC03FahLabel(self):
        LogMessage(message="Test Case 03: Fahrenheit label verification")
        ElectronFlows.SecondInputVerificationFlow("Fahrengeit:")

    @allure.title("Test Case 04: Convert from celsius to fahrenheit")
    @allure.description("This test converts from celsius to fahrenheit")
    def test_TC04CelToFahr(self):
        LogMessage(message="Test Case 04: Convert from celsius to fahrenheit")
        ElectronFlows.FromCelsiusToFahrenheitFlow("10")

    @allure.title("Test Case 05: Convert from fahrenheit to celsius")
    @allure.description("This test converts from fahrenheit to celsius")
    def test_TC04FahrToCel(self):
        LogMessage(message="Test Case 05: Convert from fahrenheit to celsius")
        ElectronFlows.FromFahrenheitToCelsiusFlow("50")
