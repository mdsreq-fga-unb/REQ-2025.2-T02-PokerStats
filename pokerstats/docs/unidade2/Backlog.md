# 8. Backlog

## 8.1 Backlog Geral

- O backlog geral contém todas as funcionalidades e melhorias planejadas para o software. Cada item é 
detalhado e priorizado para garantir uma visão clara do que será desenvolvido ao longo do projeto. 


### 8.1.1 Histórias do Usuário

- US01 - Eu como usuário quero importar histórico de partidas extraídos da plataforma Bodog para que seja possível consolidar dados de diversas partidas em um único lugar. 

**Critérios de Aceitação:**


O sistema deve fornecer uma sessão em que seja possível que o usuário importe um ou mais históricos da plataforma Bodog.

O sistema deve aceitar diferentes extensões de arquivos de histórico, são elas: xlsx, csv e txt.

Após a importação bem-sucedida, o sistema deve exibir uma mensagem de sucesso, indicando o número de arquivos processados e o total de partidas/torneios consolidados.

Os dados importados devem ser refletidos nas métricas do sistema (como Lucro Total, ROI, etc.).

Caso um arquivo esteja em um formato suportado (ex: .csv), mas seu conteúdo seja inválido (ex: colunas erradas, dados corrompidos), o sistema deve exibir uma mensagem de erro clara, informar qual arquivo falhou e não consolidar os dados.

O sistema não deve permitir a importação de dados duplicados (ex: o mesmo arquivo de histórico importado duas vezes), para garantir a integridade dos cálculos.


- US02 - Eu como usuário quero que o sistema calcule automaticamente o lucro obtido a partir dos dados de partidas para que eu possa ter transparência de investimento. 

**Critérios de Aceitação**:

O sistema deve calcular o Lucro Líquido automaticamente aplicando a fórmula: (soma total dos Prêmios) - (soma total dos Buy-ins).

O cálculo deve ser atualizado instantaneamente sempre que uma nova importação de histórico for concluída ou um dado for alterado, garantindo que o usuário veja sempre a informação mais recente.

O sistema deve apresentar o valor formatado como moeda, com duas casas decimais (ex: R$ 1.500,00 ou $ 1,500.00).

Para facilitar a leitura rápida (transparência), o sistema deve exibir valores de lucro (positivos) na cor verde e valores de prejuízo (negativos) na cor vermelha.

Caso o resultado seja negativo, o sistema deve exibir explicitamente o sinal de menos antes do valor (ex: - R$ 50,00).

Se não houver dados de partidas importados no sistema, o campo de lucro deve exibir o valor neutro (0,00) sem apresentar erros de processamento na interface.

- US03 - Eu como usuário quero que o sistema calcule automaticamente o ROI geral e também para tipos diferentes de jogos para que eu possa analisar em quais modalidades eu estou me saindo melhor. 

**Critérios de Aceitação**:

O sistema deve calcular o ROI (Retorno sobre Investimento) aplicando a fórmula: ((Retorno Total - Investimento Total) / Investimento Total) * 100, exibindo o resultado em porcentagem.

O sistema deve exibir o ROI Geral, considerando a consolidação de todas as partidas registradas no banco de dados.

O sistema deve apresentar o ROI segmentado por modalidade ou tipo de jogo (ex: Sit & Go, MTT, Cash Game), agrupando os dados conforme a classificação extraída dos arquivos do Bodog.

O valor do ROI deve ser formatado com duas casas decimais e acompanhado do símbolo "%" (ex: 25,50% ou -10,00%).

Visualmente, o sistema deve destacar ROIs positivos em verde e ROIs negativos em vermelho, permitindo que o usuário identifique rapidamente em quais modalidades está tendo melhor desempenho.

Caso o investimento total de um agrupamento seja zero (ex: apenas torneios Freeroll jogados), o sistema deve tratar a divisão por zero e exibir o ROI como "0%" ou "N/A", sem gerar erro na aplicação.

- US04 - Eu como usuário quero que o sistema calcule automaticamente a taxa de vitórias para cada modalidade e também a taxa de vitórias geral para que eu consiga visualizar melhor o meu desempenho em diferentes segmentos. 

**Critérios de Aceitação**:

Calcular corretamente a taxa de vitórias

Apresentar a taxa de vitórias

Filtrar por modalidade

Filtrar por maior

Filtrar por menor

Filtrar por data

Filtrar por torneio

- US05 - Eu, como usuário, quero filtrar as métricas de desempenho por cada jogador individualmente, para que eu possa avaliar a performance de cada jogador e tomar decisões mais informadas sobre a gestão da equipe. 

**Critérios de Aceitação**:

Visualizar métricas para cada jogador individualmente

Apresentar gráficos que ilustrem as métricas da melhor maneira

Filtrar por jogador

Filtrar por modalidade

Filtrar por torneio

Filtrar por métrica

Filtrar por menor

Filtrar por maior

- US06 - Eu, como usuário, quero filtrar as análises de desempenho por tipo de torneio, para que eu possa identificar em quais modalidades sou mais lucrativo e tomar decisões mais informadas sobre onde focar meu jogo. 

**Critérios de Aceitação**:

Apresentar Análises para cada tipo de torneio

Filtrar por tipo de torneio

Filtrar por torneio específico

- US07 - Eu como usuário quero que a minha evolução ao longo do tempo seja exibida em um gráfico de linha para que eu possa ter noção de progresso. 

**Critérios de Aceitação**:

Calcular evolução do jogador ao longo do tempo

Apresentar a evolução do jogador em um gráfico de linha

Filtrar por tempo

Filtrar por % de evolução

- US08 - Eu como usuário quero ver o histórico de importações realizados para que eu possa rastrear dados que já foram ou não importados. 

**Critérios de Aceitação**:

Apresentar histórico de importações

Filtrar por data

Filtrar por mais recente

Filtrar por mais antigo

- US09 - Eu como usuário quero ver o meu histórico de transações para que eu tenha um controle sobre o valor que está sendo investido. 

**Critérios de Aceitação**:

Apresentar os valores de transações do jogador

Filtrar por data

Filtrar por maior valor

Filtrar por menor valor

Filtrar por valor específico

Filtrar por mais recente

Filtrar por mais antigo

- US10 - Eu como usuários quero ver o número de vezes que terminei em uma posição premiada para que eu possa ter uma visão ampla do meu desempenho. 

**Critérios de Aceitação**:

O sistema deve classificar automaticamente uma partida como "ITM" (In The Money) sempre que o valor do prêmio registrado na importação for maior que zero.

O sistema deve calcular a porcentagem de ITM aplicando a fórmula: (Quantidade de partidas com prêmio > 0 / Total de partidas jogadas) * 100.

A interface deve apresentar o dado de forma composta, exibindo a porcentagem e, preferencialmente, os números absolutos para contexto (ex: "20% (20/100)", indicando 20 premiações em 100 jogos).

O valor percentual deve ser arredondado para duas casas decimais (ex: 15,55%).

O indicador de ITM deve ser recalculado e atualizado na tela automaticamente após qualquer nova importação de arquivo ou remoção de dados.

Caso o total de partidas jogadas seja zero (nenhum dado importado), o sistema deve tratar a divisão por zero e exibir "0%" ou um traço "—", sem gerar erros na aplicação.

## 8.2 Priorização do Backlog Geral

- A definição do escopo e da ordem de desenvolvimento do Poker Stats partiu de uma priorização baseada em duas análises complementares: **Valor de Negócio** e **Complexidade Técnica.**

1. Análise de Valor de Negócio: Primeiramente, a importância de cada requisito foi classificada em conjunto com o cliente (Eduardo), utilizando a técnica MoSCoW. Esta etapa focou exclusivamente no valor para o negócio, tendo como critério principal o objetivo de gerar inteligência estratégica para o jogador.
2. Análise de Complexidade Técnica: Em paralelo, a complexidade de cada requisito foi estimada pela equipe de desenvolvimento, utilizando uma escala de Story Points que representa o esforço, a incerteza e o risco envolvidos na implementação.


### 8.2.1 Legenda de Prioridade (Valor de Negócio):
- Must have: Requisitos essenciais sem os quais o produto não funciona ou não entrega seu valor principal.
- Should have: Requisitos importantes que agregam valor significativo, mas não são vitais para a primeira entrega.
- Could have: Requisitos desejáveis, que podem ser incluídos se o tempo e os recursos permitirem.

### 8.2.2 Legenda de Complexidade (Story Points):

- MB (Muito Baixo - 1 pt): Funcionalidade idêntica ou extremamente semelhante a algo já feito pela equipe.
- B (Baixo - 2 pts): Funcionalidade simples e bem compreendida.
- M (Médio - 3 pts): Funcionalidade nova, mas com semelhanças a trabalhos anteriores, exigindo planejamento moderado.
- A (Alto - 5 pts): Funcionalidade nova e com incertezas técnicas, exigindo mais planejamento e pesquisa.
- MA (Muito Alto - 7+ pts): Funcionalidade com alta incerteza, envolvendo tecnologias desconhecidas ou problemas sem solução óbvia. Recomenda-se quebrar em partes menores.

A partir da análise combinada, o Produto Mínimo Viável (MVP) foi definido como o conjunto de todos os requisitos classificados como "Must have"

| ID   | Descrição                           | Nível de Esforço | Prioridade   | MVP |
|------|--------------------------------------|------------------|--------------|-----|
| US01 | Importar histórico de torneios       | A                | Must have    | X   |
| US02 | Calcular Lucro Total                 | MB               | Must have    | X   |
| US03 | Calcular ROI                         | B                | Must have    | X   |
| US04 | Calcular Taxa de Vitória             | MB               | Should have  |     |
| US05 | Segmentar Análises por jogador       | MA               | Should have  |     |
| US06 | Segmentar Análises por tipo de torneio | A              | Must have    | X   |
| US07 | Visualizar Gráfico de Linha de Evolução | M             | Could Have   |     |
| US08 | Listar Histórico de Importações      | M                | Could Have   |     |
| US09 | Exibir Histórico de Transações       | B                | Should Have  |     |
| US10 | Calcular ITM (In The Money)          | B                | Must have    | X   |

 