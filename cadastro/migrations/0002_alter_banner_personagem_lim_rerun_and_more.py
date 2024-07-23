# Generated by Django 4.2.6 on 2023-10-16 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner_personagem_lim',
            name='rerun',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='banner_personagem_lim',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'Destruição'), (2, 'Caça'), (3, 'Abundância'), (4, 'Preservação'), (5, 'Inexistência'), (6, 'Harmonia'), (7, 'Erudição')]),
        ),
    ]