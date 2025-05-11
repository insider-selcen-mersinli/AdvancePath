"""
Base class containing setUp and tearDown functions common to each test.

"""

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.basePage import BasePage
from pages.careersPage import CareersPage
from pages.homePage import HomePage
from pages.leverApplicationFormPage import LeverApplicationFormPage
from pages.qualityAssuranceCareersPage import QualityAssuranceCareersPage



class BaseTest(unittest.TestCase):
    def setUp(self):
        """
        Basic preparations before the test starts

        """

        """
        chrome_options = webdriver.ChromeOptions()
        option.add_argument('--start-maximized')
        option.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

        self.driver.get("https://useinsider.com/")

        self.base = BasePage(self.driver)
        self.home = HomePage(self.driver)
        self.careers = CareersPage(self.base)
        self.lever = LeverApplicationFormPage(self.base)
        self.qa = QualityAssuranceCareersPage(self.base)

    def tearDown(self):
        """
        Closing procedures at the end of the test

        """

        self.driver.quit()