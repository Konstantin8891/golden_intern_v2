from django import forms

from .models import InMemories


class InMemoriesForm(forms.ModelForm):
    class Meta:
        model = InMemories
        fields = ('title', 'comment')
