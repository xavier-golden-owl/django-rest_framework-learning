from . import views

from django.urls import path, include

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book')
router.register(f'users', views.UserViewSet, basename='user')

urlpatterns = [
	path('', include(router.urls)),
]