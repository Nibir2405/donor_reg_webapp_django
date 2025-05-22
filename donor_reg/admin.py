from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "blood_group")
    search_fields = ("first_name", "blood_group")
    list_filter =("last_donation", "blood_group")
    ordering = ("first_name", )
    #readonly_fields = ("blood_group", )
admin.site.register(Form, FormAdmin)
