from django.urls import path

#from wine.views import WineListView
from wine.views import WineDeleteView
from wine.views import WineDetailView
from wine.views import WineUpdateView
from wine.views import WineNewView
from . import views
from . import views

# App Namespace for app 'wine'
app_name = 'wine'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('wine/', views.WineView.as_view(), name='wine_list'),
    path('wine/<int:pk>', views.DetailView.as_view(), name='wine_detail'),
    path('edit/<int:pk>', views.EditView.as_view(), name='wine_edit'),
    path('delete/<int:pk>', WineDeleteView.as_view(), name='wine_delete'),
    path('about/', views.about, name='about'),

    ##  path('new/<int:pk>', WineNewView.as_view(), name='wine_edit'), # Create entries

    # watson search engine
    #path('r"^search/"', include('watson.urls')),
]
