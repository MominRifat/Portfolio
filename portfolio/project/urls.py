from . import views
from django.urls import path

app_name = 'project'

urlpatterns = [
    path('', views.project, name='project'),
]
