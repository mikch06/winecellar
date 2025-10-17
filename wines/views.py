from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Wine
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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