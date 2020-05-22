from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.db.models import Sum
from wine.models import Wine
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from wine.models import WineForm



# Real and right generic view code
class WinesView(LoginRequiredMixin, generic.ListView):
    model = Wine
    template_name = 'wine/wine_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(WinesView, self).get_context_data(*args, **kwargs)
        context['bottles_sum'] = Wine.objects.all().aggregate(Sum('nmbrbottles'))['nmbrbottles__sum']
        context['wines_sum'] = Wine.objects.count()
        return context

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
        # check whether it's valid:
        if form.is_valid():
            form.save()
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
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(request, 'wine/create_form.html', {'form': form})


class WineReadView(generic.DetailView):
    model = Wine
    template_name = 'wine/modal.html'
    success_message = 'SchubiDubi'