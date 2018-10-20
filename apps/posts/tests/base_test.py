from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class BaseTest(TestCase):

    def setUp(self):
        self.username = 'user'
        self.password = '12345'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            is_staff=True
        )
        self.data = {
            'title': 'title',
            'content': 'content',
            'user': self.user
        }
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(reverse('posts:create'), self.data)
