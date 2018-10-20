from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from .base_test import BaseTest
from .. import forms, models


class TestPostCreate(BaseTest):

    def setUp(self):
        super(TestPostCreate, self).setUp()
        self.response = self.client.get(reverse('posts:create'))
        self.form = self.response.context['form']

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'posts/form.html')

    def test_has_form(self):
        self.assertIsInstance(self.form, forms.PostForm)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_html(self):
        tags = (
            ('<form', 1),
            ('<input', 4),
            ('type="text"', 1),
            ('type="submit"', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)


class TestPostCreateNew(BaseTest):

    def test_post(self):
        self.assertRedirects(
            self.response,
            reverse('posts:detail', kwargs={'slug': self.data['title']})
        )

    def test_messages(self):
        messages = list(get_messages(self.response.wsgi_request))
        self.assertEqual(1, len(messages))
        self.assertEqual('Successfully Created', str(messages[0]))

    def test_save_post(self):
        self.assertTrue(models.Post.objects.exists())


class TestPostCreateInvalid(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client.login(username='user', password='12345')
        self.response = self.client.post(reverse('posts:create'), {})
        self.form = self.response.context['form']

    def test_post(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'posts/form.html')

    def test_has_form(self):
        self.assertIsInstance(self.form, forms.PostForm)

    def test_form_has_errors(self):
        self.assertTrue(self.form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(models.Post.objects.exists())
