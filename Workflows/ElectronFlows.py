# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-23 13:05
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5
# Title       : Full Stack test Automation Infrastructure
# Description : Electron flows (dirty work) of test cases Unpack Electron App from rar for tests
# ----------------------------------------------------------------------------------------
import allure

from Extensions.UiActions import UiActions
from Extensions.Verifications import Verifications
from Utilities.CommonOps import LogMessage
from Utilities import ManagePages


class ElectronFlows:

    @staticmethod
    @allure.step("Verify the header Flow")
    def HeaderVerificationFlow(expected: str):
        header = ManagePages.electronTemp.GetHeader().text
        LogMessage(message=f"Verify header: {header} flow")
        Verifications.VerifyEquals(header, expected=expected)

    @staticmethod
    @allure.step("First input verification")
    def FirstInputVerificationFlow(expected: str):
        inputLabel = ManagePages.electronTemp.GetLabelCel().text
        LogMessage(message=f"Verify input: {inputLabel} flow")
        Verifications.VerifyEquals(inputLabel, expected=expected)

    @staticmethod
    @allure.step("Second input verification")
    def SecondInputVerificationFlow(expected: str):
        inputLabel = ManagePages.electronTemp.GetlLabelFahr().text
        LogMessage(message=f"Verify input: {inputLabel} flow")
        Verifications.VerifyEquals(inputLabel, expected=expected)

    @staticmethod
    @allure.step("Conversion from Celsius to Fahrenheit flow")
    def FromCelsiusToFahrenheitFlow(degrees: str):
        LogMessage(message=f"Converting from celsius: {degrees} degrees to fahrenheit")
        UiActions.Clear(ManagePages.electronTemp.GetInputCel())
        UiActions.UpdateText(ManagePages.electronTemp.GetInputCel(), degrees)
        result = ManagePages.electronTemp.GetInputFahr().text
        expected = (int(degrees) * 9 / 5) + 32
        Verifications.VerifyEquals(str(result), str(expected))

    @staticmethod
    @allure.step("Conversion from Fahrenheit to Celsius flow")
    def FromFahrenheitToCelsiusFlow(degrees: str):
        LogMessage(message=f"Converting from Fahrenheit: {degrees} degrees to Celsius")
        UiActions.Clear(ManagePages.electronTemp.GetInputFahr())
        UiActions.UpdateText(ManagePages.electronTemp.GetInputFahr(), degrees)
        result = ManagePages.electronTemp.GetInputCel().text
        expected = (int(degrees) - 32) * 5 / 9
        Verifications.VerifyEquals(str(result), str(expected))
