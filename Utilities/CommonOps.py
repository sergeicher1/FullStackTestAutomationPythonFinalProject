# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-19 17:00
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Common Operations for entire Project
# ----------------------------------------------------------------------------------------

import csv
from datetime import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET
import TestCases.conftest as conf

'''Functions to Read Files'''


# Reads data from data.xml for configuration of the Project
# Parameter   : Name of the attribute in xml file
# Return value: String
def GetData(name: str) -> str:
    LogMessage(message="Reading data from data.xml")
    root = ET.parse("D:\\AtidAutomation\\FullStackFinalProject\\Configuration\\data.xml").getroot()
    return root.find(".//" + name).text


# Function to read CSV files for Data Driven Testing
def ReadCsv(fileName):
    LogMessage(message=f"Reading data from {fileName}")
    data = []
    with open(fileName, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data), row)
        return data


'''Functions to Write Files'''


# Logging
def LogMessage(message: str):
    with open(r"D:\AtidAutomation\FullStackFinalProject\TextLogs\ExecutionLog.txt", "a") as logFile:
        logFile.write(f"\n{datetime.now()} " + message)


'''Function to Explicitly Wait for elements'''


def Wait(forElement, elem):  # TODO: If needed in final version
    if forElement == "elementExists":
        WebDriverWait(conf.driver, int(GetData("WaitTime"))).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif forElement == "elementDisplayed":
        WebDriverWait(conf.driver, int(GetData("WaitTime"))).until(EC.visibility_of_element_located((elem[0], elem[1])))
    '''Can be extended here '''


'''Enums for different conditions in entire project'''


# Enum For is for selecting displayed or exist element, my Wait method uses this enum
class For:
    elementExists = "elementExists"
    elementDisplayed = "elementDisplayed"


# Enum By is for search users By text or By index TODO: If needed in final version
class By:
    user = "user"
    index = "index"


# Enum Save is for selecting whether we want to save mortgage transaction or not TODO: If needed in final version
class Save:
    Yes = True
    No = False


# Enum for selecting whether we want to save mortgage transaction or not TODO: If needed in final version
class Direction:
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"
