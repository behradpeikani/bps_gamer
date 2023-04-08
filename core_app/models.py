from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class AboutUs(models.Model):
	title = models.CharField(max_length=155)
	content = RichTextUploadingField()

	def __str__(self):
		return self.title