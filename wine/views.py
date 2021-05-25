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
from django.db.models import Q # new

class WinesView(LoginRequiredMixin, generic.ListView):
    model = Wine
    template_name = 'wine/wine_list.html'

    # Filter user data only
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(owner=self.request.user)

# Wine Delete View
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Wine
    success_url = reverse_lazy('wine:wine_list')

# Homepage
def index(request):
    return render(request, 'wine/home.html')

# 'About' page
def about(request):
    return render(request, 'wine/about.html')

# 'Info' page
@login_required
def info(request):
    return render(request, 'wine/info.html')

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
            return HttpResponseRedirect('/wine')
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
            return HttpResponseRedirect('/wine')

    return render(request, 'wine/create_form.html', {'form': form})

@login_required
def copyWine(request, pk):
    update = Wine.objects.get(id=pk)
    form = WineForm(instance=update)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WineForm(request.POST)
        # Create instance for user data entry
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect('/wine')

    return render(request, 'wine/create_form.html', {'form': form})

class FullView(LoginRequiredMixin, generic.ListView):
    model = Wine
    template_name = 'wine/wine_fullview.html'

    # Filter user data only
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(owner=self.request.user)

class WineLog(LoginRequiredMixin, generic.ListView):
    model = Wine
    template_name = 'wine/wine_log.html'

    # Show number of bottles and different wines for each user
    def get_context_data(self, *args, **kwargs):
        context = super(WineLog, self).get_context_data(*args, **kwargs)
        context['bottles_sum'] = Wine.objects.filter(owner=self.request.user).aggregate(Sum('nmbrbottles'))['nmbrbottles__sum']
        context['wines_sum'] = Wine.objects.filter(owner=self.request.user).count()
        return context

    # Filter user data only
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(owner=self.request.user).order_by('-editdate')[:25]

#### Search
#todo: Security -> LoginRequiredMixin
class SearchResultsView(LoginRequiredMixin, generic.ListView):
    model = Wine

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Wine.objects.filter(
            Q(winename__icontains=query) | Q(producer__icontains=query) |
            Q(country__icontains=query) | Q(region__icontains=query) |
            Q(year__icontains=query) | Q(grapes__icontains=query) |
            Q(country__icontains=query) | Q(producer__icontains=query) |
            Q(drinkfrom__icontains=query) | Q(drinkto__icontains=query)|
            Q(notes__icontains=query)
        )
        return object_list