# Generated by Django 3.2.21 on 2023-10-19 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_alter_review_user_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='recommended',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
