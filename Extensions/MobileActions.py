# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-22 23:51
# Language    : Python
# Version     : 3.10
# WebDriver   : Appium
# Version     : 1.3.0
# Selenium Ver: 3.141.0
# Title       : Full Stack test Automation Infrastructure
# Description : Mobile Actions, inherit from UI Actions
# ----------------------------------------------------------------------------------------

import allure

from Extensions.UiActions import UiActions
from TestCases import conftest


# Not all used in this specific project, but very useful implementation for future infrastructure
class MobileActions(UiActions):

    @staticmethod
    @allure.step("Tap on Element")
    def Tap(elem, times=1):
        conftest.action.tap(elem, times).perform()

    @staticmethod
    @allure.step("Swipe Screen")
    def Swipe(startX, startY, endX, endY, duration):
        conftest.driver.swipe(startX, startY, endX, endY, duration)

    @staticmethod
    @allure.step("Zoom Screen")
    def Zoom(element, pixels=200):
        action1 = conftest.action
        action2 = conftest.action2
        multiAction = conftest.multiAction
        xLoc = element.rect["x"]
        yLoc = element.rect["y"]
        action1.long_press(x=xLoc, y=yLoc).movet_to(x=xLoc, y=yLoc + pixels).wait(500).release()
        action2.long_press(x=xLoc, y=yLoc).movet_to(x=xLoc, y=yLoc - pixels).wait(500).release()
        multiAction.add(action1, action2)
        multiAction.perform()

    @staticmethod
    @allure.step("Pinch Screen")
    def Pinch(element, pixels=200):
        action1 = conftest.action
        action2 = conftest.action2
        multiAction = conftest.multiAction
        xLoc = element.rect["x"]
        yLoc = element.rect["y"]
        action1.long_press(x=xLoc, y=yLoc + pixels).movet_to(x=xLoc, y=yLoc).wait(500).release()
        action2.long_press(x=xLoc, y=yLoc - pixels).movet_to(x=xLoc, y=yLoc).wait(500).release()
        multiAction.add(action1, action2)
        multiAction.perform()
