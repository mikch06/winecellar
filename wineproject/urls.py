from django.contrib import admin
from django.urls import include, path
from django.urls import path
#from wine.views import AuthorCreate, AuthorUpdate, AuthorDelete

urlpatterns = [
    path('contact/', include('wine.urls')),
    path('author/', include('wine.urls')),

    path('wine/', include('wine.urls')),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),

]

