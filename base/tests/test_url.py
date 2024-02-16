from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from base.models import AdminNotice

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from base.models import AdminNotice  # Replace 'yourapp' with the actual name of your Django app

class UrlsTestCase(TestCase):
    """
    Test case for the URL patterns and views in your Django application.

    This test case covers various views such as 'common_page', 'home',
    'create_notice', and 'notice_details'.
    """

    def setUp(self):
        """
        Set up necessary data for the test case.
        """
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.notice = AdminNotice.objects.create(
           
            # Add any other required fields
        )
        # Create a sample AdminNotice object
        #

    def test_common_page_view(self):
        """
        Test the 'common_page' view.

        This test checks if the 'common_page' view returns a status code of 200.
        Additional assertions can be added based on the behavior of the view.
        """
        response = self.client.get(reverse('common_page'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the behavior of your common_page view

    def test_home_view(self):
        """
        Test the 'home' view.

        This test logs in the test user and checks if the 'home' view returns a status code of 200.
        Additional assertions can be added based on the behavior of the view.
        """
        # Login the test user before accessing the home view
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the behavior of your home view

    def test_create_notice_view(self):
        """
        Test the 'create_notice' view.

        This test logs in the test user and checks if the 'create_notice' view returns a status code of 200.
        Additional assertions can be added based on the behavior of the view.
        """
        # Login the test user before accessing the create_notice view
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_notice'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the behavior of your create_notice view

    def test_notice_details_view(self):
        """
        Test the 'notice_details' view.

        This test checks if the 'notice_details' view returns a status code of 200.
        Additional assertions can be added based on the behavior of the view.
        """
        response = self.client.get(reverse('notice_details', args=[str(self.notice.pk)]))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the behavior of your notice_details view

