from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin

from .models import InMemories

class InMemoriesAdmin(admin.OSMGeoAdmin):
    list_display = ('title', 'comment', 'location')

admin.site.register(InMemories, InMemoriesAdmin)
