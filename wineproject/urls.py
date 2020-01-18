from django.contrib import admin
from django.urls import include, path
from django.urls import path

from django.conf.urls import url, include

urlpatterns = [
    # by default not in use or set.
    #path('contact/', include('wine.urls')),
    #path('author/', include('wine.urls')),

    path('', include('wine.urls')),
    path('admin/', admin.site.urls),

]

