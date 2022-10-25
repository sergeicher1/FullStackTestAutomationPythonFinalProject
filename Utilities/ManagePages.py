# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-20 09:00
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Managing pages with their Page Objects
# ----------------------------------------------------------------------------------------

from PageObjects.DesktopObjects.WPFPage import WPFPage
from PageObjects.ElectronObjects.MainPage import MainPage
from PageObjects.MobileObjects.SettingsPage import SettingsPage
from PageObjects.WebObjects.LeftMenuBar import LeftMenuBar
from PageObjects.WebObjects.LoginPage import LoginPage
from PageObjects.WebObjects.PimAddEmployeePage import PimAddEmployeePage
from PageObjects.WebObjects.PimPage import PimPage
from PageObjects.WebObjects.UpperMenuBar import UpperMenuBar
from TestCases import conftest
from Utilities.CommonOps import LogMessage

'''Web Objects'''
loginPage = None
pimPage = None
leftMenuBar = None
upperMenuBar = None
pipAddEmployeePage = None

'''Mobile Objects'''
settingMobilePage = None

'''Electron Objects'''
electronTemp = None

'''Desktop Objects'''
myAppWPF = None


class ManagePages:

    # Initialization of web objects
    @staticmethod
    def InitWebPages():
        LogMessage(message="Initializing Web Objects")
        globals()["loginPage"] = LoginPage(conftest.driver)
        globals()["pimPage"] = PimPage(conftest.driver)
        globals()["leftMenuBar"] = LeftMenuBar(conftest.driver)
        globals()["upperMenuBar"] = UpperMenuBar(conftest.driver)
        globals()["pipAddEmployeePage"] = PimAddEmployeePage(conftest.driver)

    # Initialization of mobile objects
    @staticmethod
    def InitMobilePages():
        LogMessage(message="Initializing Mobile Objects")
        globals()["settingMobilePage"] = SettingsPage(conftest.driver)

    # Initialization of electron objects
    @staticmethod
    def InitElectronPages():
        LogMessage(message="Initializing Electron Objects")
        globals()["electronTemp"] = MainPage(conftest.driver)

    # Initialization of desktop objects
    @staticmethod
    def IniDesktopPages():
        LogMessage(message="Initializing Desktop Objects")
        globals()["myAppWPF"] = WPFPage(conftest.driver)
