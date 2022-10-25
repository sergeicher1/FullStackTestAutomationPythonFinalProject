# --------------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-20 10:15
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Different Verifications(assertions) for entire Project
# --------------------------------------------------------------------------------------------

import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations

from Utilities.CommonOps import LogMessage


class Verifications:

    @staticmethod
    @allure.step("Equality Verification")
    def VerifyEquals(actual, expected):
        LogMessage(message=f"Verifying {actual} equals to {expected} ?")
        assert actual == expected, "Equality Verification FAILED, actual: " + str(
            actual) + " is not Equals to expected: " + str(expected)

    @staticmethod
    @allure.step("Verify if element is displayed on page")
    def VerifyIsDisplayed(elem: WebElement):
        LogMessage(message=f"Verifying if the {elem} is displayed on page? ")
        assert elem.is_displayed(), "Verification is FAILED, Element: " + elem.text + " is not displayed!"

    '''Method to append FAILED assertion to list, and check only in the end of test case'''

    # Verify Menu Buttons Using smart - assertion Yoni's implementation
    @staticmethod
    @allure.step("Soft Displayed elements")
    def SoftDisplayed(elements):
        LogMessage(message=f"Method Soft Displayed is used on {elements}")
        failedElements = []
        for i in range(len(elements)):
            if not elements[i].is_displayed():
                failedElements.insert(len(failedElements), elements[i].get_attribute("aria-label"))
        if len(failedElements) > 0:
            for failedElement in failedElements:
                print("Soft Displayed FAILED, Element which have FAILED: ",
                      str(failedElement))  # Doesn't know what to expect, cast to string
            raise AssertionError("Soft Displayed FAILED")

    # Verify Menu Buttons Using Installed package smart - assertion
    @staticmethod
    @allure.step("Soft Assert(Verification) using soft_assert")
    def SmartAssert(elems):
        LogMessage(message=f"Method Soft Assert is used on {elems}")
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()

    @staticmethod
    @allure.step("Verification of amount of elements in table")
    def VerifyAmountOfElements(elems, expectedSize):
        LogMessage(message=f"Verification an amount of {elems} with {expectedSize} in table")
        assert len(elems) == expectedSize, "Number of elements in list: " + str(
            len(elems)) + " doesn't match expected size: " + str(expectedSize)

    # @staticmethod TODO: Check if needed, because every page should implement it...
    # @allure.step("Verify current URL")
    # def VerifyCurrentURL(actual: str, expected: str):
    #     LogMessage(message=f"Verifying current URL {actual} and expected {expected}")
    #     assert actual == expected, f"actual: {actual} is not equal to expected: {expected}"
