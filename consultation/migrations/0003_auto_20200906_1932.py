# Generated by Django 2.2.10 on 2020-09-06 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("consultation", "0002_auto_20200906_1254"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctorprofile",
            name="speciality",
            field=models.CharField(
                blank=True,
                choices=[
                    ("cardiac", "Cardiologist"),
                    ("ENT", "ENT specialist"),
                    ("gastrologist", "stomach and digestion"),
                    ("pediatrics", "pediatrics"),
                    ("dermatology", "skin specialist"),
                    ("dentist", "dentist"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="generalsymptom",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("cardiac", "Cardiologist"),
                    ("ENT", "ENT specialist"),
                    ("gastrologist", "stomach and digestion"),
                    ("pediatrics", "pediatrics"),
                    ("dermatology", "skin specialist"),
                    ("dentist", "dentist"),
                ],
                max_length=50,
                null=True,
                verbose_name="symptom_category",
            ),
        ),
        migrations.AlterField(
            model_name="qualification",
            name="degree",
            field=models.CharField(
                blank=True,
                choices=[
                    ("MBBS", "MBBS"),
                    ("BMBS", "BMBS"),
                    ("MBChB", "MBChB"),
                    ("MBBCh", "MBBCh"),
                    ("MD", "MD"),
                    ("Dr.MuD", "Dr.MuD"),
                    ("Dr.Med", "Dr.Med"),
                    ("DO", "DO"),
                    ("PhD", "PhD"),
                    ("DPhil", "DPhil"),
                    ("MCM", "MCM"),
                    ("MS", "MS"),
                    ("MPhil", "MPhil"),
                    ("DMedSc", "DMedSc"),
                    ("DMSc", "DMSc"),
                    ("DS", "DS"),
                    ("DSurg", "DSurg"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]