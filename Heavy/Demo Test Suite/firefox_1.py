import os
import time
import log_test_message as log
from appium import webdriver
from python_script_base import PythonScriptBase
from selenium.webdriver.common.by import By
from selenium import webdriver
import selenium_helper as helper




class TestScript(PythonScriptBase):
    def __init__(self):
        super(TestScript, self).__init__(__file__)

    def initialise(self):
        try:
            log.logFnEntryExit(__file__, 'initialise', 'begin')

            self.driver = webdriver.Firefox()

            log.logFnEntryExit(__file__, 'initialise', 'end')
            return True

        except Exception as ex:
            log.logException(__file__, 'initialise', ex)
            self.statusId = 5
            return False

    def uninitialise(self):
        try:
            log.logFnEntryExit(__file__, 'uninitialise', 'begin')

            # Remove pre-conditions.
            # Scan logs for unexpected errors.
            # Set the test result (statusId) and comments.
            # statusId:
            # 1 = passed, 2 = blocked, 3 = untested, 4 = retest, 5 = failed.
            self.driver.quit()

            log.logFnEntryExit(__file__, 'uninitialise', 'end')

        except Exception as ex:
            log.logException(__file__, 'uninitialise', ex)

    def execute(self):
        try:
            log.logFnEntryExit(__file__, 'execute', 'begin')
            if (not helper.SeleniumHelper.BrowseWebLink(self,'http://google.com/')):
                raise Exception('Fail browse to google')
            log.logProgress(__file__, 'main', 'successfully go to google')

        except Exception as ex:
            log.logException(__file__, 'execute', ex)
            self.statusId = 5




if (__name__ == '__main__'):
    testScript = TestScript()
    testScript.main()
