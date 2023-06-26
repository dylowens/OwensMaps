from django.urls import path
from . import views  # import views from current directory

urlpatterns = [
    path('', views.home, name='home'),
]
