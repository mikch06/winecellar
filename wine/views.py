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









class IndexView(generic.ListView):
    template_name = 'wine/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Wine.objects


class WineView(generic.ListView):
    model = Wine
    template_name = 'wine/wine_list.html'


class DetailView(generic.DetailView):
    model = Wine
    template_name = 'wine/wine_detail.html'

class EditView(generic.DetailView):
    model = Wine
    template_name = 'wine/wine_form.html'



# 'About' page
def about(request):
    #return HttpResponse("This is all about...")
    return render(request, 'wine/about.html')