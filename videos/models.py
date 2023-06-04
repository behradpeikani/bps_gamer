from django.db import models
import random


class Video(models.Model):
	id = models.AutoField(primary_key=True)
	random_id = models.PositiveIntegerField(unique=True, default=random.randint(100, 999))
	title = models.CharField(max_length=255)
	thumbnail = models.ImageField()
	description = models.TextField()
	iframe = models.TextField()
	tags = models.CharField(max_length=255)

	def __str__(self):
		return self.title