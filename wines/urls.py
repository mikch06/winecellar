from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views

# App Namespace for app 'wine'



# !remove this namespace
urlpatterns = [
    #TODO: copy View
    #path('wine/copy/<int:pk>', views.copyWine, name='copy_wine'),
    path('about/', views.about),
    path('info/', views.info),
    path('wine/export/', views.export_csv),
    path('wine/export_xls/', views.export_xls),
    #TODO: Fix as_view
    #path('wine/full/', views.FullView.as_view(), name='wine_fullview'),
    path('wines/log/', views.WineLog.as_view(), name='log'),
    path('wine/detail/<int:pk>', views.WineLogDetail, name='wine_log_detail'),
    path('logout/', views.logout_view),

    # New urls routes
    path('', views.index),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("wines/", WineListView.as_view(), name="wine_list"),
    path("<int:pk>/", WineDetailView.as_view(), name="wine_detail"),
    path("<int:pk>/edit/", WineUpdateView.as_view(), name="wine_edit"),
    path("new/", WineCreateView.as_view(), name="wine_new"),
    path("wines/<int:pk>/delete/", wine_delete, name="wine_delete"),
    path('wines/debug/', lambda request: HttpResponse("DEBUG OK")),
]
