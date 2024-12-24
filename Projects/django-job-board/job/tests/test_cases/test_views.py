
from django.test import TestCase
from django.urls import reverse

class ViewTestCase(TestCase):   # inherite from TestCase class

    def test_jobs_list_loads_properly(self):
        """ The Jobs List page loads properly """
        response = self.client.get('/jobs/')        # test directly using path url
        self.assertEqual(response.status_code, 200)

    def test_job_list_path(self):
        """ test job list view """
        response = self.client.get(reverse('jobs:job_list'))  # Use the namespace
        self.assertEqual(response.status_code, 200)
