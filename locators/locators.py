
from selenium.webdriver.common.by import By

class HomePageLocators:
    COMPANY_BUTTON = (By.ID, 'navbarDropdownMenuLink')
    CAREERS_BUTTON = (By.CSS_SELECTOR, "#navbarNavDropdown > ul:nth-child(1) > li:nth-child(6) > div > div.new-menu-dropdown-layout-6-mid-container > a:nth-child(2)")

class CareersPageLocators:
    LOCATION_AREA = (By.ID, 'career-our-location')
    TEAMS_AREA = (By.ID, 'career-find-our-calling')
    LIFE_AT_INSIDER_AREA = (By.CSS_SELECTOR, '.e-swiper-container')
    SEE_ALL_TEAMS_BUTTON = (By.CSS_SELECTOR, '.btn.btn-outline-secondary')
    QUALITY_ASSURANCE_BUTTON = (By.CSS_SELECTOR, '#career-find-our-calling > div > div > div.col-12.d-flex.flex-wrap.p-0.career-load-more > div:nth-child(23) > div.job-title.mt-0.mt-lg-2.mt-xl-5')

class QualityAssuranceCareersPage:
    SEE_ALL_QA_JOBS_BUTTON = (By.CSS_SELECTOR, ".btn.btn-outline-secondary")
    FILTER_BY_LOCATION = (By.ID, 'select2-filter-by-location-container')
    ISTANBUL_TURKEY = (By.ID, 'select2-filter-by-location-result-h1ns-Istanbul, Turkiye')
    FILTER_BY_DEPARTMENT = (By.ID, 'select2-filter-by-department-container')
    QUALITY_ASSURANCE = (By.ID, 'select2-filter-by-department-result-4ahi-Quality Assurance')
    JOB_LISTING = (By.CSS_SELECTOR, '.flex-column.flex-lg-row')
    JOB_ONE = (By.CSS_SELECTOR, '#jobs-list > div:nth-child(1) > div')
    JOB_ONE_DEPARTMENT = (By.CSS_SELECTOR, "#jobs-list > div:nth-child(1) > div > span")
    JOB_ONE_LOCATION = (By.CSS_SELECTOR, "#jobs-list > div:nth-child(1) > div > div")
    JOB_ONE_VIEW_ROLE_BUTTON = (By.CSS_SELECTOR, '#jobs-list > div:nth-child(1) > div > a')

class LeverApplicationFormPage:
    APPLY_FOR_THIS_JOB = (By.CSS_SELECTOR, 'body > div.content-wrapper.posting-page > div > div.section-wrapper.accent-section.page-full-width > div > div.postings-btn-wrapper > a')
