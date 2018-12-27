from time import sleep

import nidaqmx
from nidaqmx.constants import LineGrouping

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



def waitElement(driver, method, locator, timeout):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((method, locator)))
        sleep(1)
        return True

    except Exception as ex:
        return False


def getElementWithoutWait(driver, method, locator):
    try:
        if (method == By.ID):
            element = driver.find_element_by_id(locator)
        else:
            element = driver.find_element_by_xpath(locator)
        return element

    except Exception as ex:
        return None


def getElement(driver, method, locator, timeout):
    try:
        if (not waitElement(driver, method, locator, timeout)):
            return None

        return getElementWithoutWait(driver, method, locator)

    except Exception as ex:
        return None


def waitElementToDisappear(driver, method, locator, timeout):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        for second in range(timeout):
            if (not element.is_displayed()):
                return True
            sleep(1)
            print('waiting for it to disappear..')

        return False

    except Exception as ex:
        return False


def waitElementToContainText(driver, method, locator, timeout):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        for second in range(timeout):
            if (element.text != ''):
                return True
            sleep(1)
            print('waiting for it to contain some text..')

    except Exception as ex:
        return False

def waitElementContentChanged(driver, method, locator, timeout):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        originalText = element.text

        for second in range(timeout):
            if (element.text != originalText):
                return True
            sleep(1)
            print('waiting for content changed..')

        return False

    except Exception as ex:
        return False


def click(element):
    element.click()
    sleep(1)


def swipe(driver, x1, y1, x2, y2):
    driver.swipe(x1, y1, x2, y2)
    sleep(1)


def clickElement(driver, method, locator, timeout):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        click(element)
        return True

    except Exception as ex:
        return False


def clickElementAndWaitContentChanged(driver, method, locator, content, timeout):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        content = getElement(driver, method, content, timeout)
        if (content == None):
            return False

        originalText = content.text
        click(element)

        for second in range(timeout):
            if (content.text != originalText):
                return True
            sleep(1)
            print('waiting for content changed..')

        return False

    except Exception as ex:
        return False

def setTextElement(driver, method, locator, timeout, text):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        element.set_text(text)

        for second in range(timeout):
            if (element.text == text):
                return True
            sleep(1)
            print('waiting for text to take effect..')

        return False

    except Exception as ex:
        return False


def setPasswordElement(driver, method, locator, timeout, password):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        element.set_text(password)
        sleep(2)
        return True

    except Exception as ex:
        return False


def uncheckElement(driver, method, locator, timeout):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        if (element.is_selected()):
            click(element)

        return True

    except Exception as ex:
        return False


def swipeUp(driver, method, locator, percent, timeout):
    try:
        container = getElement(driver, method, locator, timeout)
        if (container == None):
            return False

        x = container.location['x'] + (container.size['width'] / 2)
        y1 = container.location['y'] + container.size['height'] - 10
        y2 = container.location['y'] + 10
        amount = y1 - y2
        y2 = int(y1 - (amount * percent) / 100)
        swipe(driver, x, y1, x, y2)
        return True

    except Exception as ex:
        return False


def swipeLeft(driver, method, locator, percent, timeout):
    try:
        container = getElement(driver, method, locator, timeout)
        if (container == None):
            return False

        x1 = container.location['x'] + container.size['width'] - 10
        x2 = container.location['x'] + 10
        y = container.location['y'] + (container.size['height'] / 2)
        amount = x1 - x2
        x2 = int(x1 - (amount * percent) / 100)
        swipe(driver, x1, y, x2, y)
        return True

    except Exception as ex:
        return False


def swipeUpAndClickElement(driver, container, className, target, tries):
    try:
        for x in range(tries):
            print('try ' + str(x))
            elements = driver.find_elements_by_class_name(className)
            for index in range(len(elements) - 1):
                if (elements[index].text == target):
                    click(elements[index])
                    return True
            swipeUp(driver, By.ID, container, 20, 10)
        return False

    except Exception as ex:
        return False

def PressPowerButton (portAndline):
    try:
        task123 = nidaqmx.task.Task()
        task123.do_channels.add_do_chan(portAndline, 'line',line_grouping=LineGrouping.CHAN_PER_LINE)
        task123.write(True)
        sleep(2)
        task123.write(False)

        task123.stop()
        task123.close()
        return True

    except Exception as ex:
        return False

