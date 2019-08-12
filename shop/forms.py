from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label="", help_text="", widget=forms.TextInput(
        attrs={'placeholder': "Search entire store here..."}))
