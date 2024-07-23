from django.db import models
from cadastro.models import banner_personagem, banner_arma, OcorrenciaBannerArma, OcorrenciaBannerPersonagem

# Create your models here.
class tiro_b_personagem(models.Model):
    num_t = models.IntegerField()
    data_adc = models.DateField()
    tipo_t = models.BooleanField(default=False)
    ocorrencia = models.ForeignKey(OcorrenciaBannerPersonagem, on_delete=models.CASCADE, null=True, blank=True)


class tiro_b_arma(models.Model):
    num_ta = models.IntegerField()
    data_tadc = models.DateField()
    tipo_ta = models.BooleanField(default=False)
    ocorrencia = models.ForeignKey(OcorrenciaBannerArma, on_delete=models.CASCADE, null=True, blank=True)


