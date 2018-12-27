import os
import time
from subprocess import Popen

import appium_helper as appHelp
import dyson_link_helper as dysonlinkhelp
import log_test_message as log
from appium import webdriver
from python_script_base import PythonScriptBase
from selenium.webdriver.common.by import By

from dyson_link_config import DysonLinkConfig
import nidaq_helper as nidaq


class TestScript(PythonScriptBase):
    def __init__(self):
        super(TestScript, self).__init__(__file__)

    def initialise(self):
        try:
            log.logFnEntryExit(__file__, 'initialise', 'begin')

            self.config = DysonLinkConfig()

            # autoGrantPermissions works for Appium server v1.7.1.
            desired_caps = {'platformName': self.config.platformName,
                            'platformVersion': self.config.platformVersion,
                            'deviceName': self.config.deviceName,
                            'app': 'C:\\Users\\sli\\PycharmProjects\\Appium\\WifiManager\\WiFi Manager.apk',
                            'appPackage': 'org.kman.WifiManager',
                            # 'appActivity': dysonLinkConfig.appActivity,
                            # 'optionalIntentArguments': dysonLinkConfig.optionalIntentArguments,
                            # 'autoGrantPermissions': True
                            'noReset': True,
                            }
            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.setWIFI = '520_IT_Mi3'

            if (not appHelp.swipeUpAndClickElement(driver, 'decor_content_parent', 'android.widget.TextView',
                                                        self.setWIFI,
                                                        6)):
                log.logProgress(__file__, 'Main', 'Failed at clickElement - '+ self.setWIFI)
                return False

            if (not appHelp.waitElement(driver, By.ID, 'button1', 10)):
                log.logProgress(__file__, 'Main', 'Failed at clickElement - confirm button')
                return False
            try:
                WIFI_confirm = driver.find_element_by_id('button1')
                if (WIFI_confirm.text == 'CONNECT'):
                    appHelp.clickElement(driver, By.ID, 'button1', 10)
                else:
                    appHelp.clickElement(driver, By.ID, 'button2', 10)
            except Exception as ex:
                log.logException(__file__, 'initialise', ex)

            time.sleep(10)
            log.logProgress(__file__, 'main', self.setWIFI + ' is selected')
            driver.quit()

            self.config = DysonLinkConfig()

            # autoGrantPermissions works for Appium server v1.7.1.
            desired_caps = {'platformName': self.config.platformName,
                            'platformVersion': self.config.platformVersion,
                            'deviceName': self.config.deviceName,
                            'app': self.config.app,
                            'appPackage': self.config.appPackage,
                            'appActivity': self.config.appActivity,
                            'optionalIntentArguments': self.config.optionalIntentArguments,
                            'autoGrantPermissions': True,
                            'noReset': True
                            }
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)




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

            #no need log in if not reset app

            # Remove the machine if it is already there
            if appHelp.waitElement(self.driver,By.ID,'settings_imagebutton',10):
                dysonlinkhelp.RemoveMachine(self.driver)
                log.logProgress(__file__, 'main', 'remove machine before journey')
            time.sleep(3)

            if (not appHelp.clickElement(self.driver, By.ID, 'navigation_menu_button', 10)):
                raise Exception('Failed at clickElement - navigation_menu_button')
            log.logProgress(__file__, 'main', 'after navigation_menu_button')

            # new action: check version and print out before proceed with connection journey
            if (not appHelp.clickElement(self.driver,By.XPATH,"//android.widget.TextView [@text ='About the Dyson Link app']",30)):
                raise Exception('Failed at clickElement - About the dyson link app')
            log.logProgress(__file__, 'main', 'Press the version tag')
            if (not appHelp.waitElement(self.driver,By.ID,'version_text',10)):
                raise Exception('Failed at clickElement - About the dyson link app')
            log.logProgress(__file__, 'main', 'version shown')
            try:
                version = self.driver.find_element_by_id('version_text').text
                longtext = 'App version is ' + version
            except:
                raise Exception('Failed at get the software version')

            log.logProgress(__file__, 'main', longtext)
            if (not appHelp.clickElement(self.driver, By.ID, 'close_button', 10)):
                raise Exception('Failed at clickElement - close button')
            log.logProgress(__file__, 'main', 'after close button')
            #End of version checking


            if (not appHelp.clickElement(self.driver, By.ID, 'add_machine_button', 60)):
                raise Exception('Failed at clickElement - add_machine_button')
            log.logProgress(__file__, 'main', 'after add_machine_button')
            if (not appHelp.clickElementAndWaitContentChanged(self.driver, By.ID, 'next_button', 'title_label', 10)):
                raise Exception('Failed at clickElement - next_button')
            log.logProgress(__file__, 'main', 'after next_button')
            if (not appHelp.clickElementAndWaitContentChanged(self.driver, By.ID, 'next_button', 'title_label', 10)):
                raise Exception('Failed at clickElement - next_button')
            log.logProgress(__file__, 'main', 'after next_button')
            if (not appHelp.clickElement(self.driver, By.ID, 'next_button', 10)):
                raise Exception('Failed at clickElement - next_button')
            log.logProgress(__file__, 'main', 'after next_button')
            if (not appHelp.waitElementToDisappear(self.driver, By.ID, 'spinner', 10)):
                raise Exception('Failed at waitElementToDisappear - spinner')
            log.logProgress(__file__, 'main', 'after spinner disappear')
            if (not self.clickMachineElement(self.config.prefix, self.config.machine_serial, 20)):
                raise Exception('Failed at clickMachineElement')
            log.logProgress(__file__, 'main', 'after machine selected')

            if (not appHelp.waitElementContentChanged(self.driver, By.ID, 'instruction_label', 30)):
                raise Exception('Failed at waiting for the machine')
            log.logProgress(__file__, 'main', 'after waiting for machine')

            time.sleep(5)
            if(not nidaq.PressPowerButton(self.config.port)):
                raise Exception('Failed at press powerbutton')
            log.logProgress(__file__, 'main', 'after pressing the button')

            if (not appHelp.clickElement(self.driver, By.ID, 'next_button', 120)):
                raise Exception('Failed at clickElement - next_button')
            #Check whether selected wifi is used
            try:
                realWIFI = self.driver.find_element_by_id('home_network_button').text
                print('WIFI used is '+realWIFI)
            except:
                raise Exception('cannot get the selected WIFI name')
            if (realWIFI != self.setWIFI):
                raise Exception('Wrong WIFI is selected '+ realWIFI)
            log.logProgress(__file__, 'main', 'Correct WIFI is selcted')
            #End of new code
            log.logProgress(__file__, 'main', 'after next_button')
            if (not appHelp.setPasswordElement(self.driver, By.ID, 'textinput_left', 10, self.config.WIFI_password)):
                raise Exception('Failed at setPasswordElement - textinput_left')
            log.logProgress(__file__, 'main', 'after WIFI_password')
            if (not appHelp.clickElement(self.driver, By.ID, 'next_button', 10)):
                raise Exception('Failed at clickElement - next_button')
            log.logProgress(__file__, 'main', 'after next_button')
            if (not appHelp.clickElement(self.driver, By.ID, 'bottom_button', 300)):
                raise Exception('Failed at clickElement - first confirm button')
            log.logProgress(__file__, 'main', 'after confirm button - check here')
            if (not appHelp.clickElement(self.driver, By.ID, 'bottom_button', 10)):
                raise Exception('Failed at clickElement - second confirm button')
            log.logProgress(__file__, 'main', 'after the second confirm button')
            if (not appHelp.clickElement(self.driver, By.ID, 'bottom_button', 10)):
                raise Exception('Failed at clickElement - third confirm button')
            log.logProgress(__file__, 'main', 'after the third confirm button')
            if (not appHelp.waitElement(self.driver, By.ID, 'settings_imagebutton', 300)):
                raise Exception('Failed at waitElement - settings_imagebutton')
            log.logProgress(__file__, 'main', 'Machine is connected')

            try:
                dysonlinkhelp.RemoveMachine(self.driver)
            except:
                raise Exception('Failed remove machine after connected')
            log.logProgress(__file__, 'main', 'Connection Journey is completed! - success')

        except Exception as ex:
            log.logException(__file__, 'execute', ex)
            self.statusId = 5

    def clickMachineElement(self, prefix, machineSerial, tries):
        try:
            for x in range(tries):
                print('try ' + str(x))
                elements = self.driver.find_elements_by_class_name('android.widget.TextView')
                for index in range(len(elements) - 1):
                    if (elements[index].text.startswith(prefix) and elements[index + 1].text == machineSerial):
                        appHelp.click(elements[index + 1])
                        return True

                appHelp.swipeUp(self.driver, By.ID, 'machine_list', 20, 10)
            return False

        except Exception as ex:
            return False


if (__name__ == '__main__'):
    testScript = TestScript()
    testScript.main()
