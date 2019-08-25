from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'company_name',
                  'address', 'city', 'postal_code', 'phone_number', 'email']
