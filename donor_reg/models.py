from django.db import models

class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    blood_group = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    last_donation = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

