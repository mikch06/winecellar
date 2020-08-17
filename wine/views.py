from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.db.models import Sum
from wine.models import Wine
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from wine.models import WineForm

class WinesView(LoginRequiredMixin, generic.ListView):
    model = Wine
    template_name = 'wine/wine_list.html'

    # Show number of bottles and different wines for each user
    def get_context_data(self, *args, **kwargs):
        context = super(WinesView, self).get_context_data(*args, **kwargs)
        context['bottles_sum'] = Wine.objects.filter(owner=self.request.user).aggregate(Sum('nmbrbottles'))['nmbrbottles__sum']
        context['wines_sum'] = Wine.objects.filter(owner=self.request.user).count()
        return context

    # Filter user data only
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(owner=self.request.user)

# Wine Delete View
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Wine
    success_url = reverse_lazy('wine:wine_list')

# 'About' page
@login_required
def about(request):
    #return HttpResponse("This is all about...")
    return render(request, 'wine/about.html')

@login_required
def home(request):
    return render(request, 'wine/index.html')

@login_required
def createWine(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WineForm(request.POST)
        # Create instance for user data entry
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect('/')
    else:
        form = WineForm()
    return render(request, 'wine/create_form.html', {'form': form})

@login_required
def updateWine(request, pk):
    update = Wine.objects.get(id=pk)
    form = WineForm(instance=update)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WineForm(request.POST, instance=update)
        # Create instance for user data entry
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect('/')

    return render(request, 'wine/create_form.html', {'form': form})

class WineDetailView(DetailView):
    model = Wine
    template_name = 'wine/wine_modal.html'