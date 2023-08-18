from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	release = models.DateTimeField(auto_now_add=True)
	rate = models.IntegerField()

	# uploader
	owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
	rated = models.CharField(max_length=100)

	class Meta:
		ordering = ['-release']

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if self.author == 'cao tan duc':
			self.rate = 5
		elif self.author == 'xavier cao':
			self.rate = 4 
		else:
			self.rate = 1

		self.rated = '*' * self.rate
		super().save(*args, **kwargs)