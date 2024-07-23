from django.shortcuts import render, redirect
from cadastro.models import banner_personagem, banner_arma, OcorrenciaBannerArma, OcorrenciaBannerPersonagem
from .models import tiro_b_personagem, tiro_b_arma
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime

def cad_tiro_banner(request):
    personagens_comum = OcorrenciaBannerPersonagem.objects.filter(numero_ocorrencia__lt=1).order_by('-data_inicio')
    ocorrencia = OcorrenciaBannerPersonagem.objects.filter(numero_ocorrencia__gte=1).order_by('-data_inicio')

    if request.method == 'POST':
        nome = request.POST.get('nome') 
        nome_r = request.POST.get('nome_r')
        data_adc = request.POST.get('data_adc')
        num_t = request.POST.get('tiros')
        tipo_tst = request.POST.get('tipo', 'False')
        tipo_t = tipo_tst.lower() == 'true'

        verif_nome = nome if nome else nome_r
        ocorrencia_ints = OcorrenciaBannerPersonagem.objects.get(id=verif_nome)

        tiro_personagem = tiro_b_personagem(
            num_t=num_t,
            data_adc=data_adc,
            tipo_t = tipo_t,
            ocorrencia = ocorrencia_ints,
        )
        tiro_personagem.save()

        messages.add_message(request, constants.SUCCESS, 'Cadastro efetuado com sucesso')
        return redirect('/tiro/cad_tiro_banner/')  # Redirecione para a página apropriada após o cadastro

    return render(request, 'tiro_comum.html', {'personagens_comum': personagens_comum, 'ocorrencia':ocorrencia})


def cad_tiro_arma(request):
    armas_comum = OcorrenciaBannerArma.objects.filter(numero_ocorrencia__lt=1).order_by('-data_inicio')
    armas_ocorrencia = OcorrenciaBannerArma.objects.filter(numero_ocorrencia__gte=1).order_by('-data_inicio')

    if request.method == 'POST':
        nome = request.POST.get('nome') 
        nome_r = request.POST.get('nome_r') 
        data_tadc = request.POST.get('data_adc')
        num_ta = request.POST.get('tiros')
        tipo_atst = request.POST.get('tipo', 'False')
        tipo_ta = tipo_atst.lower() == 'true'

        verif_nome = nome if nome else nome_r
        armas_comum = OcorrenciaBannerArma.objects.get(id=verif_nome)

        tiro_a = tiro_b_arma(
            ocorrencia=armas_comum,
            data_tadc=data_tadc,
            num_ta=num_ta,
            tipo_ta = tipo_ta
        )
        tiro_a.save()

        messages.add_message(request, constants.SUCCESS, 'Cadastro efetuado com sucesso')
        return redirect('/tiro/cad_tiro_arma/')

    return render(request, 'tiro_arma.html', {'armas_comum':armas_comum, 'armas_ocorrencia':armas_ocorrencia})

def lista_tiros_personagens(request):
    tds_tiros = tiro_b_personagem.objects.all().order_by('-data_adc')
    
    return render(request, 'lista_tiros_personagens.html', {'tds_tiros':tds_tiros})

def lista_tiros_armas(request):
    tds_armas = tiro_b_arma.objects.all().order_by('-data_tadc')

    return render(request, 'lista_tiros_armas.html', {'tds_armas':tds_armas})

def ed_tiro_personagem(request,id):
    info_tiro = tiro_b_personagem.objects.get(id=id)

    if request.method == 'POST':

        nome = request.POST.get('nome') 
        data = request.POST.get('data_adc')
        tiros = request.POST.get('tiros') 
        tipo = request.POST.get('tipo') == 'True'

        if data:
            try:
                info_tiro.data_adc = datetime.strptime(data, '%Y-%m-%d').date()
            except ValueError:
                info_tiro.data_adc = None

        info_tiro.num_t = tiros
        info_tiro.tipo_t = tipo

        if nome:
            banner = info_tiro.ocorrencia.banner
            banner.nome = nome
            banner.save()

        info_tiro.save()

        messages.add_message(request, constants.SUCCESS, 'Editado com sucesso')
    return render(request, 'ed_tiro_personagem.html', { 'info_tiro':info_tiro, 'personagens_comum':[info_tiro.ocorrencia] })

def ed_tiro_arma(request, id):
    info_tiro = tiro_b_arma.objects.get(id=id)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_adc = request.POST.get('data_adc')
        numero_ocorrencia = request.POST.get('numero_ocorrencia')
        tiros = request.POST.get('tiros')
        tipo = request.POST.get('tipo') == 'True'

        if data_adc:
            try:
                info_tiro.data_tadc = datetime.strptime(data_adc, '%Y-%m-%d').date()
            except ValueError:
                info_tiro.data_tadc = None

        info_tiro.num_ta = tiros
        info_tiro.tipo_ta = tipo

        if nome:
            banner = info_tiro.ocorrencia.banner
            banner.nome_a = nome
            banner.save()

        info_tiro.save()
        messages.add_message(request, constants.SUCCESS, 'Editado com sucesso')
    return render(request, 'ed_tiro_arma.html', {'info_tiro':info_tiro})

def del_tiro_personagem(request,id):
    del_tiro = tiro_b_personagem.objects.get(id=id)

    del_tiro.delete()
    messages.add_message(request, constants.ERROR, 'Deletado com sucesso')

    return redirect('lista_tiros_personagens')

def del_tiro_arma(request, id):
    del_tiro = tiro_b_arma.objects.get(id=id)

    del_tiro.delete()
    messages.add_message(request, constants.ERROR, 'Deletado com sucesso')

    return redirect('lista_tiros_personagens')