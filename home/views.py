from django.shortcuts import render, redirect
import io
import os
import calendar
import matplotlib
import numpy as np
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict
from django.conf import settings
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.db.models import F, Value, CharField, When, Case, Count, Sum
from tiro.models import tiro_b_personagem, tiro_b_arma
from cadastro.models import banner_personagem, banner_arma, OcorrenciaBannerPersonagem, OcorrenciaBannerArma
import matplotlib.colors as mcolors
# Create your views here.

def home(request):
    total_count = 0
    counts = {}
    for caminho in range(1, 8):
        tipo = banner_personagem.objects.filter(caminho=caminho)
        count = tiro_b_personagem.objects.filter(ocorrencia__banner__caminho=caminho).count()
        counts[f'count_{caminho}'] = count
        total_count += count

    dados_tiro_p = tiro_b_personagem.objects.all().order_by('-data_adc')
    dados_tiros_a = tiro_b_arma.objects.all().order_by('-data_tadc')
    total_num_t = tiro_b_personagem.objects.aggregate(total=Sum('num_t'))['total']
    total_gem = total_num_t * 160
    
    #----- GRAFICO 1 TODOS OS PERSONAGENS -----  
   # Agrupar dados por mês e calcular o total de tiros
    tiroC = tiro_b_personagem.objects.values('data_adc', 'num_t')

    monthly_data = defaultdict(int)
    for item in tiroC:
        month = item['data_adc'].strftime('%B')
        monthly_data[month] += item['num_t']

    # Ordenar os dados por mês
    ordered_months = list(calendar.month_name)[1:]  # lista de meses do ano
    nome = [month for month in ordered_months if month in monthly_data]
    valores = [monthly_data[month] for month in nome]

    # Seu código para criar o gráfico
    fig, ax = plt.subplots(figsize=(16, 6))
    colors = list(mcolors.TABLEAU_COLORS.values())
    bars = ax.bar(nome, valores, color=colors[:len(nome)])

    for bar, valor in zip(bars, valores):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(valor), ha='center', va='bottom')

    ax.set_title('Lista completa de tiros por mês no banner de personagem')
    ax.set_xlabel('')
    ax.set_ylabel('Número de Tiros')

    # Converta a figura em bytes
    buffer = io.BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buffer)

    # Crie um nome de arquivo temporário
    image_file = os.path.join(settings.MEDIA_ROOT, 'temp_barras.png')

    # Salve o gráfico no arquivo temporário
    with open(image_file, 'wb') as f:
        f.write(buffer.getvalue())

    # Retorna o URL da imagem
    Barras = os.path.join(settings.MEDIA_URL, 'temp_barras.png')

    caminho_choices = {
        1: 'Destruição',
        2: 'Caça',
        3: 'Abundância',
        4: 'Preservação',
        5: 'Inexistência',
        6: 'Harmonia',
        7: 'Erudição'
    }

    # Contagem de tiros por caminho
    counts_name = {
        caminho_choices[1]: tiro_b_personagem.objects.filter(ocorrencia__banner__caminho=1).count(),
        caminho_choices[2]: tiro_b_personagem.objects.filter(ocorrencia__banner__caminho=2).count(),
        caminho_choices[3]: tiro_b_personagem.objects.filter(ocorrencia__banner__caminho=3).count(),
        caminho_choices[4]: tiro_b_personagem.objects.filter(ocorrencia__banner__caminho=4).count(),
        caminho_choices[5]: tiro_b_personagem.objects.filter(ocorrencia__banner__caminho=5).count(),
        caminho_choices[6]: tiro_b_personagem.objects.filter(ocorrencia__banner__caminho=6).count(),
        caminho_choices[7]: tiro_b_personagem.objects.filter(ocorrencia__banner__caminho=7).count()
    }

    #----- GRAFICO 2 CAMINHOS -----  
    # Dados para o gráfico
    data = list(counts_name.values())
    labels = list(counts_name.keys())

    # Configuração do gráfico
    fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(aspect="equal"))

    # Criar gráfico de pizza (ou de rosca)
    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    # Propriedades da anotação
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
            bbox=bbox_props, zorder=0, va="center")

    # Adicionar anotações
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)

    # Título do gráfico
    ax.set_title("")

    # Mostrar gráfico
    plt.show()

        # Converta a figura em bytes
    buffer = io.BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buffer)

    # Crie um nome de arquivo temporário
    image_file = os.path.join(settings.MEDIA_ROOT, 'temp_pizza.png')

    # Salve o gráfico no arquivo temporário
    with open(image_file, 'wb') as f:
        f.write(buffer.getvalue())

    # Retorna o URL da imagem
    Pizza = os.path.join(settings.MEDIA_URL, 'temp_pizza.png')
    
    # Feche a figura para liberar memória
    plt.close(fig)
    

        #----- GRAFICO 3 TODOS ASARMAS -----  
   # Agrupar dados por mês e calcular o total de tiros
    tiroC = tiro_b_arma.objects.values('data_tadc', 'num_ta')

    monthly_data = defaultdict(int)
    for item in tiroC:
        month = item['data_tadc'].strftime('%B')
        monthly_data[month] += item['num_ta']

    # Ordenar os dados por mês
    ordered_months = list(calendar.month_name)[1:]  # lista de meses do ano
    nome = [month for month in ordered_months if month in monthly_data]
    valores = [monthly_data[month] for month in nome]

    # Seu código para criar o gráfico
    fig, ax = plt.subplots(figsize=(16, 6))
    colors = list(mcolors.TABLEAU_COLORS.values())
    bars = ax.bar(nome, valores, color=colors[:len(nome)])

    for bar, valor in zip(bars, valores):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(valor), ha='center', va='bottom')

    ax.set_title('Lista completa de tiros por mês no banner de arma')
    ax.set_xlabel('')
    ax.set_ylabel('Número de Tiros')

    # Converta a figura em bytes
    buffer = io.BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buffer)

    # Crie um nome de arquivo temporário
    image_file = os.path.join(settings.MEDIA_ROOT, 'temp_barras_AR.png')

    # Salve o gráfico no arquivo temporário
    with open(image_file, 'wb') as f:
        f.write(buffer.getvalue())

    # Retorna o URL da imagem
    Barras_AR = os.path.join(settings.MEDIA_URL, 'temp_barras_AR.png')

    return render(request, 'home.html', {'Barras': Barras, 'Pizza':Pizza, 'dados_tiro_p':dados_tiro_p, 'total_gem':total_gem, 
                                         'counts':counts, 'total_count':total_count, 'total_num_t':total_num_t, 'dados_tiros_a':dados_tiros_a,
                                          'Barras_AR':Barras_AR })

import threading

print("Identificador da Thread Principal:", threading.current_thread().ident)


