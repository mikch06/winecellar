from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Wine
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

class WineListView(ListView):
    model = Wine
    template_name = "wines/list.html"
    context_object_name = "wines"

class WineDetailView(DetailView):
    model = Wine
    template_name = "wines/_detail.html"
    context_object_name = "wine"

class WineCreateView(CreateView):
    model = Wine
    fields = ["name", "year", "region", "grape", "notes"]
    template_name = "wines/_form.html"
    success_url = reverse_lazy("wine_list")

class WineUpdateView(UpdateView):
    model = Wine
    fields = ["name", "year", "region", "grape", "notes"]
    template_name = "wines/_form.html"
    success_url = reverse_lazy("wine_list")

def wine_delete(request, pk):
    wine = get_object_or_404(Wine, pk=pk)
    if request.method == "POST":
        wine.delete()
        wines = Wine.objects.all()
        return render(request, "wines/list.html", {"wines": wines})
    return render(request, "wines/_delete_confirm.html", {"wine": wine})

# 'About' page
def about(request):
    return render(request, 'wine/about.html')

# 'Info' page
@login_required
def info(request):
    return render(request, 'wine/info.html')    