from django.urls import path

from users import views

app_name = 'user_name'
urlpatterns = [
    path('register/', views.register),
    path('register_handle/', views.register_handle, name='register_handle'),
]
