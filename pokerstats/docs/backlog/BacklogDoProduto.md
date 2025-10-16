cat > 9_backlog_de_produto.md << 'EOF'
# 9. BACKLOG DE PRODUTO

## 9.1 Backlog Geral

### ÉPICO 1 — Importação e Consolidação de Dados
- **US01:** Importar arquivos de histórico (evitar duplicações e erros).

### ÉPICO 2 — Análise e Métricas de Desempenho
- **US02:** Calcular Lucro Total.
- **US03:** Calcular Taxa de Vitórias.
- **US04:** Calcular ROI.
- **US05:** Visualizar histórico de transações.

### ÉPICO 3 — Visualização e Relatórios
- **US06:** Apresentar resumo de desempenho.
- **US07:** Filtrar relatórios e análises.
- **US08:** Gerar relatórios comparativos.
- **US09:** Garantir interface minimalista.

### ÉPICO 4 — Desempenho e Distribuição
- **US10:** Otimizar processamento de grandes volumes.
- **US11:** Distribuir como executável (.exe).

---

## 9.2 Priorização do Backlog Geral

**Priorização dos Requisitos Funcionais do Poker Stats**  
A tabela a seguir apresenta a priorização dos requisitos com base no valor de negócio (MoSCoW) e na complexidade técnica. Os requisitos do MVP (“Must Have”) aparecem destacados.

| **ID**   | **Descrição**                                 | **Esforço** | **Prioridade** | **MVP** |
|:--------:|:----------------------------------------------|:-----------:|:--------------:|:-------:|
| **RF01** | **Importar histórico de torneios**            |     G       |   Must have    |   ✅    |
| **RF02** | **Calcular Lucro Total**                      |     P       |   Must have    |   ✅    |
| **RF03** | **Calcular ROI**                              |     P       |   Must have    |   ✅    |
|  RF04    | Calcular Taxa de Vitória                      |     P       |  Should have   |         |
|  RF05    | Segmentar Análises por jogador                |     G       |  Should have   |         |
| **RF06** | **Segmentar Análises por tipo de torneio**    |     G       |   Must have    |   ✅    |
|  RF07    | Visualizar Gráfico de Linha de Evolução        |     M       |  Could have    |         |
|  RF08    | Listar Histórico de Importações               |     M       |  Could have    |         |
|  RF09    | Exibir Histórico de Transações                |     P       |  Should have   |         |
| **RF10** | **Calcular ITM (In The Money)**               |     P       |   Must have    |   ✅    |

---

## 9.3 MVP

O MVP contém:
- US01 — Importar histórico  
- US02 — Calcular lucro total  
- US06 — Resumo de desempenho  
- US11 — Distribuição em .exe  

Essas histórias entregam o valor essencial: **consolidar dados e apresentar lucro de forma simples e automática.**

EOF
