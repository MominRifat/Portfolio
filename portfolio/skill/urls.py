from . import views
from django.urls import path
app_name = 'skill'
urlpatterns = [
    path('', views.skill, name='skill'),
]