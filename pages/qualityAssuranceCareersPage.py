from pages.basePage import BasePage
from locators import locators
from selenium.webdriver.support import expected_conditions as ec

class QualityAssuranceCareersPage(BasePage):
    def __init__(self, driver):
        """
        constructor

        """

        super().__init__(driver)

    def clicked_see_all_qa_jobs(self):
        self.click_element(locators.QualityAssuranceCareersPage.SEE_ALL_QA_JOBS_BUTTON)

    def filter_location(self):
        self.click_element(locators.QualityAssuranceCareersPage.FILTER_BY_LOCATION)
        self.click_element(locators.QualityAssuranceCareersPage.ISTANBUL_TURKEY)

    def filter_department(self):
        self.click_element(locators.QualityAssuranceCareersPage.FILTER_BY_DEPARTMENT)
        self.click_element(locators.QualityAssuranceCareersPage.QUALITY_ASSURANCE)

    def displayed_job_listing(self):
        return self.displayed(locators.QualityAssuranceCareersPage.JOB_LISTING)

    def get_job_location(self):
        job_location = self.find_element(*locators.QualityAssuranceCareersPage.JOB_ONE_LOCATION).text
        return job_location

    def get_job_department(self):
        job_department = self.find_element(*locators.QualityAssuranceCareersPage.JOB_ONE_DEPARTMENT).text
        return job_department

    def clicked_view_role(self):
        self.click_element(locators.QualityAssuranceCareersPage.JOB_ONE_VIEW_ROLE_BUTTON)