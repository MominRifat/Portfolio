from . import views
from django.urls import path
app_name = 'edu'
urlpatterns = [
    path('', views.edu, name='edu'),
]