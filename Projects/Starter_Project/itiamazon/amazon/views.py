from django.shortcuts import render

from django.http import HttpResponse     # added to handel the view http response

# Create your views here.

# hellowworld webpage view
def helloworld(request):

    # create an https response as a reply to the function http request
    return HttpResponse("Hello World!")

def mywebsite(request):
    return HttpResponse("<h1> My Website </h1>")

def sayhello(request, name):
    return HttpResponse(f"<h1> Hi {name} </h1>")

# using templates, it searches all "templates" dires by default and based on the "settings.py", so mention the path inside templates only
def amazonhome(request):
    return render(request, "amazon/home.html")