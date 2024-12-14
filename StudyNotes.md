# Django installation:

* install pip3                          >$ pip3 --version          ;
* install virtualenv                    >$ pip install virtualenv
* create virtual env called venv        >$ virtualenv venv     &&  source venv/Scripts/activate
* install Django (doc: ):
```bash
$ pip install django
* check if django installed:
$ pip freeze
        ```

            asgiref==3.8.1

            Django==5.1.4

            sqlparse==0.5.2

            tzdata==2024.2

        ```

# Create ur first project with django:
$ django-admin startproject awsamazon             (creates project with default app files)
```

* this creates the following:
* awsamazon parent folder, represents project folder
* awsamazon sub folder, represents default app folder
* manage.py file:
* create django app
* start server
* make and run migrations

* start server:
```bash
$ python awsamazon/manage.py runserver    (start development server for ur application)
```

        ```

            Starting development server at http://127.0.0.1:8000/

        ```






# * Django Architectural Pattern:   
* _(show up the attchached note "MVC vs MVT" to know more)_
*  Architectural pattern: define the overall structure of an application and the relationships between its components.
* Django follows  MVT Architectural Pattern:
* MVT: model view template


# * Create multiple apps in the same project:
* the new app is a discrete app in the smae project, it holds different "views" file, it might be like a new feature
* you then add URL paths in the "urls" file to route to the new app views

* cd to "awsamazon" project
* ` python manage.py startapp amazon            (create another app folder and files in the same project)`


# * Create a new webpage in the new application:   (check awsamazon folder "urls && views files")
* accroding to the MVT arch pattern for django: each "url" has to have a "view" to be routed to
* in the default app which is "awsamazon":
* create the url path: choose which string do you want to use to reach webpage like url/hello for example
* in your application "amazon":
* create the required view to be called using path
* in the default app "awsamazon":
* import the view module, and add the function to the path

Refactor "URLs":

-----------------


* multiple applications could be created in the same project,
* you have to import each of those "views" module inside the "urls" module file and route the required path to the approperiate function
* this will make the "urls" more complicated as it stores all the routes"urls"
* so,
* create urls file for each app and add ur app specific routes
* just "include" the "app.urls" path inside the main urls file in the default app: path('amazon/', include("amazon.urls")),


Templates:

==========

* with Django arch pattern we have used just two componenets so far which are "routers" && "views"
* a route "url" redirects to a "view" which is an HttpResponse: return HttpResponse("<h1> Hello From the Library </h1>")
* However we can route "url" to view, then "view" display a specific web "Template" which contains some html,css,js or any web code,
* it's an advanced step in the MVT arch pattern:   routers --> view ---> template
* ex response that call templates instead of http HttpResponse:

How Template Works:

-------------------

* In the "settings.py" file in the default app, Django by default adds some config params related to how it manages the Templates
* "INSTALLED_APPS" :
* it lists the apps that python interpriter fetches one by one in a row
* To allow python to render your app templates while interpriting code:
* you need to add your newly created apps at the end of this list
* you must add ur apps to this list even if you don't intend to use templates

* there are two ways to add apps:
* add app folder name: "not prefered"
* add app full path:
* it means adding app corresponding class name
* each app has an "apps.py" file which define a "class" called same as the app "name"
* you should add that full class name like:  "amazon.apps.amazonConfig"


* "TEMPLATES" :
* it has important params like,
* 'APP_DIRS': True
* it tells python interpriter to search for any folder called "templates" all over the app dires

* Create folder called "templates" at each application directory
* in templates, create a folder with the same name of the app folder

* then, when you call the render method in the views file, python automatically searches all app dires for the required template while interpriting



Static files:

* you can serve static files like images, css, javascripts files

* STATIC_URL = 'static/'
*  it's a directive inside "setting.py" indicates where to search for static files inside the application folder
* you must create directory called "static", it is mandatory to be named like that

* inside "<app-folder>/static" folder:
* create <app-name> dir
* optionally create these folders to serve static file in different categories: "images","css","js"

* access static files in code:
* in ur template html for example:
* add the following code:  src = {% static 'products/images/product1.png' %}
* restart server: must

* access css:
*     <link type="text/css" rel="stylesheet" href="{% static  'products/css/style.css'%}">


Access Database:

* "view" should access "model" to retrive data from the "database"
* Django comes with a built-in SQLite database. However, we can use the various databases in Django.
* you need to configure "database access credentials" inside "settings" file in the default app
* each backend db has some different configs inside the "DATABASES" directive
* you can show it up at: