from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def edu(request):
    return render(request, 'edu/edu.html')