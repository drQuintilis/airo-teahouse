from django import forms

from .models import ResponseItem

class ResponseForm(forms.ModelForm):

    class Meta:
        model = ResponseItem
        fields = ('name', 'text',)