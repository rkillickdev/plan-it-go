# Generated by Django 3.2.21 on 2023-09-20 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0002_rename_longtitude_location_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11)),
                ('category', models.CharField(max_length=50)),
                ('rank', models.IntegerField()),
                ('tags', models.JSONField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='locations.location')),
            ],
            options={
                'ordering': ['-rank'],
            },
        ),
    ]
