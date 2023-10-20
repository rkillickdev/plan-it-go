# Generated by Django 3.2.21 on 2023-10-20 10:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_auto_20231020_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user_rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
