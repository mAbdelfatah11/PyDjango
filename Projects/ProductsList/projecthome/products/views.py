from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def productindex(request):

    allproducts = [
        {"id":1, "name": "product1", "image":"product1.png"},
        {"id":2, "name":"product2", "image":"product2.png"},
        {"id":3, "name":"product3", "image":"product3.png"}

    ]

    return render(request, "products/allproducts.html", context={"products":allproducts})

    # return HttpResponse("Here is the Product Index")

