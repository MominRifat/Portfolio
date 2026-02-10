from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def skill(request):
    return render(request, 'skill/skill.html')