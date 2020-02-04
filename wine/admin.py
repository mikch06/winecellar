from django.contrib import admin

from .models import Wine


class WineAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['winename']}),
        (None, {'fields': ['producer']}),
        (None, {'fields': ['year']}),
    ]
    list_display = ('winename', 'producer', 'year', 'purchase', 'nmbrbottles')
    search_fields = ['winename', 'producer', 'year', 'purchase', 'nmbrbottles']

admin.site.register(Wine, WineAdmin)