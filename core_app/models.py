from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class AboutUs(models.Model):
	title = models.CharField(max_length=155)
	content = RichTextUploadingField()

	class Meta:
		verbose_name = 'about us'
		verbose_name_plural = 'about us'

	def __str__(self):
		return self.title


class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')

    def __str__(self):
        return self.content


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact us'
        verbose_name_plural = 'Contact us'

    def __str__(self):
        return self.name
