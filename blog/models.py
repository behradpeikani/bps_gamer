from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
import random
from mptt.models import MPTTModel, TreeForeignKey


def article_image_upload_to(instance, filename):
    # Generate a unique filename based on the article title
    title = instance.title
    slug = slugify(title)
    return f'blog/{slug}/{filename}'

# Model Manager
class ArticlePublishManager(models.Manager):
    def published(self):
        return self.filter(status='published')


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

    OPTIONS = (
    ('draft', 'Draft'),
    ('published', 'Published')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to=article_image_upload_to)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=OPTIONS, default='publish')
    objects = ArticlePublishManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(MPTTModel):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='children')
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['publish']

    def __str__(self):
        return self.name