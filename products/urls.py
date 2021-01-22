from django.urls import path, include
from .views import create, detail, upvote

urlpatterns = [
    path('create/', create, name='create'),
    path('<int:product_id>', detail, name='detail'),
    path('<int:product_id>/upvote', upvote, name='upvote')
]