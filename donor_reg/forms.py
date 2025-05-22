from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    blood_group = forms.CharField(max_length=80)
    phone = forms.CharField(max_length=80)
    email = forms.EmailField()
    last_donation = forms.DateField()
    address = forms.CharField(max_length=100)