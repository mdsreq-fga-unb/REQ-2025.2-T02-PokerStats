import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.dates as mdates

# Estilo Global
plt.style.use('dark_background')
COR_VERDE = '#2ecc71'
COR_VERMELHO = '#e74c3c'
COR_AZUL = '#3498db'
COR_FUNDO = '#2b2b2b' 
COR_TEXTO = 'white'

def _configurar_figura(ax, titulo):
    ax.set_facecolor(COR_FUNDO)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#555')
    ax.spines['left'].set_color('#555')
    ax.tick_params(axis='x', colors=COR_TEXTO, labelsize=7)
    ax.tick_params(axis='y', colors=COR_TEXTO, labelsize=7)
    ax.set_title(titulo, fontsize=9, fontweight='bold', color=COR_TEXTO, pad=10)

def criar_figura_base():
    fig = Figure(figsize=(5, 4), facecolor=COR_FUNDO, layout='tight')
    return fig

def gerar_grafico_evolucao(dados):
    fig = criar_figura_base()
    ax = fig.add_subplot(111)
    
    if not dados:
        ax.text(0.5, 0.5, "Sem dados", ha='center', color='gray')
        return fig

    df = pd.DataFrame([{
        'data': d.data_inicio,
        'lucro': (d.resultado.lucro if d.resultado else 0.0)
    } for d in dados])
    
    if df.empty: return fig

    df = df.sort_values('data')
    df['acumulado'] = df['lucro'].cumsum()
    
    ax.plot(df['data'], df['acumulado'], color=COR_AZUL, linewidth=1.5)
    ax.fill_between(df['data'], df['acumulado'], 0, color=COR_AZUL, alpha=0.1)
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    fig.autofmt_xdate(rotation=30, ha='right')
    
    _configurar_figura(ax, "Evolução do Bankroll")
    return fig

def gerar_grafico_modalidades(dados):
    fig = criar_figura_base()
    ax = fig.add_subplot(111)

    if not dados: return fig

    categorias = {'MTT': 0.0, 'SNG': 0.0, 'Outros': 0.0}
    for d in dados:
        nome = (d.nome_torneio or "").upper()
        lucro = d.resultado.lucro if d.resultado else 0.0
        inv = d.buy_in or 0.0
        
        if inv == 0 and lucro > 0: cat = 'Outros'
        elif 'SIT' in nome or 'SNG' in nome: cat = 'SNG'
        elif 'CASH' in nome: cat = 'Outros'
        else: cat = 'MTT'
        categorias[cat] += lucro

    names = list(categorias.keys())
    values = list(categorias.values())
    colors = [COR_VERDE if v >= 0 else COR_VERMELHO for v in values]

    ax.bar(names, values, color=colors, width=0.4)
    ax.axhline(0, color='gray', linewidth=0.8)
    
    _configurar_figura(ax, "Lucro por Modalidade")
    return fig

def gerar_grafico_itm(dados):
    fig = criar_figura_base()
    ax = fig.add_subplot(111)

    itm = sum(1 for d in dados if (d.premio or 0) > 0)
    total = len(dados)
    otm = total - itm
    
    if total == 0: return fig

    wedges, texts, autotexts = ax.pie(
        [itm, otm], labels=['ITM', ''], colors=[COR_VERDE, '#444'], 
        autopct='%1.1f%%', startangle=90, pctdistance=0.85, 
        textprops={'color':"white", 'fontsize': 8}
    )
    
    centre_circle = plt.Circle((0,0), 0.70, fc=COR_FUNDO)
    ax.add_artist(centre_circle)
    ax.set_title("Taxa de ITM", fontsize=9, fontweight='bold', color=COR_TEXTO, pad=5)
    
    return fig

def gerar_grafico_scatter(dados):
    fig = criar_figura_base()
    ax = fig.add_subplot(111)

    buyins, rois = [], []
    for d in dados:
        b = d.buy_in or 0.0
        p = d.premio or 0.0
        if b > 0:
            roi = ((p - b) / b) * 100
            if roi < 5000: 
                buyins.append(b)
                rois.append(roi)

    if buyins:
        colors = [COR_VERDE if r > 0 else COR_VERMELHO for r in rois]
        ax.scatter(buyins, rois, c=colors, alpha=0.6, edgecolors='none', s=15)
    
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    _configurar_figura(ax, "ROI vs Buy-in")
    
    return fig