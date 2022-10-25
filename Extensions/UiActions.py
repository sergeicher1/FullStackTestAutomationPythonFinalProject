# --------------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-20 10:00
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : User Interface Actions for Web, In future other platforms can Inherit from it
# --------------------------------------------------------------------------------------------

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from TestCases import conftest
from TestCases.conftest import action
from Utilities.CommonOps import LogMessage


class UiActions:

    @staticmethod
    @allure.step("Click On Element")
    def Click(elem: WebElement):
        LogMessage(message=f"Clicking on {elem}")
        elem.click()

    @staticmethod
    @allure.step("Clear field")
    def Clear(elem: WebElement):
        LogMessage(message=f"Clearing {elem} field")
        elem.clear()

    @staticmethod
    @allure.step("Updating text")
    def UpdateText(elem: WebElement, value: str):
        LogMessage(message=f"Updating {elem} with {value}")
        elem.send_keys(value)

    @staticmethod
    @allure.step("Mouse hover")
    def MouseHover(elem1: WebElement, elem2: WebElement):
        LogMessage(message=f"Hovering mouse to {elem1}, click and move to {elem2} and click")
        action.move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step("Mouse hover tooltip")  # for electron app
    def MouseHoverTooltip(elem: WebElement):
        LogMessage(message=f"Hovering mouse tooltip to {elem}, click ")
        # Because of dynamic rendering actionChains should be initialized every time for mobile?
        ActionChains(conftest.driver).move_to_element(elem).click().perform()

    @staticmethod
    @allure.step("Mouse Right Click")
    def MouseRightClick(elem: WebElement):
        LogMessage(message=f"Mouse right click on {elem}")
        action.context_click(elem).perform()

    @staticmethod
    @allure.step("Drag And Drop")
    def DragAndDrop(elem1: WebElement, elem2: WebElement):
        LogMessage(message=f"Dragging {elem1} and Dropping {elem2}")
        action.drag_and_drop(elem1, elem2).perform()
