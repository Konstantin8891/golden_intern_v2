from django.contrib import admin

from .models import InMemories

class InMemoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'comment', 'location')

    class Meta:
        verbose_name_plural = 'In memories'

admin.site.register(InMemories, InMemoriesAdmin)