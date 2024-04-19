from . import views
from django.urls import path

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add-product/<slug:product_slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove-product/<slug:product_slug>/', views.remove_from_cart, name='remove_from_cart')
]