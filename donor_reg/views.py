from django.shortcuts import render
from .forms import RegistrationForm
from .models import Form
from django.contrib import messages

def index(request):
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone = form.cleaned_data["phone"]
            address = form.cleaned_data["address"]
            date = form.cleaned_data["last_donation"]
            blood_group = form.cleaned_data["blood_group"]
            
            Form.objects.create(first_name=first_name, last_name=last_name, blood_group=blood_group,
                         phone=phone, last_donation=date, location=address)
            
            messages.success(request, "Registration Successfull")
    return render(request, "index.html")
