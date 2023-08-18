from .models import Book

from django.contrib.auth.models import User

from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	rate = serializers.HyperlinkedIdentityField(view_name='book-rate', format='html')

	class Meta:
		model = Book
		fields = ['url', 'id', 'title', 'author', 'release', 'rate', 'owner']

	
class UserSerializer(serializers.ModelSerializer):
	books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)
	class Meta:
		model = User
		fields = ['url', 'id', 'username', 'books']