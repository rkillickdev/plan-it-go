# Generated by Django 3.2.21 on 2023-10-12 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_rename_rating_place_ratings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='ratings',
            new_name='rating',
        ),
    ]
