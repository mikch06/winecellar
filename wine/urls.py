from django.urls import path
from . import views

# App Namespace for app 'wine'
app_name = 'wine'
urlpatterns = [
    path('', views.index),
    path('wine/', views.WinesView.as_view(), name='wine_list'),
    path('wine/delete/<int:pk>', views.DeleteView.as_view(), name='wine_delete'),
    path('wine/new/', views.createWine, name='create_wine'),
    path('wine/edit/<int:pk>', views.updateWine, name='update_wine'),
    path('wine/copy/<int:pk>', views.copyWine, name='copy_wine'),
    path('about/', views.about),
    path('wine/full/', views.FullView.as_view(), name='wine_fullview'),
    path('wine/log/', views.WineLog.as_view(), name='wine_log'),

]
