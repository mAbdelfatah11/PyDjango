
from django.urls import path                                        # required for the default "django admin" panel
from amazon.views import helloworld, mywebsite, sayhello,amazonhome            # import amazon app views         



urlpatterns = [

    ## url routes for "amazon" application
    path('hello/',helloworld),
    path('iti/',mywebsite),
    path('iti/<name>', sayhello),
    # return template response 
    path("home/",amazonhome)



]
