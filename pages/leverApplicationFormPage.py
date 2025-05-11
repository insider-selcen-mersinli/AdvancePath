from pages.basePage import BasePage
from locators import locators
from selenium.webdriver.support import expected_conditions as ec

class LeverApplicationFormPage(BasePage):
    def __init__(self, driver):
        """
        constructor

        """

        super().__init__(driver)

    def displayed_apply_for_this_job(self):
        return self.displayed(locators.LeverApplicationFormPage.APPLY_FOR_THIS_JOB)