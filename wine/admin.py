from django.contrib import admin

from .models import Wine


class WineAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['winename']}),
        ('Date information', {'fields': ['entrydate'], 'classes': ['collapse']}),
    ]
    list_display = ('winename', 'producer', 'year')
    list_filter = ['year', 'winename']
    search_fields = ['winename', 'producer']

admin.site.register(Wine, WineAdmin)
