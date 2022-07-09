from django import forms
from leaflet.forms.widgets import LeafletWidget

from .models import InMemories


class InMemoriesForm(forms.ModelForm):
    class Meta:
        model = InMemories
        fields = ('title', 'comment', 'location')
        widgets = {'location': LeafletWidget()}
