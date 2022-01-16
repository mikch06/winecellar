from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('wine.urls')),
    path('admin/', admin.site.urls),
]

