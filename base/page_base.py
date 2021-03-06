from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BaseClass(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def presence_for_element(self, selector):
        """
        Presence for element to present
        :param selector: locator of the element to find

        """
        return self.wait.until(ec.presence_of_element_located(selector))

    def presence_for_all_elements(self, selector):
        """
        Presence for all elements to present
        :param selector: locator of the elements to find

        """
        return self.wait.until(ec.presence_of_all_elements_located(selector))

    def send_keys(self, selector, text):
        """
        Writes the text in the parameter to the element
        :param selector: locator of the elements to find
        :param text: text to write to element

        """
        self.presence_for_element(selector).send_keys(text)

    def move_to_element(self, selector):
        """
        Hover the specified element
        :param selector: locator of the elements to find

        """
        self.actions.move_to_element(self.presence_for_element(selector)).perform()
