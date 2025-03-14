# Generated by Django 5.1.6 on 2025-02-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0008_reservations_adults_reservations_children'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservations',
            name='guest_name',
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='room',
        ),
        migrations.AddField(
            model_name='reservations',
            name='guest_fullname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='arrival_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='departure_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='guest_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
