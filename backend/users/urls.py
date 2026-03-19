from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, WishlistView, WishlistDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', WishlistDeleteView.as_view(), name='wishlist-delete'),
]
