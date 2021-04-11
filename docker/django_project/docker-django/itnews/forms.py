from django import forms

class ITnewsSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Keyword')

    
class RefreshForm(forms.Form):
    pass