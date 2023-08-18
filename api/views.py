from .models import Book
from .serializers import BookSerializer, UserSerializer

from rest_framework import mixins
from rest_framework import generics

from django.contrib.auth.models import User

class BookList(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer