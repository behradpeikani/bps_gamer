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
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.comment


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
