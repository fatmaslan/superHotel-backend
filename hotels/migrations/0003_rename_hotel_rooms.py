# Generated by Django 5.1.6 on 2025-02-21 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_alter_hotel_created_at_alter_hotel_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hotel',
            new_name='Rooms',
        ),
    ]
