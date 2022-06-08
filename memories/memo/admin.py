from django.contrib import admin

from .models import InMemories

class InMemoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'comment', 'location')

admin.site.register(InMemories, InMemoriesAdmin)