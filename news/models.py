from ckeditor import fields
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Auditable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="+")
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class News(Auditable):
    title = models.CharField(max_length=200)
    overview = RichTextUploadingField()
    body = RichTextUploadingField()
    image = models.OneToOneField('Uploads', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'news'
        verbose_name = "news"


class Like(Auditable):
    liked = models.BooleanField(default=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'
        verbose_name = "likes"


class Comment(Auditable):
    comment = models.CharField(max_length=200)
    news = models.ForeignKey(News, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'comments'
        verbose_name = "comments"


class Uploads(models.Model):
    original_name = models.CharField(max_length=300)
    content_type = models.CharField(max_length=100)
    new_name = models.CharField(max_length=100)
    path = models.CharField(max_length=500)
    code = models.CharField(max_length=70, unique=True)
    size = models.IntegerField()

    class Meta:
        db_table = 'uploads'
