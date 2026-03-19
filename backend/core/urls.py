from django.urls import path
from .views import CategoryListView, BrandListView, ProductListView, ProductDetailView, DealListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('deals/', DealListView.as_view(), name='deal-list'),
]
