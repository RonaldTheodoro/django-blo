from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from .. import forms, models


class TestPostEdit(TestCase):

    def setUp(self):
        self.post = models.Post.objects.create(
            title='title',
            content='content'
        )
        self.response = self.client.get(
            reverse('posts:edit', kwargs={'pk': self.post.pk})
        )
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
            ('<input', 3),
            ('type="text"', 1),
            ('type="submit"', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)


class TestPostEditPost(TestCase):

    def setUp(self):
        data = {'title': 'title', 'content': 'content'}
        self.client.post(reverse('posts:create'), data)
        self.response = self.client.post(
            reverse('posts:edit', kwargs={'pk': 1}),
            data
        )

    def test_post(self):
        self.assertRedirects(
            self.response,
            reverse('posts:detail', kwargs={'pk': 1})
        )

    def test_messages(self):
        messages = list(get_messages(self.response.wsgi_request))
        self.assertEqual(2, len(messages))
        self.assertEqual('Successfully Created', str(messages[0]))
        self.assertEqual('Successfully Updated', str(messages[1]))

    def test_save_subscription(self):
        self.assertTrue(models.Post.objects.exists())
