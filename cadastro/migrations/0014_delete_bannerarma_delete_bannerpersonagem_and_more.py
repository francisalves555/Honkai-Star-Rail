# Generated by Django 4.2.6 on 2024-07-21 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0013_ocorrenciabannerarma_ocorrenciabannerpersonagem'),
        ('tiro', '0007_remove_ocorrenciabannerpersonagem_banner_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BannerArma',
        ),
        migrations.DeleteModel(
            name='BannerPersonagem',
        ),
        migrations.AddField(
            model_name='ocorrenciabannerpersonagem',
            name='banner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ocorrencias', to='cadastro.banner_personagem'),
        ),
        migrations.AddField(
            model_name='ocorrenciabannerarma',
            name='banner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ocorrencias', to='cadastro.banner_arma'),
        ),
    ]
