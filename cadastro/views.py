from django.shortcuts import render, redirect
from .models import banner_personagem, banner_arma, OcorrenciaBannerArma, OcorrenciaBannerPersonagem
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def personagem(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        data_inicio = request.POST.get('data_inicio')
        data_final = request.POST.get('data_final')
        caminho = request.POST.get('caminho')
        foto = request.FILES.get('foto')
        foto_m = request.FILES.get('mini-foto')
        tipo_str = request.POST.get('tipo', 'False')  # Valor padrão 'False' se não houver seleção
        tipo = tipo_str.lower() == 'true'  # Converte para valor booleano

        if not data_inicio:
            data_inicio = None
        if not data_final:
            data_final = None

        BN_personagem = banner_personagem(
                    nome = nome,
                    caminho = caminho, 
                    foto = foto,
                    foto_m = foto_m,
                    tipo = tipo
                )
        BN_personagem.save()
        
        OC_personagem = OcorrenciaBannerPersonagem(
                    banner = BN_personagem,
                    data_inicio = data_inicio, 
                    data_final = data_final,
                    numero_ocorrencia = 0,
        )
        OC_personagem.save()
        

    messages.add_message(request, constants.SUCCESS, 'Cadastro efetuado com sucesso')
    return redirect('/cadastro/personagem/') 

def arma(request):
    if request.method == 'GET':
        return render(request, 'cadastro_arma.html')
    
    else:
        nome_a = request.POST.get('nome')
        data_inicio_a = request.POST.get('data_inicio')
        data_final_a = request.POST.get('data_final')
        foto_a = request.FILES.get('foto')
        tipo_a_str = request.POST.get('tipo', 'False')
        tipo_a = tipo_a_str.lower() == 'true'

        if not data_inicio_a:
            data_inicio_a = None
        if not data_final_a:
            data_final_a = None
        
        BN_arma = banner_arma(
            nome_a = nome_a,
            foto_a = foto_a,
            tipo_a = tipo_a
        )
        BN_arma.save()

        OC_arma = OcorrenciaBannerArma(
            banner = BN_arma,
            data_inicio = data_inicio_a,
            data_final = data_final_a,
            numero_ocorrencia = 0,
        )
        OC_arma.save()

        messages.add_message(request, constants.SUCCESS, 'Cadastro efetuado com sucesso')
    return redirect('/cadastro/arma/') 

def reroll(request):
    if request.method == 'GET':
        personagens_comum = OcorrenciaBannerPersonagem.objects.filter(numero_ocorrencia=0).order_by('-data_inicio')
    else:
        nome = request.POST.get('nome')
        data_inicio = request.POST.get('data_inicio')
        data_final = request.POST.get('data_final')
        reroll = request.POST.get('reroll')

        RE_personagens = OcorrenciaBannerPersonagem(
            banner_id = nome,
            data_inicio = data_inicio,
            data_final = data_final,
            numero_ocorrencia = reroll,
        )
        RE_personagens.save()
        messages.add_message(request, constants.SUCCESS, 'Reroll cadastrado com sucesso')

    return render(request, 'cadastro_reroll.html', {'personagens_comum': personagens_comum})

def arma_reroll(request):
    armas_comum = OcorrenciaBannerArma.objects.filter(numero_ocorrencia=0).order_by('-data_inicio')
    if request.method == 'GET':
        armas_comum = OcorrenciaBannerArma.objects.filter(numero_ocorrencia=0).order_by('-data_inicio')
        
    if request.method == 'POST':
        nome_a = request.POST.get('nome')
        numero_ocorrencia = request.POST.get('reroll')
        data_inicio = request.POST.get('data_inicio')
        data_final = request.POST.get('data_final')
    
        RE_arma = OcorrenciaBannerArma(
            banner_id = nome_a,
            numero_ocorrencia = numero_ocorrencia,
            data_final = data_final,
            data_inicio = data_inicio,
        )
        RE_arma.save()
        messages.add_message(request, constants.SUCCESS, 'Reroll cadastrado com sucesso')

    return render(request, 'cadastro_arma_reroll.html',{ 'armas_comum':armas_comum })