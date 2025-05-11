"""
This class is the class where the tests are run.

"""

from tests.baseTest import BaseTest


class TestInsider(BaseTest):

    def test(self):
        self.home.hover_company()
        self.home.click_careers()

        self.assertTrue(self.careers.displayed_locations(),"Location is not accessible")
        self.assertTrue(self.careers.displayed_teams(),"Teams is not accessible")
        self.assertTrue(self.careers.displayed_life_at_insider(),"Life at Insider is not accessible")
        self.careers.clicked_see_all_teams()
        self.careers.clicked_quality_assurance()

        self.qa.clicked_see_all_qa_jobs()
        self.qa.filter_location()
        self.qa.filter_department()
        self.assertTrue(self.qa.displayed_job_listing(), "The jobs were not listed")
        self.assertEqual(self.qa.get_job_location(), "Istanbul, Turkiye", "Filtering process is incorrect.")
        self.assertEqual(self.qa.get_job_department(), "Quality Assurance", "Filtering process is incorrect.")
        self.qa.clicked_view_role()

        self.assertTrue(self.lever.displayed_apply_for_this_job(), "The redirect did not work or it worked incorrectly")
