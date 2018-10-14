import hashlib
import os
from datetime import datetime


def upload_file_path(instance, filename):
    basename = os.path.basename(filename)
    name, ext = os.path.splitext(basename)
    name = hashlib.md5(name.encode()).hexdigest()
    date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return f'{instance.id}/{date}-{name}{ext}'
