# Generated by Django 5.0 on 2024-01-26 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='status',
            field=models.CharField(choices=[('AWAITING', 'Awaiting Authorization'), ('IN_VISIT', 'In Visit'), ('FINALIZED', 'Visit has been finalized')], default='AWAITING', max_length=10, verbose_name='Status'),
        ),
    ]
