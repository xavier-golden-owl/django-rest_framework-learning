from .views import BookViewSet, UserViewSet, api_root

from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers


book_list = BookViewSet.as_view({
	'get': 'list',
	'post': 'create',
})

book_detail = BookViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy',
})

book_rate = BookViewSet.as_view({
	'get': 'rate',
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
	'get': 'list',
})

user_detail = UserViewSet.as_view({
	'get': 'retrieve',
})

urlpatterns = [
	path('', api_root),

	path('books/', book_list, name='book-list'),
	path('books/<int:pk>/', book_detail, name='book-detail'),
	path('books/<int:pk>/rate/', book_rate, name='book-rate'),

	path('users/', user_list, name='user-list'),
	path('users/<int:pk>/', user_detail, name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)