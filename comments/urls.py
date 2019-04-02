from django.urls import path

from comments import views

app_name = "comments"
urlpatterns = [
    path('comment/<int:books_id>/', views.comment, name='comment'),
]
