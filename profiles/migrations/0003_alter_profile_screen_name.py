# Generated by Django 3.2.21 on 2023-11-05 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20230912_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='screen_name',
            field=models.CharField(max_length=25, null=True, unique=True),
        ),
    ]
