from django import forms
from .models import song

#Form to search all songs
class search_form(forms.Form):
	search_key=forms.CharField()
