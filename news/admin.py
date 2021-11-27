from django.contrib import admin

# Register your models here.
from news.models import (
    News,
    Like,
    Comment)

admin.site.register(News)
admin.site.register(Like)
admin.site.register(Comment)
