from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # create an HttpRequest object
        request = HttpRequest()
        # pass object into the home_page view which returns an instance
        # of an HttpResponse object
        response = home_page(request)
        # response.content is raw bytes not a Python string
        # so the b'' syntaxis used to compare them
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
