

from django.contrib import admin        ## required for the default "django admin" panel
from django.urls import path, include   ## importing the required path and include methods from the urls package
# from amazon.views import helloworld, mywebsite, sayhello      ## import amazon app views         
# from books.views import bookindex                               ## import books app views


urlpatterns = [
    path('admin/', admin.site.urls),            # default webpage url and path

    ## url routes for "amazon" application
    # path('hello/',helloworld),
    # path('iti/',mywebsite),
    # path('iti/<name>', sayhello),

    # ## url routes for "books" application
    # path('books/',booklib)


    # Refactoring urls: including each "app" urls file instead of mentioning all thier "urls" here 
    # """ include "urls" module for "amazon" app """
    path('amazon/', include("amazon.urls")),            # when you type /amazon in site url, it will include directly the amazon "urls" module file


    # """ include "urls" module for "books" app """
    path('books/', include("books.urls")),

]
