"""
Class containing functions specific to the Home page.
"""


from pages.basePage import BasePage
from locators import locators
from selenium.webdriver.support import expected_conditions as ec

class HomePage(BasePage):
    def __init__(self, driver):
        """
        constructor

        """

        super().__init__(driver)

    def hover_company(self):
        self.hover(locators.HomePageLocators.COMPANY_BUTTON)

    def click_careers(self):
        """
        Switches to the sign_in page
        """
        self.click_element(locators.HomePageLocators.CAREERS_BUTTON)