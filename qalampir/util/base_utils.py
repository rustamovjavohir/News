from time import time_ns
from uuid import uuid4

from django.views.decorators.http import require_http_methods

from news.models import Uploads
from qalampir.settings import MEDIA_ROOT, join_path

require_DELETE = require_http_methods(["DELETE"])


def media_path(file_name):
    return f'/media/uploads/{file_name}'


def process_name(code: str, extension: str):
    return f"{code}.{extension}"


def get_extension(file_name: str):
    return file_name.split(".")[-1]


def unique_code():
    return "%s%s" % (time_ns(), str(uuid4()).replace("-", ""))


def save_file(file):
    code = unique_code()
    new_name = process_name(code, get_extension(file.name))
    for chunk in file.chunks():
        with open(join_path(MEDIA_ROOT, 'uploads', new_name), mode="wb+") as write_file:
            write_file.write(chunk)

    instance = Uploads()
    instance.code = code
    instance.original_name = file.name
    instance.path = media_path(new_name)
    instance.size = file.size
    instance.content_type = file.content_type
    instance.new_name = new_name
    instance.save()
    return instance


def upload_file(file) -> Uploads:
    instance = Uploads()
    code = unique_code()
    new_name = process_name(code, get_extension(file.name))
    instance.code = code
    instance.original_name = file.name
    instance.path = media_path(new_name)
    instance.size = file.size
    instance.content_type = file.content_type
    instance.new_name = new_name
    instance.save()
    return instance
