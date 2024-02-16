# Generated by Django 5.0.1 on 2024-01-26 01:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doorman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=194, verbose_name='Full Name')),
                ('ssn', models.CharField(max_length=9, verbose_name='SSN')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('apartment_number', models.PositiveSmallIntegerField(verbose_name='Apartment Number to be visited')),
                ('vehicle_plate', models.CharField(blank=True, max_length=7, null=True, verbose_name='Vehicle Plate Number')),
                ('arrival_time', models.DateTimeField(auto_now_add=True, verbose_name='Arrival Time of Guest')),
                ('checkout_time', models.DateTimeField(blank=True, null=True, verbose_name='Guest Checkout Time')),
                ('authorization_time', models.DateTimeField(blank=True, null=True, verbose_name='Time of Entry Authorization')),
                ('responsible_tenant', models.CharField(blank=True, max_length=194, verbose_name="Name of Tenant responsible for the guest's visit")),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doorman.doorman', verbose_name='Doorman responsible for registering this guest')),
            ],
            options={
                'verbose_name': 'Visitor',
                'verbose_name_plural': 'Visitors',
                'db_table': 'visitor',
            },
        ),
    ]
