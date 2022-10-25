# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# Author      : Sergei Chernyahovsky
# Date        : 2022-10-21 08:39
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4.5.0 for driver initialization to work Only for WEB TESTS !!!!
# Title       : Full Stack test Automation Infrastructure
# Description : Page Objects that are located on Left Navigation Bar
# ----------------------------------------------------------------------------------------

from selenium.webdriver.common.by import By
from Utilities.CommonOps import LogMessage

imageBanner = (By.XPATH, "//img[@alt='client brand banner']")
search = (By.XPATH, "//input[@placeholder='Search']")
listAmount = (By.XPATH, "//ul[@class='oxd-main-menu']/li")  # without logo and search == 11
admin = (By.XPATH, "//*/a[@href='/web/index.php/admin/viewAdminModule']")
pim = (By.XPATH, "//*/a[@href='/web/index.php/pim/viewPimModule']")
leave = (By.XPATH, "//*/a[@href='/web/index.php/leave/viewLeaveModule']")
time = (By.XPATH, "//*/a[@href='/web/index.php/time/viewTimeModule']")
recruitment = (By.XPATH, "//*/a[@href='/web/index.php/recruitment/viewRecruitmentModule']")
myInfo = (By.XPATH, "//*/a[@href='/web/index.php/pim/viewMyDetails']")
performance = (By.XPATH, "//*/a[@href='/web/index.php/performance/viewPerformanceModule']")
dashboard = (By.XPATH, "//*/a[@href='/web/index.php/dashboard/index']")
directory = (By.XPATH, "//*/a[@href='/web/index.php/directory/viewDirectory']")
maintenance = (By.XPATH, "//*/a[@href='/web/index.php/maintenance/viewMaintenanceModule']")
buzz = (By.XPATH, "//*/a[@href='/web/index.php/buzz/viewBuzz']")
collapse = (By.XPATH, "//i[@class='oxd-icon bi-chevron-left']")
expand = (By.XPATH, "//div/button/i[@class='oxd-icon bi-chevron-right']")


class LeftMenuBar:

    def __init__(self, driver):
        LogMessage(message="Constructor __init__ of LeftMenuBar")
        self.driver = driver

    def GetImageBanner(self):
        LogMessage(message="Locating image logo on left menu bar")
        return self.driver.find_element(imageBanner[0], imageBanner[1])

    def GetSearch(self):
        LogMessage(message="Locating search element")
        return self.driver.find_element(search[0], search[1])

    def GetListAmount(self):
        LogMessage(message="Locating amount of elements on left menu bar")
        return self.driver.find_elements(listAmount[0], listAmount[1])

    def GetAdmin(self):
        LogMessage(message="Locating admin element")
        return self.driver.find_element(admin[0], admin[1])

    def GetPim(self):
        LogMessage(message="Locating pim element")
        return self.driver.find_element(pim[0], pim[1])

    def GetLeave(self):
        LogMessage(message="Locating leave element")
        return self.driver.find_element(leave[0], leave[1])

    def GetTime(self):
        LogMessage(message="Locating time element")
        return self.driver.find_element(time[0], time[1])

    def GetRecruitment(self):
        LogMessage(message="Locating recruitment element")
        return self.driver.find_element(recruitment[0], recruitment[1])

    def GetMyInfo(self):
        LogMessage(message="Locating my info element")
        return self.driver.find_element(myInfo[0], myInfo[1])

    def GetPerformance(self):
        LogMessage(message="Locating performance element")
        return self.driver.find_element(performance[0], performance[1])

    def GetDashboard(self):
        LogMessage(message="Locating dashboard element")
        return self.driver.find_element(dashboard[0], dashboard[1])

    def GetDirectory(self):
        LogMessage(message="Locating directory element")
        return self.driver.find_element(directory[0], directory[1])

    def GetMaintenance(self):
        LogMessage(message="Locating maintenance element")
        return self.driver.find_element(maintenance[0], maintenance[1])

    def GetBuzz(self):
        LogMessage(message="Locating buzz element")
        return self.driver.find_element(buzz[0], buzz[1])

    def GetCollapse(self):
        LogMessage(message="Locating collapse button")
        return self.driver.find_element(collapse[0], collapse[1])

    def GetExpand(self):
        LogMessage(message="Locating expand button")
        return self.driver.find_element(expand[0], expand[1])
