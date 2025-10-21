from django.contrib import admin

from .models import Wine


class WineAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['winename']}),
        (None, {'fields': ['producer']}),
        (None, {'fields': ['year']}),
        (None, {'fields': ['purchase']}),
        (None, {'fields': ['drinkfrom']}),
        (None, {'fields': ['nmbrbottles']}),
    ]
    list_display = ('winename', 'producer', 'year', 'country', 'purchase', 'nmbrbottles')
    search_fields = ['winename', 'producer', 'year', 'country', 'purchase', 'nmbrbottles']

admin.site.register(Wine, WineAdmin)