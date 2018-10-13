from django.test import TestCase
from django.urls import reverse


class TestPostDetail(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('posts:detail'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'posts/detail.html')
