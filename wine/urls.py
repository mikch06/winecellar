from django.urls import path
from . import views

# App Namespace for app 'wine'
app_name = 'wine'
urlpatterns = [
    path('wine/', views.WinesView.as_view(), name='wine_list'),
    path('wine/<int:pk>', views.DetailView.as_view(), name='wine_detail'),
    path('wine/delete/<int:pk>', views.DeleteView.as_view(), name='wine_delete'),

    path('new/', views.wineform),

    path('wine/edit/<int:pk>', views.update_view, name='wine_update'),




    path('about/', views.about, name='about'),
    path('', views.WinesView.as_view(), name='wine_list'),


]
