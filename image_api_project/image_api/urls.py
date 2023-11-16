from django.urls import path
from .views import ImageListCreateAPIView, ImageDetailAPIView

urlpatterns = [
    path('images/', ImageListCreateAPIView.as_view(), name='image-list-create'),
    path('images/<int:pk>/', ImageDetailAPIView.as_view(), name='image-detail'),
]
