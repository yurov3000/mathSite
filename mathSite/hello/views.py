from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def math_ticket(request):
    return HttpResponse("<h2>here ticket math</h2>")