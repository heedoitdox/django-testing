from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list),
    path('user/', views.user_create)
]
