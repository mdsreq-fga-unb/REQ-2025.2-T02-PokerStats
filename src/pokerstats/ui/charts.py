import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.dates as mdates
import customtkinter as ctk

def _cores():
    tema = ctk.get_appearance_mode()
    if tema == "Dark":
        return {
            "fundo": "#2b2b2b",
            "texto": "white",
            "verde": "#2ecc71",
            "vermelho": "#e74c3c",
            "azul": "#3498db",
            "cinza": "#555"
        }
    return {
        "fundo": "white",
        "texto": "black",
        "verde": "#27ae60",
        "vermelho": "#c0392b",
        "azul": "#2980b9",
        "cinza": "#777"
    }

def _aplicar_estilo_matplotlib():
    tema = ctk.get_appearance_mode()
    if tema == "Dark":
        plt.style.use("dark_background")
    else:
        plt.style.use("default")

def _configurar_figura(ax, titulo, C):
    ax.set_facecolor(C["fundo"])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color(C["cinza"])
    ax.spines['left'].set_color(C["cinza"])
    ax.tick_params(axis='x', colors=C["texto"], labelsize=7)
    ax.tick_params(axis='y', colors=C["texto"], labelsize=7)
    ax.set_title(titulo, fontsize=9, fontweight='bold', color=C["texto"], pad=10)

def criar_figura_base():
    _aplicar_estilo_matplotlib()
    C = _cores()
    fig = Figure(figsize=(5, 4), facecolor=C["fundo"], layout='tight')
    return fig

def gerar_grafico_evolucao(dados):
    C = _cores()
    fig = criar_figura_base()
    ax = fig.add_subplot(111)
    if not dados:
        ax.text(0.5, 0.5, "Sem dados", ha='center', color=C["texto"])
        return fig
    df = pd.DataFrame([{
        'data': d.data_inicio,
        'lucro': (d.resultado.lucro if d.resultado else 0.0)
    } for d in dados])
    if df.empty: 
        return fig
    df = df.sort_values('data')
    df['acumulado'] = df['lucro'].cumsum()
    ax.plot(df['data'], df['acumulado'], color=C["azul"], linewidth=1.5)
    ax.fill_between(df['data'], df['acumulado'], 0, color=C["azul"], alpha=0.1)
    ax.axhline(0, color=C["cinza"], linestyle='--', linewidth=0.8)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    fig.autofmt_xdate(rotation=30, ha='right')
    _configurar_figura(ax, "Evolução do Bankroll", C)
    return fig

def gerar_grafico_modalidades(dados):
    C = _cores()
    fig = criar_figura_base()
    ax = fig.add_subplot(111)
    if not dados:
        return fig
    categorias = {'MTT': 0.0, 'SNG': 0.0, 'Outros': 0.0}
    for d in dados:
        nome = (d.nome_torneio or "").upper()
        lucro = d.resultado.lucro if d.resultado else 0.0
        inv = d.buy_in or 0.0
        if inv == 0 and lucro > 0:
            cat = 'Outros'
        elif 'SIT' in nome or 'SNG' in nome:
            cat = 'SNG'
        elif 'CASH' in nome:
            cat = 'Outros'
        else:
            cat = 'MTT'
        categorias[cat] += lucro
    names = list(categorias.keys())
    values = list(categorias.values())
    colors = [C["verde"] if v >= 0 else C["vermelho"] for v in values]
    ax.bar(names, values, color=colors, width=0.4)
    ax.axhline(0, color=C["cinza"], linewidth=0.8)
    _configurar_figura(ax, "Lucro por Modalidade", C)
    return fig

def gerar_grafico_itm(dados):
    C = _cores()
    fig = criar_figura_base()
    ax = fig.add_subplot(111)
    itm = sum(1 for d in dados if (d.premio or 0) > 0)
    total = len(dados)
    if total == 0:
        return fig
    otm = total - itm
    wedges, texts, autotexts = ax.pie(
        [itm, otm], labels=['ITM', ''],
        colors=[C["verde"], C["cinza"]],
        autopct='%1.1f%%', startangle=90,
        pctdistance=0.85,
        textprops={'color': C["texto"], 'fontsize': 8}
    )
    centre_circle = plt.Circle((0,0), 0.70, fc=C["fundo"])
    ax.add_artist(centre_circle)
    ax.set_title("Taxa de ITM", fontsize=9, fontweight='bold', color=C["texto"], pad=5)
    return fig

def gerar_grafico_scatter(dados):
    C = _cores()
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
        colors = [C["verde"] if r > 0 else C["vermelho"] for r in rois]
        ax.scatter(buyins, rois, c=colors, alpha=0.6, edgecolors='none', s=15)
    ax.axhline(0, color=C["cinza"], linestyle='--', linewidth=0.8)
    _configurar_figura(ax, "ROI vs Buy-in", C)
    return fig
