from .models import Book

from django.contrib.auth.models import User

from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	rate = serializers.ReadOnlyField()
	class Meta:
		model = Book
		fields = '__all__'

	
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'books']