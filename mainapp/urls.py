from django.urls import path

from . import views
from .views import ProductDetailView, CategoryDetailView, BaseView

urlpatterns = [
    path("", BaseView.as_view(), name="index"),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail')
]
