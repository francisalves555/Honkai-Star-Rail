# Generated by Django 4.2.6 on 2023-10-19 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_alter_banner_personagem_lim_data_final'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner_personagem_lim',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Destruição'), (2, 'Caça'), (3, 'Abundância'), (4, 'Preservação'), (5, 'Inexistência'), (6, 'Harmonia'), (7, 'Erudição')], null=True),
        ),
    ]
