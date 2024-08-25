from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def display(request):
    # return HttpResponse("welcome to django")
    return render (request, 'hello.html', {"name":"SIKIRU"})