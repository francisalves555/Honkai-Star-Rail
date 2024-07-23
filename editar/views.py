import os
from django.shortcuts import render, redirect
from cadastro.models import banner_personagem, banner_arma, OcorrenciaBannerArma, OcorrenciaBannerPersonagem
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime

def ed_personagem(request, id):
    # Busca a ocorrência específica
    dados_ocorrencia = OcorrenciaBannerPersonagem.objects.get(id=id)
    # Busca o banner relacionado
    dados_banner = dados_ocorrencia.banner

    if request.method == 'POST':
        # Atualiza os campos do banner relacionado
        dados_banner.nome = request.POST.get('nome')
        dados_banner.caminho = request.POST.get('caminho')
        dados_banner.tipo = request.POST.get('tipo') == 'True'
        
        # Atualiza os campos da ocorrência
        data_inicio = request.POST.get('data_inicio')
        if data_inicio:
            try:
                dados_ocorrencia.data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date()
            except ValueError:
                dados_ocorrencia.data_inicio = None

        data_final = request.POST.get('data_final')
        if data_final:
            try:
                dados_ocorrencia.data_final = datetime.strptime(data_final, '%Y-%m-%d').date()
            except ValueError:
                dados_ocorrencia.data_final = None

        if 'foto' in request.FILES:
            dados_banner.foto = request.FILES['foto']
        if 'mini-foto' in request.FILES:
            dados_banner.foto_m = request.FILES['mini-foto']
    
        # Salva as alterações
        dados_banner.save()
        dados_ocorrencia.save()

        messages.add_message(request, constants.SUCCESS, 'Editado com sucesso!')
        return redirect('lista_personagens')

    return render(request, 'ed_personagem.html', {
        'dados_ocorrencia': dados_ocorrencia,
        'dados_banner': dados_banner,
    })

def lista_personagens(request):
    if request.method == 'GET':
        dados_personagem = OcorrenciaBannerPersonagem.objects.filter(numero_ocorrencia__lt=1).order_by('-data_inicio')

    return render (request, 'lista_personagens.html', {'dados_personagem':dados_personagem })

def lista_reroll_personagens(request):
    if request.method == 'GET':
        dados_personagem = OcorrenciaBannerPersonagem.objects.filter(numero_ocorrencia__gte=1).order_by('-data_inicio')

    return render (request, 'lista_personagens.html', {'dados_personagem':dados_personagem })

def del_personagem(request, id):
    try:
        # Obtém o personagem
        personagem = banner_personagem.objects.get(id=id)

        if request.method == 'POST':
            # Verifica se o personagem tem fotos e exclui os arquivos
            if personagem.foto and os.path.isfile(personagem.foto.path):
                os.remove(personagem.foto.path)
            if personagem.foto_m and os.path.isfile(personagem.foto_m.path):
                os.remove(personagem.foto_m.path)

            # Exclui o personagem do banco de dados
            personagem.delete()
            messages.add_message(request, constants.SUCCESS, 'Deletado com sucesso')
            return redirect('lista_personagens')

    except banner_personagem.DoesNotExist:
        messages.add_message(request, constants.ERROR, 'Personagem não encontrado')
        return redirect('lista_personagens')

def del_OC_personagem(request, id):
    personagem = OcorrenciaBannerPersonagem.objects.get(id=id)

    if request.method == 'POST':
        personagem.delete()
        messages.add_message(request, constants.ERROR, 'Deletado com sucesso')

    return redirect('lista_personagens')

def lista_armas(request):
    dados_arma = OcorrenciaBannerArma.objects.filter(numero_ocorrencia__lt=1).order_by('-data_inicio')

    return render(request, 'lista_armas.html', {'dados_arma':dados_arma})

def lista_arma_reroll(request):
    dados_arma = OcorrenciaBannerArma.objects.filter(numero_ocorrencia__gte=1).order_by('-data_inicio')

    return render (request, 'lista_armas.html', {'dados_arma':dados_arma})

def ed_arma(request, id):
    OC_arma = OcorrenciaBannerArma.objects.get(id=id)
    arma = OC_arma.banner
    
    if request.method == 'POST':
        arma.nome_a = request.POST.get('nome')
        arma.tipo_a = request.POST.get('tipo') == 'True'
        
        data_inicio_a = request.POST.get('data_inicio')
        if data_inicio_a:
            try:
                OC_arma.data_inicio = datetime.strptime(data_inicio_a,'%Y-%m-%d').date()
            except ValueError:
                OC_arma.data_inicio = None

        data_final_a = request.POST.get('data_final')
        if data_final_a:
            try:
                OC_arma.data_final = datetime.strptime(data_final_a, '%Y-%m-%d').date()
            except ValueError:
                OC_arma.data_final = None

        if 'foto' in request.FILES:
            arma.foto_a = request.FILES['foto']

        arma.save()
        OC_arma.save()

        messages.add_message(request, constants.SUCCESS, 'Editado com sucesso')
        return redirect('lista_armas')

    return render(request, 'ed_arma.html', {'arma':arma, 'OC_arma':OC_arma})

def del_arma(request, id):
    try:
        arma = banner_arma.objects.get(id=id)

        if request.method == 'POST':
            if arma.foto_a and os.path.isfile(arma.foto_a.path):
                os.remove(arma.foto_a.path)

                arma.delete()
                messages.add_message(request, constants.ERROR, 'Deletado com sucesso')
        
            arma.delete()
            messages.add_message(request, constants.ERROR, 'Deletado com sucesso')
            return redirect('lista_armas')
    
    except banner_arma.DoesNotExist:
        messages.add_message(request, constants.ERROR, 'Personagem não encontrado')
        return redirect('lista_armas')

def del_OC_arma(request, id):

    arma = OcorrenciaBannerArma.objects.get(id=id)

    if request.method == 'POST':
        arma.delete()
        messages.add_message(request, constants.ERROR, 'Reroll deletado com sucesso')
    return redirect('lista_armas')
