# ----------------------------------------------------------------------------------------
# -- coding   : utf-8 --
# author      : Sergei Chernyahovsky
# Date        : 2022-09-20 18:50
# Language    : Python
# Version     : 3.10
# WebDriver   : Selenium
# Version     : 4
# Title       : Full stack test Python Automation
# description : Utilities Event Listener
# Teacher     : Yoni Flenner
# Site        : [""]
# ----------------------------------------------------------------------------------------

from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class EventListener(AbstractEventListener):
    button_text = None

    def before_navigate_to(self, url, driver):
        print("Before Navigating to", url)

    def after_navigate_to(self, url, driver):
        print("After Navigating to", url)

    def before_navigate_back(self, driver):
        print("Before Navigating Back", driver.current_url)

    def after_navigate_back(self, driver):
        print("After Navigating Back", driver.current_url)

    def before_navigate_forward(self, driver):
        print("Before Navigating Forward", driver.current_url)

    def after_navigate_forward(self, driver):
        print("After Navigating Forward", driver.current_url)

    def before_find(self, by, value, driver):
        print("Before Find Element:", value)

    def after_find(self, by, value, driver):
        print("After Find Element", value)

    def before_change_value_of(self, element, driver):
        if element.tag_name == "input":
            print("Before Change Value ", element.get_attribute("value"))
        else:
            print("Before Change Value ", element.text)

    def after_change_value_of(self, element, driver):
        if element.tag_name == "input":
            print("After Change Value ", element.get_attribute("value"))
        else:
            print("After Change Value ", element.text)

    def before_click(self, element, driver):
        EventListener.button_text = element.get_attribute("value")
        if element.tag_name == "input":
            print("Before Click ", EventListener.button_text)
        else:
            print("Before Click ", EventListener.button_text)

    def after_click(self, element, driver):
        print("After Click ", EventListener.button_text)

    def before_execute_script(self, script, driver):
        print("Before Execute Script ", script)

    def after_execute_script(self, script, driver):
        print("After Execute Script ", script)

    def before_close(self, driver):
        print("Before Closing Tab")

    def after_close(self, driver):
        print("After Closing Tab")

    def before_quit(self, driver):
        print("Before Quiting Session")

    def after_quit(self, driver):
        print("After Quiting Session")

    def on_exception(self, exception, driver):
        print("On Exception: ", exception)
