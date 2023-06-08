from django.db import models
import random
from blog.models import Tag, Category


class Video(models.Model):
	id = models.AutoField(primary_key=True)
	random_id = models.PositiveIntegerField(unique=True, default=random.randint(100, 999))
	title = models.CharField(max_length=255)
	thumbnail = models.ImageField()
	description = models.TextField()
	iframe = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
	tags = models.ManyToManyField(Tag)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title