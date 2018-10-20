from django.contrib.messages import get_messages
from django.urls import reverse

from .. import forms, models
from .base_test import BaseTest

class TestPostEdit(BaseTest):

    def setUp(self):
        super(TestPostEdit, self).setUp()
        self.response = self.client.get(
            reverse('posts:edit', kwargs={'slug': self.data['title']})
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
            ('<input', 4),
            ('type="text"', 1),
            ('type="submit"', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)


class TestPostEditPost(BaseTest):

    def setUp(self):
        super(TestPostEditPost, self).setUp()
        self.response = self.client.post(
            reverse('posts:edit', kwargs={'slug': self.data['title']}),
            self.data
        )

    def test_post(self):
        self.assertRedirects(
            self.response,
            reverse('posts:detail', kwargs={'slug': 'title'})
        )

    def test_messages(self):
        messages = list(get_messages(self.response.wsgi_request))
        self.assertEqual(2, len(messages))
        self.assertEqual('Successfully Created', str(messages[0]))
        self.assertEqual('The post has been saved', str(messages[1]))

    def test_save_subscription(self):
        self.assertTrue(models.Post.objects.exists())
