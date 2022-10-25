# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-19 16:30
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : This is a configuration file for the entire Project
# ----------------------------------------------------------------------------------------

from time import sleep
import mysql.connector
import allure
import pytest
from datetime import *
import appium
import selenium
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from Utilities.EventListener import EventListener
from appium import webdriver as AWebDriver
from selenium.webdriver import ActionChains
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from Utilities.CommonOps import *
from selenium import webdriver as SWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from applitools.selenium import Eyes
from Utilities.ManagePages import ManagePages

'''Objects Initialization'''
driver = None
action = None
action2 = None
multiAction = None
mobileSize = None
eyes = Eyes()  # Applitools
dbConnector = None

'''Web Driver Initialization'''

# Only with selenium 4x for Web Testing, doesn't include Applitools
# For Applitools, downgrade to selenium 3.141.0 stable version,
# be careful, driver initiation will not work for other browsers!!!
# COMMENT SECTIONS FOR OTHER PLATFORMS FOR PROPER EXECUTION
########################################################################################################

'''Web Driver Initialization'''


@pytest.fixture(scope="class")
def InitWebDriver(request):
    if GetData("ExecuteApplitools").lower() == "yes":  # Applitools doesn't support eventListeners
        LogMessage(message="Initializing WebDriver for Applitools that doesn't support eventListeners")
        globals()["driver"] = GetWebDriver()
    else:
        edriver = GetWebDriver()
        LogMessage(message="Initializing WebDriver with eventListeners")
        globals()["driver"] = EventFiringWebDriver(edriver, EventListener())

    driver = globals()["driver"]
    driver.maximize_window()
    driver.implicitly_wait(int(GetData("WaitTime")))
    driver.get(GetData("URL"))
    request.cls.driver = driver
    globals()["action"] = ActionChains(driver)
    ManagePages.InitWebPages()

    if GetData("ExecuteApplitools").lower() == "yes":  # Applitools
        eyes.api_key = GetData("ApplitoolsKey")
    yield
    LogMessage(message="quitting webdriver")
    globals()["driver"].quit()
    if GetData("ExecuteApplitools").lower() == "yes":  # Applitools
        eyes.close()
        eyes.abort()
        LogMessage(message="quitting eyes of Applitools")


# Checks which browser is requested for execution
def GetWebDriver():
    browser = GetData("Browser")
    LogMessage(message="Checking browser type requested")
    if browser.lower() == "chrome":
        LogMessage(message="Chrome browser is chosen")
        driver = GetChrome()
    elif browser.lower() == "firefox":
        LogMessage(message="Firefox browser is chosen")
        driver = GetFirefox()
    elif browser.lower() == "edge":
        LogMessage(message="Edge browser is chosen")
        driver = GetEdge()
    else:
        driver = None
        LogMessage(message="No browser is chosen")
        raise Exception("Wrong Input for browser, check configuration in .xml file!")
    return driver


'''Initialize specific WebDriver'''


def GetChrome():
    chromeDriver = SWebDriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return chromeDriver


def GetFirefox():
    ffDriver = SWebDriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    return ffDriver


def GetEdge():
    edgeDriver = SWebDriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    return edgeDriver


########################################################################################################
# CHANGE selenium to 3.141.0 and comment everything for web driver

'''Mobile Driver Initialization'''

# @pytest.fixture(scope="class")
# def InitMobileDriver(request):
#     edriver = GetMobileDriver()
#     globals()["driver"] = EventFiringWebDriver(edriver, EventListener())
#     driver = globals()["driver"]
#     driver.implicitly_wait(int(GetData("WaitTime")))
#     request.cls.driver = driver
#     globals()["action"] = TouchAction(driver)  # Actions for mobile
#     request.cls.action = globals()["action"]
#     globals()["action2"] = TouchAction(driver)  # Actions for mobile
#     request.cls.action2 = globals()["action2"]
#     globals()["multiAction"] = MultiAction(driver)  # Multi Actions for mobile(zoom/pinch)
#     request.cls.multiAction = globals()["multiAction"]
#     globals()["mobileSize"] = driver.get_window_size()
#     request.cls.mobileSize = globals()["mobileSize"]
#
#     ManagePages.InitMobilePages()
#     yield
#     driver.quit()
#
#
# def GetMobileDriver():
#     if GetData("MobileDevice").lower() == "android":
#         driver = GetAndroid(GetData("Udid"))
#     elif GetData("MobileDevice").lower() == "ios":
#         driver = GetIOS(GetData("Udid"))
#     else:
#         driver = None
#         raise Exception("Wrong input, Unrecognized mobile operating system")
#     return driver
#
#
# def GetAndroid(udid):
#     dc = {}
#     dc['udid'] = udid
#     dc['appPackage'] = GetData("AppPackage")
#     dc['appActivity'] = GetData("AppActivity")
#     dc['platformName'] = 'android'
#     androidDriver = AWebDriver.Remote(GetData("AppiumServer"), dc)  # alias AWebDriver
#     return androidDriver
#
#
# def GetIOS(udid):
#     dc = {}
#     dc['udid'] = udid
#     dc['bundle_id'] = GetData("BundleID")
#     dc['platformName'] = 'ios'
#     iosDriver = AWebDriver.Remote(GetData("AppiumServer"), dc)
#     return iosDriver


########################################################################################################

'''Electron Driver Initiation'''

# @pytest.fixture(scope="class")
# def InitElectronDriver(request):
#     globals()["driver"] = GetElectronDriver()
#     driver = globals()["driver"]
#     driver.implicitly_wait(int(GetData("WaitTime")))
#     request.cls.driver = driver
#     globals()["action"] = ActionChains(driver)
#     request.cls.driver = globals()["action"]
#     ManagePages.InitElectronPages()
#
#     yield
#     driver.quit()
#
#
# def GetElectronDriver():
#     options = selenium.webdriver.ChromeOptions()
#     options.binary_location = GetData("ElectronApp")
#     driver = selenium.webdriver.Chrome(options=options, executable_path=GetData("ElectronDriver"))
#     return driver


########################################################################################################

'''Win Driver Initiation'''

# @pytest.fixture(scope="class")
# def InitDesktopDriver(request):
#     edriver = GetDesktopDriver()
#     globals()["driver"] = EventFiringWebDriver(edriver, EventListener())
#     driver = globals()["driver"]
#     driver.implicitly_wait(int(GetData("WaitTime")))
#     request.cls.driver = driver
#     ManagePages.IniDesktopPages()
#
#     yield
#     driver.quit()
#
#
# def GetDesktopDriver():
#     dc = {}
#     dc["app"] = GetData("ApplicationName")
#     dc["platformName"] = "Windows"
#     dc["deviceName"] = "WinowsPC"
#     driver = appium.webdriver.Remote(GetData("WinAppDriverService"), dc)
#     return driver


########################################################################################################

'''Database connection'''


@pytest.fixture(scope="class")
def initDBConnection(request):  # Open session
    dbConnector = mysql.connector.connect(
        host=GetData("DbHost"),
        database=GetData("DbName"),
        user=GetData("DbUser"),
        password=GetData("DbPassword")
    )
    globals()["dbConnector"] = dbConnector
    request.cls.dbConnector = dbConnector

    yield
    dbConnector.close()  # Close session


########################################################################################################

'''Catch Exceptions Errors and Screenshots'''


# This is exception for API test
# If it is None -> Screenshot will not be captured, because no browser is opened!
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()["driver"] is not None:
            image = GetData("ScreenshotPath") + "screen_" + str(datetime.now()).replace(":", "-") + ".png"
            globals()["driver"].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
