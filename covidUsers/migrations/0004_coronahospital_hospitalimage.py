# Generated by Django 2.2.10 on 2020-03-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidUsers', '0003_auto_20200325_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='coronahospital',
            name='hospitalImage',
            field=models.ImageField(blank=True, null=True, upload_to='media/uploads/', verbose_name='Hospital Image'),
        ),
    ]
