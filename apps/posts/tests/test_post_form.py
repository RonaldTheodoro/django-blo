from django.test import TestCase

from .. import forms


class TestPostForm(TestCase):

    def test_has_form_fields(self):
        fields = ['title', 'content']
        form = forms.PostForm()
        self.assertSequenceEqual(fields, list(form.fields))
