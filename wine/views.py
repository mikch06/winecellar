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


# Wine Detail View
from django.views.generic import DetailView
from wine.models import Wine

## hint: https://docs.djangoproject.com/en/3.0/intro/tutorial04/#amend-views
#todo: amend views

## Real and right generic view code
class WineView(generic.ListView):
    model = Wine
    template_name = 'wine/wine_list.html'

class DetailView(generic.DetailView):
    model = Wine
    template_name = 'wine/wine_detail.html'

class EditView(UpdateView):
    model = Wine
    template_name = 'wine/wine_form.html'
    fields = ['winename', 'producer', 'grapes', 'year', 'country',
              'region', 'purchase', 'notes', 'drinkfrom', 'drinkto', 'nmbrbottles']
    success_url = reverse_lazy('wine:wine_list')

# Wine Delete View
class DeleteView(DeleteView):
    model = Wine
    success_url = reverse_lazy('wine:wine_list')

# Wine Create View
class CreateView(CreateView):
    model = Wine
    template_name = 'wine/wine_create.html'
    fields = ['winename', 'producer', 'year', 'country', 'nmbrbottles']
    success_url = reverse_lazy('wine:wine_list')

# 'About' page
def about(request):
    #return HttpResponse("This is all about...")
    return render(request, 'wine/about.html')

def home(request):
    return render(request, 'wine/index.html')