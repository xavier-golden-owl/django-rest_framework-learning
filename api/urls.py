from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
	path('', views.api_root),

	path('books/', views.BookList.as_view(), name='book-list'),
	path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
	path('books/<int:pk>/rate/', views.BookRate.as_view(), name='book-rate'),

	path('users/', views.UserList.as_view(), name='user-list'),
	path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)