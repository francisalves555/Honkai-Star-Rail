# Generated by Django 4.2.6 on 2023-10-19 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_alter_banner_personagem_lim_data_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner_personagem_lim',
            name='data_final',
            field=models.DateField(blank=True, null=True),
        ),
    ]
