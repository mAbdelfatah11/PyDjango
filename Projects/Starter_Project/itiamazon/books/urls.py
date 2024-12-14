

from django.urls import path                   ## importing the required path and include methods from the urls package
from books.views import bookindex,bookshome              ## import books app views


urlpatterns = [

    ## url routes for "books" application
    path('bookindex/',bookindex),
    path('home/',bookshome)

]
