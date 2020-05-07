from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.db.models import Sum
from wine.models import Wine
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import WineForm

# Real and right generic view code
class WinesView(LoginRequiredMixin, generic.ListView):
    model = Wine
    template_name = 'wine/wine_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WinesView, self).get_context_data(*args, **kwargs)
        context['bottles_sum'] = Wine.objects.all().aggregate(Sum('nmbrbottles'))['nmbrbottles__sum']
        context['wines_sum'] = Wine.objects.count()
        return context

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Wine

class EditView(LoginRequiredMixin, UpdateView):
    model = Wine
    template_name = 'wine/wine_form.html'
    fields = ['winename', 'producer', 'grapes', 'year', 'country',
              'region', 'purchase', 'dealer', 'notes', 'drinkfrom', 'drinkto', 'nmbrbottles', 'price']
    success_url = reverse_lazy('wine:wine_list')


# Wine Delete View
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Wine
    success_url = reverse_lazy('wine:wine_list')

# Wine Create View
class CreateView(LoginRequiredMixin, CreateView):
    model = Wine
    template_name = 'wine/wine_form.html'
    fields = ['winename', 'producer', 'grapes', 'year', 'country',
              'region', 'purchase', 'dealer', 'notes', 'drinkfrom', 'drinkto', 'nmbrbottles', 'price']
    success_url = reverse_lazy('wine:wine_list')

# 'About' page
def about(request):
    #return HttpResponse("This is all about...")
    return render(request, 'wine/about.html')

@login_required
def home(request):
    return render(request, 'wine/index.html')


def wineform(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WineForm()

    return render(request, 'wine/form.html', {'form': form})