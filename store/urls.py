from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('categories/<str:category>/', views.categorize, name="categorize"),
    path('description/<str:id>/', views.description, name="description"),
    path('search/', views.search, name="search"),
]