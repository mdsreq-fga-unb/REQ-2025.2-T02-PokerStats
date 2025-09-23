# Página 1

# Requisitos do Sistema Poker Stats

## 1. Requisitos Funcionais (RFs)

### 1.1 Importação de Dados

**RF001:** O sistema deve permitir a importação de arquivos de histórico de transações da plataforma Bodog.  
- **Prioridade:** Alta  
- **Justificativa:** Essencial para a coleta de dados e funcionamento do sistema.  
- **Características:** O sistema deve ser capaz de processar arquivos em formato CSV (ou similar, conforme disponibilizado pela Bodog).  

---

### 1.2 Resumos Financeiros

**RF002:** O sistema deve gerar um resumo financeiro geral.  
- **Prioridade:** Alta  
- **Justificativa:** Atende à necessidade principal do usuário de ter uma visão financeira consolidada.  
- **Características:** Deve incluir Período das transações, Saldo Inicial, Saldo Final e ROI Geral.  

**RF003:** O sistema deve gerar um resumo financeiro para torneios Sit & Go.  
- **Prioridade:** Média  
- **Justificativa:** Fornece análise específica para um tipo de jogo relevante para o usuário.  
- **Características:** Deve incluir quantidade de torneios, ITM (In The Money), Lucros Sit & Go e ROI Sit & Go.  

**RF004:** O sistema deve gerar um resumo financeiro para torneios programados.  

---

# Página 2

### 1.3 Performance dos Jogos

**RF005:** O sistema deve apresentar a performance geral dos jogos.  
- **Prioridade:** Média  
- **Justificativa:** Permite ao usuário identificar padrões de desempenho.  
- **Características:** Deve incluir total de torneios e ITM.  

**RF006:** O sistema deve apresentar o desempenho por torneio individual.  
- **Prioridade:** Média  
- **Justificativa:** Detalha o desempenho em cada torneio para análise aprofundada.  
- **Características:** Deve incluir Nome do torneio, Valor (buy-in/premiação), Horário, Quantidade de partidas, ITM e Lucro.  

---

### 1.4 Transações e Transferências

**RF007:** O sistema deve registrar e exibir transferências realizadas e recebidas.  
- **Prioridade:** Média  
- **Justificativa:** Importante para o controle financeiro completo da banca.  
- **Características:** Deve incluir Data, Valor e Referência da transação.  

---

### 1.5 Visualização e Filtragem

**RF008:** O sistema deve permitir a visualização de métricas essenciais (lucro, ROI, % vitórias) em relatórios rápidos e confiáveis.  
- **Prioridade:** Alta  
- **Justificativa:** Atende ao objetivo de eliminar a “cegueira estatística”.  
- **Características:** Relatórios devem ser gerados em menos de 60 segundos em 90% dos casos.  

---

# Página 3

**RF009:** O sistema deve permitir a aplicação de filtros de análise por modalidade e tipo de torneio.  
- **Prioridade:** Média  
- **Justificativa:** Ajuda na identificação de padrões de desempenho.  
- **Características:** Filtros devem ser intuitivos e de fácil uso.  

**RF010:** O sistema deve fornecer comparativos históricos para acompanhar a evolução do jogador ao longo do tempo.  
- **Prioridade:** Média  
- **Justificativa:** Permite ao jogador ajustar estratégias com base em dados concretos.  
- **Características:** Deve permitir a comparação de métricas (lucro, ROI, % vitórias) em diferentes períodos.  

---

# 2. Requisitos Não Funcionais (RNFs)

### 2.1 Usabilidade

**RNF001:** O sistema deve possuir uma interface de usuário intuitiva e de fácil compreensão.  
- **Prioridade:** Alta  
- **Justificativa:** O público-alvo (jogadores casuais) busca uma solução minimalista e acessível.  
- **Características:** Foco em UI/UX simples, sem sobrecarga de informações.  

**RNF002:** O sistema deve ser acessível para usuários com familiaridade tecnológica básica.  
- **Prioridade:** Média  
- **Justificativa:** Amplia a base de usuários e facilita a adoção.  

---

# Página 4

### 2.2 Desempenho

**RNF003:** O sistema deve processar grandes volumes de dados de forma rápida e eficiente.  
- **Prioridade:** Alta  
- **Justificativa:** Crucial para a experiência do usuário e credibilidade das estatísticas.  
- **Características:** Geração de relatórios em menos de 60 segundos em 90% dos casos.  

**RNF004:** A arquitetura do sistema deve ser escalável para suportar um número crescente de usuários e volume de dados.  
- **Prioridade:** Média  
- **Justificativa:** Garante a sustentabilidade e crescimento futuro do produto.  

---

### 2.3 Confiabilidade

**RNF005:** O sistema deve ser resiliente a incompletudes ou erros nos arquivos de origem da Bodog.  
- **Prioridade:** Alta  
- **Justificativa:** Os dados da plataforma podem ser limitados ou inconsistentes.  
- **Características:** Métodos inteligentes para inferir ou complementar informações ausentes.  

**RNF006:** O sistema deve garantir a integridade, precisão e ausência de duplicações nos dados processados.  
- **Prioridade:** Alta  
- **Justificativa:** Fundamental para a credibilidade das estatísticas geradas.  

---

### 2.4 Manutenibilidade e Adaptabilidade

**RNF007:** O sistema deve ser flexível para se adaptar a mudanças nos formatos de logs ou interfaces da plataforma Bodog.  
- **Prioridade:** Média  
- **Justificativa:** Garante a continuidade da coleta e processamento de dados a longo prazo.  

---

# Página 5

### 2.5 Requisitos de Implementação

**RNF008:** O sistema deve ser desenvolvido utilizando a linguagem Python.  
- **Prioridade:** Alta  
- **Justificativa:** Experiência da equipe e robustez da linguagem para análise de dados.  

**RNF009:** O sistema deve ser empacotado como um executável (.exe) para Windows.  
- **Prioridade:** Alta  
- **Justificativa:** Facilidade de instalação e uso no ambiente do cliente (Windows).  

**RNF010:** O sistema deve utilizar tecnologias leves de banco de dados para armazenamento local.  
- **Prioridade:** Média  
- **Justificativa:** Manter histórico de importações e relatórios de forma eficiente.  

---

# 3. Dados e Relatórios Exigidos

### 3.1 Dados de Entrada

**DE001:** Arquivos de histórico de transações da plataforma Bodog (formato CSV ou similar).  
- **Campos esperados:** Data, Descrição, Referência, Cash Amount, Bonus Amount, Points, Cash Before, Cash After.  

### 3.2 Relatórios e Métricas de Saída

**RS001:** Resumo Financeiro Geral  
- Métricas: Período das transações, Saldo Inicial, Saldo Final, ROI Geral.  

**RS002:** Resumo Financeiro Sit & Go  
- Métricas: Quantidade de torneios, ITM, Lucros Sit & Go, ROI Sit & Go.  

**RS003:** Resumo Financeiro Torneios Programados  
- Métricas: ITM, Lucros, ROI.  

**RS004:** Performance Geral dos Jogos  
- Métricas: Total de torneios, ITM.  

**RS005:** Desempenho por Torneio Individual  
- Métricas: Nome, Valor (buy-in/premiação), Horário, Quantidade de partidas, ITM, Lucro.  

**RS006:** Histórico de Transferências  
- Métricas: Data, Valor, Referência.  

---

# Página 6

# 4. Histórias de Usuário (Exemplos)

**HU001:** Como jogador, eu quero importar meus históricos de transações da Bodog para que eu possa consolidar todos os meus dados em um só lugar.  
- **Critérios de Aceitação:**  
  - O sistema deve aceitar arquivos CSV exportados da Bodog.  
  - O sistema deve processar o arquivo e exibir uma confirmação de importação bem-sucedida.  
  - Os dados importados devem ser refletidos nos resumos financeiros.  

**HU002:** Como jogador, eu quero visualizar um resumo financeiro geral para que eu possa entender meu desempenho financeiro total em um período.  
- **Critérios de Aceitação:**  
  - O sistema deve exibir o saldo inicial e final do período selecionado.  
  - O sistema deve calcular e exibir o ROI geral para o período.  
  - O sistema deve permitir a seleção de diferentes períodos para o resumo.  

---

# Página 7

**HU003:** Como jogador, eu quero filtrar meus resultados por tipo de torneio (Sit & Go, Programado) para que eu possa identificar onde sou mais lucrativo.  
- **Critérios de Aceitação:**  
  - O sistema deve apresentar opções de filtro para tipos de torneio.  
  - Ao aplicar o filtro, os resumos financeiros e de performance devem ser atualizados para refletir apenas os torneios selecionados.  

**HU004:** Como jogador, eu quero ver o desempenho individual de cada torneio que joguei para que eu possa analisar detalhes específicos e aprender com meus resultados.  
- **Critérios de Aceitação:**  
  - O sistema deve listar os torneios com seus respectivos nomes, valores, horários, quantidade de partidas, ITM e lucro.  
  - Deve ser possível ordenar a lista por diferentes critérios (ex: lucro, data).  

---

# Página 8 e 9

# 5. Rastreabilidade dos Requisitos

# Rastreabilidade dos Requisitos

| ID Requisito | Origem (Documento/Seção)                          | Objetivo(s) Atendido(s) | História(s) de Usuário Relacionada(s) |
|--------------|---------------------------------------------------|-------------------------|---------------------------------------|
| RF001        | VisãoDoProdutoeProjetoPokerStats.md (1.3.1, 2.2)  | OE1                     | HU001                                 |
| RF002        | VisãoDoProdutoeProjetoPokerStats.md (2.1)         | OE1, OE3                | HU002                                 |
| RF003        | Prompt do Usuário                                 | OE2                     | HU003                                 |
| RF004        | Prompt do Usuário                                 | OE2                     | HU003                                 |
| RF005        | Prompt do Usuário                                 | OE2                     | HU003                                 |
| RF006        | Prompt do Usuário                                 | OE2                     | HU004                                 |
| RF007        | Prompt do Usuário                                 | OE1                     | -                                     |
| RF008        | VisãoDoProdutoeProjetoPokerStats.md (2.1, 2.2)    | OE3                     | HU002                                 |
| RF009        | VisãoDoProdutoeProjetoPokerStats.md (2.2)         | OE2                     | HU003                                 |
| RF010        | VisãoDoProdutoeProjetoPokerStats.md (2.1, 2.2)    | OE4                     | -                                     |
| RNF001       | VisãoDoProdutoeProjetoPokerStats.md (1.3.3, 2.3)  | -                       | -                                     |
| RNF002       | VisãoDoProdutoeProjetoPokerStats.md (1.4, 2.3)    | -                       | -                                     |
| RNF003       | VisãoDoProdutoeProjetoPokerStats.md (1.3.2, 2.1)  | OE3                     | -                                     |
| RNF004       | VisãoDoProdutoeProjetoPokerStats.md (1.3.2)       | -                       | -                                     |



---
