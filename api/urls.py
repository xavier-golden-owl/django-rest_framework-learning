from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
	path('books/', views.BookList.as_view()),
	path('books/<int:pk>/', views.BookDetail.as_view()),
	path('users/', views.UserList.as_view()),
	path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)