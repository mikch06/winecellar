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
    path('info/', views.info),
    path('wine/export/', views.export),
    path('wine/full/', views.FullView.as_view(), name='wine_fullview'),
    path('wine/log/', views.WineLog.as_view(), name='wine_log'),
    #path('charts/', views.EditorChartView.as_view(), name='charts')
]
