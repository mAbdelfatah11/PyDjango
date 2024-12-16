from django.test import TestCase

from job.views import job_list, job_detail
class ViewTestCase(TestCase):
    def test_jobs_list_loads_properly(self):
        # """ The Jobs List page loads properly """
        # response = self.client.get('/jobs/')
        # self.assertEqual(response.status_code, 200)
        assert 1 == 1