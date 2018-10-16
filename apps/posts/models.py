from django.db import models
from django.urls import reverse

from contrib import utils

class Post(models.Model):
    title = models.CharField('title', max_length=120)
    content = models.TextField('content')
    slug = models.SlugField('slug', unique=True)
    image = models.ImageField(
        'image',
        upload_to=utils.upload_file_path,
        null=True,
        blank=True
    )
    updated = models.DateTimeField(
        'updated',
        auto_now=True,
        auto_now_add=False
    )
    timestamp = models.DateTimeField(
        'timestamp',
        auto_now=False,
        auto_now_add=True
    )

    class Meta:
        ordering = ['-timestamp', '-updated']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = utils.get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.pk})
