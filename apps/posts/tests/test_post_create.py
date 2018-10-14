from django.test import TestCase
from django.urls import reverse

from .. import forms


class TestPostCreate(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('posts:create'))
        self.form = self.response.context['form']

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'posts/create.html')

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
