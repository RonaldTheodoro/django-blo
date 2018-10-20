from django.urls import reverse

from .. import models
from .base_test import BaseTest


class TestPostDetail(BaseTest):

    def setUp(self):
        super(TestPostDetail, self).setUp()
        self.response = self.client.get(
            reverse('posts:detail', kwargs={'slug': self.data['title']})
        )

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'posts/detail.html')
