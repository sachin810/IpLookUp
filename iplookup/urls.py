from django.urls import path
from . import views

app_name = 'iplookup'

urlpatterns = [
    path('', views.home, name='home'),
]