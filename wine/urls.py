from django.urls import path

from wine.views import WineListView, WineDeleteView
from wine.views import WineDetailView
from wine.views import WineUpdateView

urlpatterns = [
    path('', WineListView.as_view(), name='wine_list'),
    path('wine/<int:pk>', WineDetailView.as_view(), name='wine_detail'),
    path('edit/<int:pk>', WineUpdateView.as_view(), name='wine_edit'),
    path('delete/<int:pk>', WineDeleteView.as_view(), name='wine_delete'),
]
