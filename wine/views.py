from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from wine.models import Wine

# Wine List (lists all wines in a view
class WineListView(ListView):
    model = Wine
    paginate_by = 100  # if pagination is desired

# Wine Detail View
from django.views.generic import DetailView
from wine.models import Wine

class WineDetailView(DetailView):
    model = Wine

# Wine Update View
class WineUpdateView(UpdateView):
    model = Wine
    fields = ['winename', 'producer', 'grapes', 'year', 'country',
              'region', 'purchase', 'notes', 'drinkfrom', 'drinkto', 'nmbrbottles']
    success_url = reverse_lazy('wine_list')

# Wine Delete View
class WineDeleteView(DeleteView):
    model = Wine
    success_url = reverse_lazy('wine_list')

class WineNewView(CreateView):
    model = Wine