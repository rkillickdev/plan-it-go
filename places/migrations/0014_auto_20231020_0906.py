# Generated by Django 3.2.21 on 2023-10-20 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0013_auto_20231019_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(),
        ),
    ]
