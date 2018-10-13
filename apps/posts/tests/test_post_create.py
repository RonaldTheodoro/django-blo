from django.test import TestCase
from django.urls import reverse


class TestPostCreate(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('posts:create'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'posts/create.html')
