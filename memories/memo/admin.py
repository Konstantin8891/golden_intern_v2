from django.contrib.gis import admin

from .models import InMemories


class InMemoriesAdmin(admin.OSMGeoAdmin):
    list_display = ('title', 'comment', 'location')


admin.site.register(InMemories, InMemoriesAdmin)
