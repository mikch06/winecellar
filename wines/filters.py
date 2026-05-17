class WineFilter:
    def __init__(self, data, queryset):
        self.data = data
        self.qs = queryset

        self.apply()

    def apply(self):
        self.filter_search()
        self.filter_country()
        self.filter_year()
        self.filter_drinkable()

    def get(self, key):
        value = self.data.get(key)
        return value if value not in ["", None] else None

    # -------------------------
    # SEARCH
    # -------------------------
    def filter_search(self):
        q = self.get("q")
        if q:
            self.qs = self.qs.filter(name__icontains=q)

    # -------------------------
    # COUNTRY
    # -------------------------
    def filter_country(self):
        country = self.get("country")
        if country:
            self.qs = self.qs.filter(country=country)

    # -------------------------
    # YEAR RANGE
    # -------------------------
    def filter_year(self):
        year_from = self.get("year_from")
        year_to = self.get("year_to")

        if year_from:
            self.qs = self.qs.filter(year__gte=year_from)

        if year_to:
            self.qs = self.qs.filter(year__lte=year_to)

    # -------------------------
    # DRINKABLE RANGE
    # -------------------------
    def filter_drinkable(self):
        drink_from = self.get("drink_from")
        drink_to = self.get("drink_to")

        if drink_from:
            self.qs = self.qs.filter(drinkable_from__gte=drink_from)

        if drink_to:
            self.qs = self.qs.filter(drinkable_to__lte=drink_to)