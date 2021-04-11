from django import forms

class EconomySearchForm(forms.Form):
    search_word = forms.CharField(label='Search Keyword')


