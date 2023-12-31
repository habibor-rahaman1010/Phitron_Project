# Generated by Django 4.2.3 on 2023-08-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_App', '0002_student_email_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
