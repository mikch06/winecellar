from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from wine.models import Wine
# Only used if 'view def index' is used, see below
from django.http import HttpResponse
# If template loading is used
from django.template import loader
from django.shortcuts import render
# import generic views
from django.views import generic

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

## hint: https://docs.djangoproject.com/en/3.0/intro/tutorial04/#amend-views
#todo: amend views

# Simple start page index, with its html code
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #template = loader.get_template('wine/index.html')
    return render(request, 'wine/index.html')

# 'About' page
def about(request):
    #return HttpResponse("This is all about...")
    return render(request, 'wine/about.html')

# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'