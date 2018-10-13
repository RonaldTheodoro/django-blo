from django.test import TestCase
from django.urls import reverse


class TestPostDelete(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('posts:delete'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'posts/delete.html')
