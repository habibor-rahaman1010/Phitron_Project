# Generated by Django 4.2.3 on 2023-08-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstroemodel',
            name='last_publication',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
