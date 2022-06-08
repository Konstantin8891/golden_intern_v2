from django.contrib import admin

from .models import InMemories

class InMemoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'coment', 'location')

admin.site.register(InMemories, InMemoriesAdmin)