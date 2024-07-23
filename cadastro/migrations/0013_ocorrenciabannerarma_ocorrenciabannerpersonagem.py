# Generated by Django 4.2.6 on 2024-07-21 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0012_bannerarma_bannerpersonagem_delete_bannerarmaantigo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OcorrenciaBannerArma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_final', models.DateField()),
                ('numero_ocorrencia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OcorrenciaBannerPersonagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_final', models.DateField()),
                ('numero_ocorrencia', models.IntegerField()),
            ],
        ),
    ]