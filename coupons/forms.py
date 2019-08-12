from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField(label="", help_text="", widget=forms.TextInput(
        attrs={'placeholder': "Enter code here..."}))
