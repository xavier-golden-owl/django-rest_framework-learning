from .models import Book
from .serializers import BookSerializer

from rest_framework import mixins
from rest_framework import generics


class BookList(mixins.ListModelMixin,
	mixins.CreateModelMixin,
	generics.GenericAPIView):

	queryset = Book.objects.all()
	serializer_class = BookSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
	

class BookDetail(mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin,
	generics.GenericAPIView):

	queryset = Book.objects.all()
	serializer_class = BookSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)