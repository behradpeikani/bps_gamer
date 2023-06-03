from django.db import models
from django.utils.text import slugify
import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
import random


class Category(models.Model):
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    random_id = models.PositiveIntegerField(unique=True, default=random.randint(1000, 9999))
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    content = RichTextUploadingField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
