from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from httpx import request
from .models import Wine
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import WineForm
from django.http import HttpResponse
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font

# Wine List View
class WineListView(LoginRequiredMixin, ListView):
    model = Wine
    template_name = "wines/list.html"
    context_object_name = "wines"

    def get_queryset(self):
        return Wine.objects.filter(owner=self.request.user)

# Wine Detail View
class WineDetailView(LoginRequiredMixin, DetailView):
    model = Wine
    template_name = "wines/_detail.html"
    context_object_name = "wine"

# Wine Create View
class WineCreateView(LoginRequiredMixin, CreateView):
    model = Wine
    form_class = WineForm
    template_name = "wines/_form.html"
    success_url = reverse_lazy("wine_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# Wine Update View
class WineUpdateView(LoginRequiredMixin, UpdateView):
    model = Wine
    form_class = WineForm
    template_name = "wines/_form.html"
    success_url = reverse_lazy("wine_list")
    
# Delete view
@login_required
def wine_delete(request, pk):
    wine = get_object_or_404(Wine, pk=pk, owner=request.user)

    if request.method == "POST":
        wine.delete()
        wines = Wine.objects.filter(owner=request.user)
        return render(request, "wines/list.html", {"wines": wines})

    return render(request, "wines/_delete_confirm.html", {"wine": wine})

@login_required
def copyWine(request, pk):
    original = get_object_or_404(Wine, pk=pk, owner=request.user)

    if request.method == "POST":
        form = WineForm(request.POST)
        if form.is_valid():
            new_wine = form.save(commit=False)
            new_wine.owner = request.user
            new_wine.pk = None  # wichtig: neuer Eintrag!
            new_wine.save()
            return HttpResponse(status=204)  # für Unpoly
    else:
        # Formular wird mit Kopie der Daten befüllt
        data = original.__dict__.copy()
        data.pop('id', None)
        data.pop('pk', None)
        data.pop('_state', None)
        form = WineForm(initial=data)

    return render(request, "wines/_form.html", {"form": form, "is_copy": True})

# Winelog, show last changes for users wines.
class WineLog(LoginRequiredMixin, generic.ListView):
    model = Wine
    template_name = 'wines/log.html'
    context_object_name = 'wines'  # <-- hier vergeben

    # Show number of bottles and different wines for each user
    def get_context_data(self, *args, **kwargs):
        context = super(WineLog, self).get_context_data(*args, **kwargs)
        context['bottles_sum'] = Wine.objects.filter(owner=self.request.user).aggregate(Sum('nmbrbottles'))['nmbrbottles__sum']
        context['wines_sum'] = Wine.objects.filter(owner=self.request.user).count()
        return context

    # Filter user data only
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(owner=self.request.user).order_by('-editdate')[:30]
    
# Data export
@login_required
def export_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    wines = Wine.objects.filter(owner=request.user)
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="wine_export.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['Wein', 'Produzent', 'Trauben', 'Jahrgang', 'Land', 'Region', 'Kaufdatum', 'Preis/Fl.', 'Dealer', 'von', 'bis', 'Lagerort', 'Anz.Fl'])
    wines = wines.values_list('winename','producer', 'grapes', 'year', 'country', 'region', 'purchase', 'price', 'dealer', 'drinkfrom', 'drinkto', 'warehouse', 'nmbrbottles')
    for w in wines:
        writer.writerow(w)
    return response    

@login_required
def export_xlsx(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="wine_export.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.title = "MyBottles"

    headers = ['Wein', 'Produzent', 'Trauben', 'Jahrgang', 'Land', 'Region',
               'Kaufdatum', 'Preis/Fl.', 'Dealer', 'von', 'bis', 'Lagerort', 'Anz.Fl']

    ws.append(headers)
    for cell in ws[1]:
        cell.font = Font(bold=True)

    wines = Wine.objects.filter(owner=request.user).values_list(
        'winename','producer','grapes','year','country','region',
        'purchase','price','dealer','drinkfrom','drinkto','warehouse','nmbrbottles'
    )

    for wine in wines:
        ws.append(wine)

    wb.save(response)
    return response

class FullView(LoginRequiredMixin, generic.ListView):
    model = Wine
    template_name = 'wine/wine_fullview.html'

    # Filter user data only
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(owner=self.request.user)

# Homepage
def index(request):
    return render(request, 'wines/home.html')

# 'Info' page
@login_required
def info(request):
    return render(request, 'wines/info.html')

# 'About' page
def about(request):
    return render(request, 'wines/about.html')

# Logout view
def logout_view(request):
    logout(request)    


from django.db.models import Count, Sum
from django.http import JsonResponse

@login_required
def wine_stats(request):
    # Gruppiere nach Land und zähle Weine & Flaschen
    stats = (
        Wine.objects.filter(owner=request.user)
        .values('country')
        .annotate(
            wine_count=Count('id'),
            bottle_sum=Sum('nmbrbottles'),
        )
        .order_by('-bottle_sum')
    )

    # Wenn per AJAX/JSON (z. B. für Chart.js)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'labels': [s['country'] or 'Unbekannt' for s in stats],
            'wines': [s['wine_count'] for s in stats],
            'bottles': [s['bottle_sum'] or 0 for s in stats],
        })

    # Normales Rendering (z. B. als Seite oder Modal)
    return render(request, 'wines/_stats.html', {'stats': stats})
