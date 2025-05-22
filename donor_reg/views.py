from django.shortcuts import render
from .forms import RegistrationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            date = form.cleaned_data["last_donation"]
            blood_group = form.cleaned_data["blood_group"]
            
            Form.objects.create(first_name=first_name, last_name=last_name, blood_group=blood_group,
                         phone=phone, email=email, last_donation=date, location=address)
            
            message_body = f"Your Registration was successfull, Thank you,\n {first_name}.\n"
            email_message = EmailMessage("Registration form Submission Confirmation", message_body, to=[email])
            email_message.send()
            

            
            messages.success(request, "Registration Successfull")
    return render(request, "index.html")
