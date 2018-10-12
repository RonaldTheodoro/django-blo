from django.db import models


class Post(models.Model):
    title = models.CharField('title', max_length=120)
    content = models.TextField('content')
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

    def __str__(self):
        return self.title
