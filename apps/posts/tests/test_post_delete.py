from django.contrib.messages import get_messages
from django.urls import reverse

from .. import models
from .base_test import BaseTest


class TestPostDelete(BaseTest):

    def setUp(self):
        super(TestPostDelete, self).setUp()
        self.response = self.client.get(
            reverse('posts:delete', kwargs={'slug': 'title'})
        )

    def test_get(self):
        self.assertRedirects(self.response, reverse('posts:index'))

    def test_deleted_post(self):
        self.assertFalse(models.Post.objects.exists())

    def test_messages(self):
        messages = list(get_messages(self.response.wsgi_request))
        self.assertEqual(2, len(messages))
        self.assertEqual('Successfully Created', str(messages[0]))
        self.assertEqual('The post has been deleted', str(messages[1]))
