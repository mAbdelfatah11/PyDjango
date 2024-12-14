from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bookindex(request):
    return HttpResponse("<h1> Hello From the Library </h1>")

# using templates: it searches all "templates" dires by default and based on the "settings.py", so mention the path inside templates only
def bookshome(request):
    return render(request, "books/home.html")