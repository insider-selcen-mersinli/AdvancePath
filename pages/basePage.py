from selenium.common import MoveTargetOutOfBoundsException
from selenium.webdriver.common.by import By

from locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time

class BasePage:

    def __init__(self, driver):
        """
        Constructor
        """

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.action = ActionChains(self.driver)

    def click_element(self, by_locator):
        """
        Click function
        Performs a click operation on the selected element.
        """

        self.wait.until(ec.presence_of_element_located(by_locator)).click()

    def find_element(self, *locator):
        """
        This function allows finding the element whose locator information is given.
        """

        return self.driver.find_element(*locator)

    def send_text(self, text, *by_locator):
        """
        It is used to send login information to elements that can receive input.
        """

        self.find_element(*by_locator).send_keys(text)

    def displayed(self, by_locator):
        """
        This function controls the display of the element whose locator information is given.
        """

        return self.wait.until(ec.presence_of_element_located(by_locator)).is_displayed()

    def hover(self, by_locator):
        self.action.move_to_element(self.driver.find_element(By.XPATH, '/html/body/nav/div[2]/div/ul[1]/li[6]/a')).perform()
        time.sleep(0.5)

    def scroll_page(self, locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        self.action.scroll_to_element(element).perform()

