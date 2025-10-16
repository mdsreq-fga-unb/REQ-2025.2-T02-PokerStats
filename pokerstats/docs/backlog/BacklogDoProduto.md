# 9. BACKLOG DE PRODUTO

## Histórico de Versão:

| **Data**   | **Versão** | **Descrição**                                               | **Autor**            |
| ---------- | ---------- | ----------------------------------------------------------- | -------------------- |
| 07/10/2025 | 1.0        | Criação do documento e atualização com conteúdo da etapa um | Felipe Júnior Duarte |

O backlog é uma lista organizada e priorizada de todas as tarefas, funcionalidades, melhorias e correções que precisam ser desenvolvidas em um projeto. Ele funciona como um repositório central de demandas, onde cada item representa um trabalho a ser realizado para agregar valor ao produto. No contexto ágil, o backlog é constantemente revisado e ajustado conforme surgem novas necessidades ou mudanças de prioridade, garantindo que a equipe foque sempre nas atividades mais importantes e alinhadas aos objetivos do projeto."


## 9.1 Requisitos Funcionais e não Funcionais

### 9.1.1 Requisitos Funcionais

| **Código** | **Descrição**                            |
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

### 9.1.2 Requisitos Não Funcionais

| **Código** | **Descrição**                                                                                                                                                     |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RNF01      | O sistema deve processar um lote de 100 arquivos de histórico e gerar as análises correspondentes em menos de 10 segundos.                                        |
| RNF02      | As operações de importação de arquivos e visualização das métricas devem ser concluídas em, no máximo, 3 ações do usuário (cliques) a partir da tela principal.   |
| RNF03      | O sistema deve garantir a consistência e a integridade dos dados durante os processos de importação, padronização e cálculo, sem corromper ou perder informações. |
| RNF04      | A aplicação deve ser compatível e executável no sistema operacional Windows.                                                                                      |
| RNF05      | O sistema deve ser desenvolvido em linguagem Python e distribuído como um arquivo executável (.exe), sem a necessidade de um instalador.                          |
| RNF06      | O sistema deve utilizar um banco de dados local para armazenar o histórico de importações e os dados processados, sem depender de um servidor externo.            |




## 9.2 Historias de Usuarios/Backlog Geral

### ÉPICO 1 — Importação e Consolidação de Dados
- **US01** - Eu como usuário quero importar histórico de partidas extraídos da plataforma Bodog para que seja possível consolidar dados de diversar partidas em um único lugar.

### ÉPICO 2 — Análise e Métricas de Desempenho
- **US02** - Eu como usuário quero que o sistema calcule automaticamente o lucro obtido a partir dos dados de partidas para que eu possa ter transparência de investimento.
- **US03** - Eu como usuário quero que o sistema calcule automaticamente o ROI geral e também para tipos diferentes de jogos para que eu possa analisar em quais modalidades eu estou me saindo melhor.
- **US04** - Eu como usuário quero que o sistema calcule automaticamente a taxa de vitórias para cada modalidade e também a taxa de vitórias geral para que eu consiga visualizar melhor o meu desempenho em diferentes segmentos.

### ÉPICO 3 — Visualização e Relatórios
- **US05** - Eu, como usuário, quero filtrar as métricas de desempenho por cada jogador individualmente, para que eu possa avaliar a performance de cada jogador e tomar decisões mais informadas sobre a gestão da equipe.
- **US06** - Eu, como usuário, quero filtrar as análises de desempenho por tipo de torneio, para que eu possa identificar em quais modalidades sou mais lucrativo e tomar decisões mais informadas sobre onde focar meu jogo.
- **US07** - Eu como usuário quero que a minha evolução ao longo do tempo seja exibida em um gráfico de linha para que eu possa ter noção de progresso.
- **US08** - Eu como usuário quero ver o histórico de importações realizados para que eu possa rastrear dados que já foram ou não importados.

### ÉPICO 4 — Desempenho e Distribuição
- **US09** - Eu como usuário quero ver o meu histórico de transações para que eu tenha um controle sobre o valor que está sendo investido.
- **US10** - Eu como usuário quero ver o número de vezes que terminei em uma posição premiada para que eu possa ter uma visão ampla do meu desempenho.

---

## 9.3 Priorização do Backlog

A definição do escopo e da ordem de desenvolvimento do Poker Stats partiu de uma priorização baseada em duas análises complementares: Valor de Negócio e Complexidade Técnica.

1. Análise de Valor de Negócio: Primeiramente, a importância de cada requisito foi classificada em conjunto com o cliente (Eduardo), utilizando a técnica MoSCoW. Esta etapa focou exclusivamente no valor para o negócio, tendo como critério principal o objetivo de gerar inteligência estratégica para o jogador.
2. Análise de Complexidade Técnica: Em paralelo, a complexidade de cada requisito foi estimada pela equipe de desenvolvimento, utilizando uma escala de Story Points que representa o esforço, a incerteza e o risco envolvidos na implementação.

### Legenda de Prioridade (Valor de Negócio):

- Must have: Requisitos essenciais sem os quais o produto não funciona ou não entrega seu valor principal.
- Should have: Requisitos importantes que agregam valor significativo, mas não são vitais para a primeira entrega.
- Could have: Requisitos desejáveis, que podem ser incluídos se o tempo e os recursos permitirem.

### Legenda de Complexidade (Story Points):

#### MB (Muito Baixo) – Story Point 1

- Complexidade: Baixíssima
- Razão: A equipe já desenvolveu funcionalidades idênticas ou extremamente semelhantes, utilizando as mesmas tecnologias e dentro do mesmo contexto do projeto atual.
- Esforço Esperado: Mínimo. Requer pouca ou nenhuma pesquisa, e a implementação é direta.

#### B (Baixo) – Story Point 2

- Complexidade: Baixa
- Razão: A equipe já desenvolveu funcionalidades semelhantes, mas utilizando tecnologias ou bibliotecas diferentes das atuais. Alternativamente, a funcionalidade é simples e bem compreendida, mesmo que nova.
- Esforço Esperado: Baixo. Pode exigir pequenos ajustes ou aprendizado superficial, mas sem grandes desafios.

#### M (Médio) – Story Point 3

- Complexidade: Moderada
- Razão: A funcionalidade é nova para a equipe, mas se assemelha a experiências anteriores. Envolve a combinação de componentes conhecidos ou exige integração com sistemas já familiares.
- Esforço Esperado: Moderado. Requer planejamento, tempo de desenvolvimento e testes mais elaborados. Obstáculos são possíveis, mas possuem soluções conhecidas.

#### A (Alto) – Story Point 5

- Complexidade: Alta
- Razão: A funcionalidade é nova e a equipe não possui experiência direta. Pode envolver uso de tecnologias desconhecidas, integração com sistemas externos complexos ou implementação de lógica de negócio intrincada.
- Esforço Esperado: Alto. Requer pesquisa, prototipagem (spikes) e existe risco significativo de imprevistos durante o desenvolvimento.

#### MA (Muito Alto) – Story Point 7

- Complexidade: Muito alta / Extremamente complexa
- Razão: A funcionalidade é uma incógnita completa (“unknown unknown”). Envolve tecnologias de ponta, problemas sem solução óbvia, alta dependência de fatores externos ou requisitos extremamente voláteis.
- Esforço Esperado: Muito alto e difícil de estimar com precisão. Recomenda-se dividir a funcionalidade em partes menores ou realizar uma fase de pesquisa e descoberta (Spike) antes da implementação.



| **ID** | **Descrição**                           | **Nível de Esforço** | **Prioridade** | **MVP** |
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


