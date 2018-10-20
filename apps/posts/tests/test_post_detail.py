from django.test import TestCase
from django.urls import reverse

from .. import models


class TestPostDetail(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client.login(username='user', password='12345')
        self.post = models.Post.objects.create(
            title='title',
            content='content',
            user_id=1
        )
        self.response = self.client.get(
            reverse('posts:detail', kwargs={'slug': self.post.slug})
        )

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'posts/detail.html')
