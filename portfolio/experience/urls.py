from . import views
from django.urls import path
app_name = 'experience'
urlpatterns = [
    path('', views.experience, name='experience'),
]