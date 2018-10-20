from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from .. import models


class TestPostDelete(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        data = {'title': 'title', 'content': 'content', 'user_id': 1}
        self.client.login(username='user', password='12345')
        self.client.post(reverse('posts:create'), data)
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
