# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),      # Add this line for the root URL
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('test_token/', views.test_token, name='test_token'),
]
