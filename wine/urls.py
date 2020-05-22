from django.urls import path
from . import views

# App Namespace for app 'wine'
app_name = 'wine'
urlpatterns = [
    path('wine/', views.WinesView.as_view(), name='wine_list'),
    path('wine/delete/<int:pk>', views.DeleteView.as_view(), name='wine_delete'),
    path('new/', views.createWine, name='create_wine'),
    path('wine/edit/<int:pk>', views.updateWine, name='update_wine'),

    path('about/', views.about, name='about'),
    path('', views.WinesView.as_view(), name='wine_list'),

    path('wine/read/<int:px>', views.WineReadView.as_view(), name='read_wine')
]
