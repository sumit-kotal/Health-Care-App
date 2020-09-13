# Generated by Django 2.2.10 on 2020-09-13 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='xrayfield',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_xrays', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='xrayfield',
            name='uploaded_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_xrays', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='qualification',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qualification', to='consultation.DoctorProfile', verbose_name='doctor_profile'),
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL, verbose_name='customUser'),
        ),
        migrations.AddField(
            model_name='generalsymptom',
            name='assigned_doctor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='assigned_doctor', to=settings.AUTH_USER_MODEL, verbose_name='doctor'),
        ),
        migrations.AddField(
            model_name='generalsymptom',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='symptoms_category', to='consultation.SpecialityTag', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='generalsymptom',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by_patient', to=settings.AUTH_USER_MODEL, verbose_name='patient'),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='doctor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL, verbose_name='customUser'),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='patients',
            field=models.ManyToManyField(related_name='patients', to=settings.AUTH_USER_MODEL, verbose_name='patients'),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='speciality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_profile', to='consultation.SpecialityTag', verbose_name='speciality_tag'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='symptoms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultation', to='consultation.GeneralSymptom', verbose_name='symptoms_data'),
        ),
    ]
