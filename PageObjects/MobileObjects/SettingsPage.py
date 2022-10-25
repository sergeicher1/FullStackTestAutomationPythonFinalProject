# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-22 19:01
# Language    : Python
# Version     : 3.10
# WebDriver   : Appium
# Version     : 1.3.0
# Selenium Ver: 3.141.0
# Title       : Full Stack test Automation Infrastructure
# Description : Page Objects that are located on Mobile Settings Page - Mobile apk
# ----------------------------------------------------------------------------------------


from selenium.webdriver.common.by import By

from Utilities.CommonOps import LogMessage

signature = (By.XPATH, "//*[@text='Your signature']")
editField = (By.XPATH, "//*[@id='edit']")
okBtn = (By.XPATH, "//*[@text='OK']")
defReply = (By.XPATH, "//*[@text='Default reply action']")
replyToAll = (By.XPATH, "//*[@text='Reply to all']")
syncEmail = (By.XPATH, "//*[@text='Sync email periodically']")
downIncAttach = (By.XPATH, "//*[@text='Download incoming attachments']")


class SettingsPage:

    def __init__(self, driver):
        LogMessage(message="Constructor __init__ of Settings page")
        self.driver = driver

    def GetSignature(self):
        LogMessage(message="Locating signature element")
        return self.driver.find_element(signature[0], signature[1])

    def GetEditField(self):
        LogMessage(message="Locating edit field")
        return self.driver.find_element(editField[0], editField[1])

    def GetOkBtn(self):
        LogMessage(message="Locating ok button")
        return self.driver.find_element(okBtn[0], okBtn[1])

    def GetDefReply(self):
        LogMessage(message="Locating default reply element")
        return self.driver.find_element(defReply[0], defReply[1])

    def GetReplyToAll(self):
        LogMessage(message="Locating reply to all element")
        return self.driver.find_element(replyToAll[0], replyToAll[1])

    def GetSyncEmail(self):
        LogMessage(message="Locating sync email element")
        return self.driver.find_element(syncEmail[0], syncEmail[1])

    def GetDownIncAttach(self):
        LogMessage(message="Locating download incoming attachments")
        return self.driver.find_element(downIncAttach[0], downIncAttach[1])
