from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	release = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-release']

	def __str__(self):
		return self.title