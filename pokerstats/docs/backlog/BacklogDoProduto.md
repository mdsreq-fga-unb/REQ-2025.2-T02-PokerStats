# BACKLOG DE PRODUTO

Esta seção detalha o backlog geral do produto e a priorização dos requisitos para consolidação do MVP.

## Requisitos Funcionais e não Funcionais

Abaixo os requisitos funcionais e não funcionais reapresentados para melhor visão da rastreabilidade:

### Requisitos Funcionais

<font size="3"><p style="text-align: left">**Tabela 1** - Requisitos Funcionais.</p></font>

| **Código** | **Descrição** |
| ---------- | ---------------------------------------- |
| RF01       | Importar e Consolidar Histórico          |
| RF02       | Calcular Lucro Total                     |
| RF03       | Calcular ROI                             |
| RF04       | Calcular Taxa de Vitórias                |
| RF05       | Segmentar Análises por jogador           |
| RF06       | Segmentar Análises por tipo de torneio   |
| RF07       | Visualizar Gráfico de Linhas de Evolução |
| RF08       | Listar Histórico de Importações          |
| RF09       | Exibir Histórico de Transações           |
| RF10       | Calcular ITM (In The Money)              |

### Requisitos Não Funcionais

<font size="3"><p style="text-align: left">**Tabela 2** - Requisitos não Funcionais.</p></font>


| **Código** | **Descrição** |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RNF01      | O sistema deve processar um lote de 100 arquivos de histórico e gerar as análises correspondentes em menos de 10 segundos.                                        |
| RNF02      | As operações de importação de arquivos e visualização das métricas devem ser concluídas em, no máximo, 3 ações do usuário (cliques) a partir da tela principal.   |
| RNF03      | O sistema deve garantir a consistência e a integridade dos dados durante os processos de importação, padronização e cálculo, sem corromper ou perder informações. |
| RNF04      | A aplicação deve ser compatível e executável no sistema operacional Windows.                                                                                      |
| RNF05      | O sistema deve ser desenvolvido em linguagem Python e distribuído como um arquivo executável (.exe), sem a necessidade de um instalador.                          |
| RNF06      | O sistema deve utilizar um banco de dados local para armazenar o histórico de importações e os dados processados, sem depender de um servidor externo.            |

## Historias de Usuarios/Backlog Geral

**US01** - Eu como usuário quero importar histórico de partidas extraídos da plataforma Bodog para que seja possível consolidar dados de diversar partidas em um único lugar.

**Critérios de Aceitação:**

-   Importar tabela csv
-   Importar tabela txt
-   Ler e apresentar dados importados corretamente

**US02** - Eu como usuário quero que o sistema calcule automaticamente o lucro obtido a partir dos dados de partidas para que eu possa ter transparência de investimento.

**Critérios de Aceitação:**

-   Ler e apresentar corretamente os dados importados
-   Calcular e apresentar o lucro obtido corretamente
-   Visualizar lucro por partida
-   Visualizar lucro por torneio
-   Visualizar lucro por modo de jogo
-   Filtrar por maior lucro
-   Filtrar por menor lucro

**US03** - Eu como usuário quero que o sistema calcule automaticamente o ROI geral e também para tipos diferentes de jogos para que eu possa analisar em quais modalidades eu estou me saindo melhor.

**Critérios de Aceitação:**

-   Ler e apresentar corretamente os dados
-   Calcular e apresentar corretamente o ROI
-   Calcular ROI geral
-   Calcular ROI para cada modalidade
-   Calcular ROI para cada torneio
-   Filtrar por menor valor
-   Filtrar por maior valor

**US04** - Eu como usuário quero que o sistema calcule automaticamente a taxa de vitórias para cada modalidade e também a taxa de vitórias geral para que eu consiga visualizar melhor o meu desempenho em diferentes segmentos.

**Critérios de Aceitação:**

-   Calcular corretamente a taxa de vitórias
-   Apresentar a taxa de vitórias
-   Filtrar por modalidade
-   Filtrar por maior
-   Filtrar por menor
-   Filtrar por data
-   Filtrar por torneio

**US05** - Eu, como usuário, quero filtrar as métricas de desempenho por cada jogador individualmente, para que eu possa avaliar a performance de cada jogador e tomar decisões mais informadas sobre a gestão da equipe.

**Critérios de Aceitação:**

-   Visualizar métricas para cada jogador individualmente
-   Apresentar gráficos que ilustrem as métricas da melhor maneira
-   Filtrar por jogador
-   Filtrar por modalidade
-   Filtrar por torneio
-   Filtrar por métrica
-   Filtrar por menor
-   Filtrar por maior

**US06** - Eu, como usuário, quero filtrar as análises de desempenho por tipo de torneio, para que eu possa identificar em quais modalidades sou mais lucrativo e tomar decisões mais informadas sobre onde focar meu jogo.

**Critérios de Aceitação:**

-   Apresentar Análises para cada tipo de torneio
-   Filtrar por tipo de torneio
-   Filtrar por torneio específico

**US07** - Eu como usuário quero que a minha evolução ao longo do tempo seja exibida em um gráfico de linha para que eu possa ter noção de progresso.

**Critérios de Aceitação:**

-   Calcular evolução do jogador ao longo do tempo
-   Apresentar a evolução do jogador em um gráfico de linha
-   Filtrar por tempo
-   Filtrar por % de evolução

**US08** - Eu como usuário quero ver o histórico de importações realizados para que eu possa rastrear dados que já foram ou não importados.

**Critérios de Aceitação:**

-   Apresentar histórico de importações
-   Filtrar por data
-   Filtrar por mais recente
-   Filtrar por mais antigo

**US09** - Eu como usuário quero ver o meu histórico de transações para que eu tenha um controle sobre o valor que está sendo investido.

**Critérios de Aceitação:**

-   Apresentar os valores de transações do jogador
-   Filtrar por data
-   Filtrar por maior valor
-   Filtrar por menor valor
-   Filtrar por valor específico
-   Filtrar por mais recente
-   Filtrar por mais antigo

**US10** - Eu como usuário quero ver o número de vezes que terminei em uma posição premiada para que eu possa ter uma visão ampla do meu desempenho.

**Critérios de Aceitação:**

-   Apresentar ITM corretamente
-   Apresentar a partida que está relacionada a cada ITM
-   Filtrar por data
-   Filtrar por premiação
-   Filtrar por menor valor
-   Filtrar por maior valor
    
## Tabela de Rastreabilidade (Histórias de Usuário x Requisitos)

<font size="3"><p style="text-align: left">**Tabela 3** - Rastreabilidade das histórias de usuários.</p></font>


| **ID da História** | **Descrição da História de Usuário** | **Requisito Funcional** |
| :--- | :--- | :--- |
| US01 | Importar Histórico de Partidas | RF01 |
| US02 | Exibir Lucro Total | RF02 |
| US03 | Exibir ROI (Geral e por Tipo) | RF03 |
| US04 | Exibir Taxa de Vitórias (Geral e por Tipo) | RF04 |
| US05 | Filtrar Análise por Jogador | RF05 |
| US06 | Filtrar Análise por Tipo de Torneio | RF06 |
| US07 | Exibir Gráfico de Evolução | RF07 |
| US08 | Listar Histórico de Importações | RF08 |
| US09 | Exibir Histórico de Transações | RF09 |
| US10 | Exibir ITM (In The Money) | RF10 |

## Priorização do Backlog

A definição do escopo e da ordem de desenvolvimento do Poker Stats partiu de uma priorização baseada em duas análises complementares: Valor de Negócio e Complexidade Técnica.

1.  Análise de Valor de Negócio: Primeiramente, a importância de cada requisito foi classificada em conjunto com o cliente (Eduardo), utilizando a técnica MoSCoW. Esta etapa focou exclusivamente no valor para o negócio, tendo como critério principal o objetivo de gerar inteligência estratégica para o jogador.
2.  Análise de Complexidade Técnica: Em paralelo, a complexidade de cada requisito foi estimada pela equipe de desenvolvimento, utilizando uma escala de Story Points que representa o esforço, a incerteza e o risco envolvidos na implementação.

### Legenda de Prioridade (Valor de Negócio):

-   Must have: Requisitos essenciais sem os quais o produto não funciona ou não entrega seu valor principal.
-   Should have: Requisitos importantes que agregam valor significativo, mas não são vitais para a primeira entrega.
-   Could have: Requisitos desejáveis, que podem ser incluídos se o tempo e os recursos permitirem.

### Legenda de Complexidade (Story Points):

#### MB (Muito Baixo) – Story Point 1

-   Complexidade: Baixíssima
-   Razão: A equipe já desenvolveu funcionalidades idênticas ou extremamente semelhantes, utilizando as mesmas tecnologias e dentro do mesmo contexto do projeto atual.
-   Esforço Esperado: Mínimo. Requer pouca ou nenhuma pesquisa, e a implementação é direta.

#### B (Baixo) – Story Point 2

-   Complexidade: Baixa
-   Razão: A equipe já desenvolveu funcionalidades semelhantes, mas utilizando tecnologias ou bibliotecas diferentes das atuais. Alternativamente, a funcionalidade é simples e bem compreendida, mesmo que nova.
-   Esforço Esperado: Baixo. Pode exigir pequenos ajustes ou aprendizado superficial, mas sem grandes desafios.

#### M (Médio) – Story Point 3

-   Complexidade: Moderada
-   Razão: A funcionalidade é nova para a equipe, mas se assemelha a experiências anteriores. Envolve a combinação de componentes conhecidos ou exige integração com sistemas já familiares.
-   Esforço Esperado: Moderado. Requer planejamento, tempo de desenvolvimento e testes mais elaborados. Obstáculos são possíveis, mas possuem soluções conhecidas.

#### A (Alto) – Story Point 5

-   Complexidade: Alta
-   Razão: A funcionalidade é nova e a equipe não possui experiência direta. Pode envolver uso de tecnologias desconhecidas, integração com sistemas externos complexos ou implementação de lógica de negócio intrincada.
-   Esforço Esperado: Alto. Requer pesquisa, prototipagem (spikes) e existe risco significativo de imprevistos durante o desenvolvimento.

#### MA (Muito Alto) – Story Point 7

-   Complexidade: Muito alta / Extremamente complexa
-   Razão: A funcionalidade é uma incógnita completa (“unknown unknown”). Envolve tecnologias de ponta, problemas sem solução óbvia, alta dependência de fatores externos ou requisitos extremamente voláteis.
-   Esforço Esperado: Muito alto e difícil de estimar com precisão. Recomenda-se dividir a funcionalidade em partes menores ou realizar uma fase de pesquisa e descoberta (Spike) antes da implementação.


<font size="3"><p style="text-align: left">**Tabela 4** - Priorização do Backlog.</p></font>


| **ID** | **Descrição** | **Nível de Esforço** | **Prioridade** | **MVP** |
| ------ | --------------------------------------- | -------------------- | -------------- | ------- |
| US01   | Importar histórico de torneios          | A                    | Must have      | X       |
| US02   | Calcular Lucro Total                    | MB                   | Must have      | X       |
| US03   | Calcular ROI                            | B                    | Must have      | X       |
| US04   | Calcular Taxa de Vitória                | MB                   | Should have    |         |
| US05   | Segmentar Análises por jogador          | MA                   | Should have    |         |
| US06   | Segmentar Análises por tipo de torneio  | A                    | Must have      | X       |
| US07   | Visualizar Gráfico de Linha de Evolução | M                    | Could have     |         |
| US08   | Listar Histórico de Importações         | M                    | Could have     |         |
| US09   | Exibir Histórico de Transações          | B                    | Should have    |         |
| US10   | Calcular ITM (In The Money)             | B                    | Must have      | X       |

## Histórico de Versões

<font size="3"><p style="text-align: left">**Tabela 5** - Histórico de versões.</p></font>

| Versão |        Descrição         |                      Autor(es)                      |    Data    |
| :----: | :----------------------: | :-------------------------------------------------: | :--------:  
|  1.0   | Criação do documento |  [Felipe Rodrigues](https://github.com/felipeJRdev)      | 15/10/2025 | 