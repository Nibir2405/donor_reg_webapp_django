from django.shortcuts import render
from .forms import RegistrationForm

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
            print(first_name)
    return render(request, "index.html")
