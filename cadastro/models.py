from django.db import models

# Create your models here.
class banner_personagem(models.Model):
    caminho_choices=(
        (1, 'Destruição'),
        (2, 'Caça'),
        (3, 'Abundância'),
        (4, 'Preservação'),
        (5, 'Inexistência'),
        (6, 'Harmonia'),
        (7, 'Erudição')
    )
    nome = models.CharField(max_length=50)
    caminho = models.IntegerField(choices=caminho_choices, null=True, blank=True)
    foto = models.FileField(upload_to="foto", null=True, blank=True)
    foto_m = models.FileField(upload_to="mini-foto", null=True, blank=True)
    tipo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
    def get_caminho_choices(self):
        return self.caminho_choices
    
class banner_arma(models.Model):
    nome_a = models.CharField(max_length=50)
    foto_a = models.FileField(upload_to="foto")
    tipo_a = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_a
    
# Model para ocorrências de banners de personagens
class OcorrenciaBannerPersonagem(models.Model):
    banner = models.ForeignKey(banner_personagem, on_delete=models.CASCADE, related_name='ocorrencias')
    data_inicio = models.DateField()
    data_final = models.DateField()
    numero_ocorrencia = models.IntegerField()

    def __str__(self):
        return f"{self.banner.nome} ({self.numero_ocorrencia}ª vez: {self.data_inicio} - {self.data_final})"
    
# Model para ocorrências de banners de armas
class OcorrenciaBannerArma(models.Model):
    banner = models.ForeignKey(banner_arma, on_delete=models.CASCADE, related_name='ocorrencias')
    data_inicio = models.DateField()
    data_final = models.DateField()
    numero_ocorrencia = models.IntegerField()

    def __str__(self):
        return f"{self.banner.nome_a} ({self.numero_ocorrencia}ª vez: {self.data_inicio} - {self.data_final})"

