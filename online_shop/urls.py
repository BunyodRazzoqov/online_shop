from django.contrib import admin
from django.urls import path
from online_shop import views

urlpatterns = [
    path('product-list/', views.product_list, name='product_list'),
    path('categories/', views.categories, name='categories'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product_detail'),
]
