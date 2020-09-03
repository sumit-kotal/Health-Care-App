# Generated by Django 2.2.10 on 2020-04-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidUsers', '0024_auto_20200416_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='isVolunteer',
        ),
        migrations.AddField(
            model_name='customuser',
            name='Volunteer',
            field=models.CharField(blank=True, choices=[('D', 'Doctor'), ('C', 'Counsellor'), ('O', 'Others')], max_length=2, null=True),
        ),
    ]
