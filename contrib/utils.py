import hashlib
import os
from datetime import datetime

from django.utils.text import slugify


def upload_file_path(instance, filename):
    basename = os.path.basename(filename)
    name, ext = os.path.splitext(basename)
    name = hashlib.md5(name.encode()).hexdigest()
    date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return f'{instance.id}/{date}-{name}{ext}'


def get_unique_slug(instance, field_name, slug_field_name):
    slug = slugify(getattr(instance, field_name))
    unique_slug = slug
    extension = 1
    ModelClass = instance.__class__

    while ModelClass._default_manager.filter(
        **{slug_field_name: unique_slug}
    ).exists():
        unique_slug = f'{slug}-{extension}'
        extension += 1

    return unique_slug
