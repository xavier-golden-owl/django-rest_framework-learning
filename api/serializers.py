from .models import Book

from django.contrib.auth.models import User

from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ['title', 'author', 'release']

	
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'books']