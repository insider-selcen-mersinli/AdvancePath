"""
Class containing functions specific to the Careers page.
"""


from pages.basePage import BasePage
from locators import locators
from selenium.webdriver.support import expected_conditions as ec

class CareersPage(BasePage):
    def __init__(self, driver):
        """
        constructor

        """

        super().__init__(driver)

    def displayed_locations(self):
        return self.displayed(locators.CareersPageLocators.LOCATION_AREA)

    def displayed_teams(self):
        return self.displayed(locators.CareersPageLocators.TEAMS_AREA)

    def displayed_life_at_insider(self):
        return self.displayed(locators.CareersPageLocators.LIFE_AT_INSIDER_AREA)

    def clicked_see_all_teams(self):
        self.scroll_page(locators.CareersPageLocators.SEE_ALL_TEAMS_BUTTON)
        self.click_element(locators.CareersPageLocators.SEE_ALL_TEAMS_BUTTON)

    def clicked_quality_assurance(self):
        self.click_element(locators.CareersPageLocators.QUALITY_ASSURANCE_BUTTON)