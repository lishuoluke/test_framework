from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def uninit(self):
        if self.driver:
            self.driver.quit()

    ## This function wait for an element to be visible.
    # @param method The method used to identify the element.
    # @param locator The parameter used together with the method to identify the element.
    # @param timeout The maximum time to wait for the element to be visible.
    # @return success Whether the element is presence.
    def BrowseWebLink(self,link):
        try:
            self.driver.get(link)
            sleep(3)
            return True

        except Exception as ex:
            return False



    def waitElement(self, method, locator, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((method, locator)))
            sleep(1)
            return True

        except Exception as ex:
            return False

    ## This function find an element without waiting for a timeout.
    # @param method The method used to identify the element.
    # @param locator The parameter used together with the method to identify the element.
    # @return element Return the found element.
    def getElementWithoutWait(self, method, locator):
        try:
            if (method == By.ID):
                element = self.driver.find_element_by_id(locator)
            elif (method == By.XPATH):
                element = self.driver.find_element_by_xpath(locator)
            elif (method == By.NAME):
                element = self.driver.find_element_by_name(locator)
            else:
                return None

            return element

        except Exception as ex:
            return None

    ## This function find an element.
    # @param method The method used to identify the element.
    # @param locator The parameter used together with the method to identify the element.
    # @param timeout The maximum time to find the element.
    # @return element Return the found element.
    def getElement(self, method, locator, timeout):
        try:
            if (not self.waitElement(method, locator, timeout)):
                return None

            return self.getElementWithoutWait(method, locator)

        except Exception as ex:
            return None

    ## This function click an element.
    # @param element The element to be clicked.
    # @return success Whether the click is successful.
    def click(self, element):
        try:
            element.click()
            sleep(1)
            return True

        except Exception as ex:
            return False

    ## This function click an element.
    # @param method The method used to identify the element.
    # @param locator The parameter used together with the method to identify the element.
    # @param timeout The maximum time to wait for the element to be clicked.
    # @return success Whether the click is successful.
    def clickElement(self, method, locator, timeout):
        try:
            element = self.getElement(method, locator, timeout)
            if (element == None):
                return False

            return self.click(element)

        except Exception as ex:
            return False

    ## This function set the text of a text element.
    # @param method The method used to identify the element.
    # @param locator The parameter used together with the method to identify the element.
    # @param timeout The maximum time to find the element.
    # @param text The text to be set in the element.
    # @return success Whether the text element is set successfully.
    def setTextElement(self, method, locator, timeout, text):
        try:
            element = self.getElement(method, locator, timeout)
            if (element == None):
                return False

            self.click(element)
            element.clear()
            element.send_keys(text)
            sleep(2)
            return True

        except Exception as ex:
            return False

    ## This function set the text of a password element.
    # @param method The method used to identify the element.
    # @param locator The parameter used together with the method to identify the element.
    # @param timeout The maximum time to find the element.
    # @param text The text to be set in the password element.
    # @return success Whether the password element is set successfully.
    def setPasswordElement(self, method, locator, timeout, password):
        return self.setTextElement(method, locator, timeout, password)

    ## This function wait for a text element to contain text.
    # @param method The method used to identify the element.
    # @param locator The parameter used together with the method to identify the element.
    # @param timeout The maximum time to wait for the element to contain text.
    # @return success Whether the element contain some text.
    def waitElementToContainText(self, method, locator, timeout):
        try:
            element = self.getElement(method, locator, timeout)
            if (element == None):
                return False

            for second in range(timeout):
                if (element.text != ''):
                    return True
                sleep(1)

        except Exception as ex:
            return False
