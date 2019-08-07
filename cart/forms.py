from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label="", help_text="", initial=1, widget=forms.NumberInput(attrs={
        'id': 'qty',
        'class': 'input-text qty',
        'title': 'Qty',
        'min': '1'
    }))
    update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)
