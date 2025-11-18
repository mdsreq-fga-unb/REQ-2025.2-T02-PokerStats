# Backlog

## Backlog Geral

- O backlog geral contém todas as funcionalidades e melhorias planejadas para o software. Cada item é 
detalhado e priorizado para garantir uma visão clara do que será desenvolvido ao longo do projeto. 


### Histórias do Usuário

- US01 - Eu como usuário quero importar histórico de partidas extraídos da plataforma Bodog para que seja possível consolidar dados de diversas partidas em um único lugar. 

- US02 - Eu como usuário quero que o sistema calcule automaticamente o lucro obtido a partir dos dados de partidas para que eu possa ter transparência de investimento. 

- US03 - Eu como usuário quero que o sistema calcule automaticamente o ROI geral e também para tipos diferentes de jogos para que eu possa analisar em quais modalidades eu estou me saindo melhor. 

- US04 - Eu como usuário quero que o sistema calcule automaticamente a taxa de vitórias para cada modalidade e também a taxa de vitórias geral para que eu consiga visualizar melhor o meu desempenho em diferentes segmentos. 

- US05 - Eu, como usuário, quero filtrar as métricas de desempenho por cada jogador individualmente, para que eu possa avaliar a performance de cada jogador e tomar decisões mais informadas sobre a gestão da equipe. 

- US06 - Eu, como usuário, quero filtrar as análises de desempenho por tipo de torneio, para que eu possa identificar em quais modalidades sou mais lucrativo e tomar decisões mais informadas sobre onde focar meu jogo. 

- US07 - Eu como usuário quero que a minha evolução ao longo do tempo seja exibida em um gráfico de linha para que eu possa ter noção de progresso. 

- US08 - Eu como usuário quero ver o histórico de importações realizados para que eu possa rastrear dados que já foram ou não importados. 

- US09 - Eu como usuário quero ver o meu histórico de transações para que eu tenha um controle sobre o valor que está sendo investido. 

- US10 - Eu como usuários quero ver o número de vezes que terminei em uma posição premiada para que eu possa ter uma visão ampla do meu desempenho. 

## Priorização do Backlog Geral

- A definição do escopo e da ordem de desenvolvimento do Poker Stats partiu de uma priorização baseada em duas análises complementares: **Valor de Negócio** e **Complexidade Técnica.**

1. Análise de Valor de Negócio: Primeiramente, a importância de cada requisito foi classificada em conjunto com o cliente (Eduardo), utilizando a técnica MoSCoW. Esta etapa focou exclusivamente no valor para o negócio, tendo como critério principal o objetivo de gerar inteligência estratégica para o jogador.
2. Análise de Complexidade Técnica: Em paralelo, a complexidade de cada requisito foi estimada pela equipe de desenvolvimento, utilizando uma escala de Story Points que representa o esforço, a incerteza e o risco envolvidos na implementação.


### Legenda de Prioridade (Valor de Negócio):
- Must have: Requisitos essenciais sem os quais o produto não funciona ou não entrega seu valor principal.
- Should have: Requisitos importantes que agregam valor significativo, mas não são vitais para a primeira entrega.
- Could have: Requisitos desejáveis, que podem ser incluídos se o tempo e os recursos permitirem.

### Legenda de Complexidade (Story Points):

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

 