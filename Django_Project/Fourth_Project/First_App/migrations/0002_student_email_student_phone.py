# Generated by Django 4.2.3 on 2023-08-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default='null', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(default='null', max_length=11, unique=True),
        ),
    ]
