# Generated by Django 4.2.6 on 2024-07-21 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0013_ocorrenciabannerarma_ocorrenciabannerpersonagem'),
        ('tiro', '0006_ocorrenciabannerarma_ocorrenciabannerpersonagem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ocorrenciabannerpersonagem',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='tiroarma',
            name='ocorrencia',
        ),
        migrations.RemoveField(
            model_name='tiropersonagem',
            name='ocorrencia',
        ),
        migrations.AddField(
            model_name='tiro_b_arma',
            name='ocorrencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastro.ocorrenciabannerarma'),
        ),
        migrations.AddField(
            model_name='tiro_b_personagem',
            name='ocorrencia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastro.ocorrenciabannerpersonagem'),
        ),
        migrations.DeleteModel(
            name='OcorrenciaBannerArma',
        ),
        migrations.DeleteModel(
            name='OcorrenciaBannerPersonagem',
        ),
        migrations.DeleteModel(
            name='TiroArma',
        ),
        migrations.DeleteModel(
            name='TiroPersonagem',
        ),
    ]
