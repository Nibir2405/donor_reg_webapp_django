# Generated by Django 5.2.1 on 2025-05-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('blood_group', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=80)),
                ('last_donation', models.DateField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
