from django.urls import path

from cart import views

app_name = "cart"
urlpatterns = [
    path('add/', views.cart_add, name='add'),
    path('count/', views.cart_count, name='count'),
]
