# Generated by Django 4.2.6 on 2023-10-20 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiro_limitado',
            old_name='data_adc',
            new_name='data_adc_L',
        ),
        migrations.RenameField(
            model_name='tiro_limitado',
            old_name='num_T',
            new_name='num_TL',
        ),
    ]
