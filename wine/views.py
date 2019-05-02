from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy




from wine.models import Wine

# Wine List (lists all wines in a view
class WineListView(ListView):

    model = Wine
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# Wine Detail View
from django.views.generic import DetailView
from wine.models import Wine

class WineDetailView(DetailView):

    model = Wine

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context

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