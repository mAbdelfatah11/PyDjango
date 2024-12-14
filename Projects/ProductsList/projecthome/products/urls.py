# here is my app specific urls
from django.urls import path
from products.views import productindex

urlpatterns = [
    ## add urls here

    path('all', productindex, name="products.all")
]
