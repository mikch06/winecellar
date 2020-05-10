from django.urls import path
from . import views
from wine.views import WineUpdate

# App Namespace for app 'wine'
app_name = 'wine'
urlpatterns = [
    path('wine/', views.WinesView.as_view(), name='wine_list'),
    path('wine/<int:pk>', views.DetailView.as_view(), name='wine_detail'),
    path('wine/delete/<int:pk>', views.DeleteView.as_view(), name='wine_delete'),

    path('new/', views.wineform),
    path('wine/edit/<int:pk>/', WineUpdate.as_view(), name='wine-update'),




    path('about/', views.about, name='about'),
    path('', views.WinesView.as_view(), name='wine_list'),


]
