# Generated by Django 3.2.21 on 2023-11-17 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0017_alter_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
