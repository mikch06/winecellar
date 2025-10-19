from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.db.models import Sum
from wine.models import Wine
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from wine.models import WineForm
import csv
import xlwt
import datetime
from datetime import datetime

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
        return query_set.filter(owner=self.request.user).order_by('-editdate')[:30]

# Detail view in 'Last changes'
@login_required
def WineLogDetail(request, pk):
    wine = Wine.objects.get(id=pk)

    return render(request, 'wine/wine_log_detail.html', {'wine': wine})

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
def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="wine_export.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('MyBottles', cell_overwrite_ok=True)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    date_style = xlwt.XFStyle()

    columns = ['Wein', 'Produzent', 'Trauben', 'Jahrgang', 'Land', 'Region', 'Kaufdatum', 'Preis/Fl.', 'Dealer', 'von', 'bis', 'Lagerort', 'Anz.Fl']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    date_style.num_format_str = "dd.mm.YYYY"

    rows = Wine.objects.filter(owner=request.user).values_list('winename','producer', 'grapes', 'year', 'country', 'region', 'purchase', 'price', 'dealer', 'drinkfrom', 'drinkto', 'warehouse', 'nmbrbottles')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):

            ws.write(row_num, col_num, row[col_num], font_style)
            ws.write(row_num, 6, datetime.now(), date_style)

    wb.save(response)
    return response

# Logout view
def logout_view(request):
    logout(request)
