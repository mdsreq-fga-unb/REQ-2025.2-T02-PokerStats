def formatar_moeda(valor):
    try:
        valor = float(valor)
    except:
        return "$ 0,00"
        
    sinal = "- " if valor < 0 else ""
    valor_abs = abs(valor)
    
    texto_us = f"{valor_abs:,.2f}"
    texto_br = texto_us.replace(",", "X").replace(".", ",").replace("X", ".")
    
    return f"{sinal}$ {texto_br}"

def formatar_pct(valor):
    return f"{valor:.2f}%"