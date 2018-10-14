from django.test import TestCase
from django.urls import reverse


class TestPostUpdate(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('posts:edit'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'posts/edit.html')
