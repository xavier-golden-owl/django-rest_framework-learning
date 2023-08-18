from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	release = models.DateTimeField(auto_now_add=True)

	# uploader
	owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
	rate = models.IntegerField()

	class Meta:
		ordering = ['-release']

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if self.author == 'Unknown':
			self.rate = 1
		else:
			self.rate = 5

		super().save(*args, **kwargs)