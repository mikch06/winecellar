from django.urls import path

#from wine.views import WineListView
from . import views

# App Namespace for app 'wine'
app_name = 'wine'
urlpatterns = [
    path('wine/', views.WinesView.as_view(), name='wine_list'),
    path('wine/<int:pk>', views.DetailView.as_view(), name='wine_detail'),
    path('edit/<int:pk>', views.EditView.as_view(), name='wine_edit'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='wine_delete'),
    path('new/', views.CreateView.as_view(), name='wine_create'),

    path('about/', views.about, name='about'),
    path('', views.home, name='index'),

    ##  path('new/<int:pk>', WineNewView.as_view(), name='wine_edit'), # Create entries

    # watson search engine
    #path('r"^search/"', include('watson.urls')),
]
