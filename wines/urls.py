from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("wines/", WineListView.as_view(), name="wine_list"),
    path("wines/<int:pk>/", WineDetailView.as_view(), name="wine_detail"),
    path("wines/<int:pk>/edit/", WineUpdateView.as_view(), name="wine_edit"),
    path("new/", WineCreateView.as_view(), name="wine_new"),
    path("wines/<int:pk>/delete/", wine_delete, name="wine_delete"),
    path('wines/<int:pk>/copy/', views.copyWine, name='wine_copy'),
    path('wines/debug/', lambda request: HttpResponse("DEBUG OK")),
    path('about/', views.about),
    path('info/', views.info),
    path('wines/export/', views.export_csv),
    path('wines/export_xls/', views.export_xlsx),
    path('wines/log/', views.WineLog.as_view(), name='wine_log'),
    path('logout/', views.logout_view),
]
