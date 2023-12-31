# Generated by Django 3.2.21 on 2023-09-15 22:26

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('summary', models.TextField()),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longtitude', models.DecimalField(decimal_places=8, max_digits=11)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
            options={
                'ordering': ['-city'],
            },
        ),
    ]
