# Solução Proposta

## Objetivo do Produto

O principal objetivo do “Poker Stats” é transformar a experiência de jogadores de poker online, eliminando a tomada de decisão baseada exclusivamente em intuição por meio da consolidação e análise de dados de desempenho (lucro, ROI, % de vitórias, entre outros). O produto tem como propósito fornecer uma solução acessível, intuitiva e confiável que permita ao jogador identificar padrões, avaliar estratégias, gerenciar sua banca e acompanhar sua evolução de forma contínua.

<font size="3"><p style="text-align: left">**Tabela 1** - Objetivos Específicos.</p></font>

| Código | Objetivo Específico                                                                                                   | Indicador de Sucesso                                                                                                                                                             |
| ------ | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OE1    | Eliminar a “cegueira estatística” dos jogadores, consolidando históricos de diferentes torneios em um único ambiente. | Usuário deve consolidar seus históricos de pelo menos 50 torneios e acessar suas métricas principais (ROI, lucros, taxa de vitórias) em menos de 2 minutos dentro da ferramenta. |
| OE2    | Permitir que jogadores identifiquem padrões de desempenho por modalidade, tipo de torneio e estilo de jogo.           | Jogador deve identificar e registrar pelo menos um padrão de desempenho relevante (por modalidade, torneio ou estilo) após usar a ferramenta por 4 semanas.                      |
| OE3    | Oferecer métricas essenciais (lucro, ROI, % vitórias) em relatórios rápidos e confiáveis.                             | Menos de 60 segundos em 90% dos casos para disponibilizar ao jogador um relatório completo e correto com lucro, ROI e % de vitórias após a sessão ou importação dos dados.       |
| OE4    | Facilitar o acompanhamento da evolução do jogador ao longo do tempo com comparativos históricos.                      | O jogador consulta relatórios comparativos de evolução de métricas (lucro, ROI, % vitórias) em diferentes períodos pelo menos 1 vez por semana.                                  |


## Características da Solução
A solução proposta para o “Poker Stats” será materializada em uma plataforma digital, cujas principais características estão diretamente associadas aos objetivos específicos do produto:

- **Consolidação de históricos de plataformas (OE1):** O sistema permitirá a importação de arquivos de diversos torneios de poker do site Bodog, padronizando formatos e unificando as informações em um único ambiente. Isso garantirá a integridade dos dados e evitará erros ou duplicações.  
- **Identificação de padrões de desempenho (OE2):** Serão disponibilizados filtros de análise por modalidade, tipo de torneio, permitindo que o jogador reconheça pontos fortes e fracos em seu estilo de jogo.  
- **Métricas essenciais e relatórios confiáveis (OE3):** A plataforma irá calcular automaticamente indicadores como lucro, ROI e porcentagem de vitórias, apresentando relatórios de forma rápida e precisa.  
- **Acompanhamento da evolução do jogador (OE4):** O sistema fornecerá comparativos históricos, permitindo ao usuário visualizar sua evolução ao longo do tempo e ajustar suas estratégias com base em dados concretos.  

## Tecnologias a Serem Utilizadas

O “Poker Stats” será desenvolvido utilizando a linguagem **Python** como base, aproveitando sua robustez e ampla disponibilidade de recursos para análise de dados, construção de interfaces e integração com diferentes formatos de arquivos.

Para viabilizar as funcionalidades propostas, serão empregadas tecnologias que atendam às seguintes necessidades:

* **Manipulação e análise de dados**: bibliotecas que permitam importar, tratar e consolidar arquivos exportados da plataforma Bodog, garantindo padronização e consistência das informações.
* **Visualização de informações**: ferramentas capazes de gerar relatórios gráficos e indicadores de desempenho de forma clara e intuitiva.
* **Interface com o usuário**: soluções para criação de uma interface gráfica multiplataforma que possibilite interação simples e acessível, mesmo para usuários sem conhecimento técnico.
* **Empacotamento e distribuição**: mecanismos que permitam transformar a aplicação em um executável (.exe), assegurando facilidade de instalação e uso.
* **Armazenamento local**: tecnologias leves de banco de dados que possibilitem manter o histórico de importações e relatórios, quando necessário.

Essa abordagem garante flexibilidade na escolha das ferramentas durante o desenvolvimento, permitindo ajustes conforme novas necessidades ou oportunidades tecnológicas surgirem.

## Pesquisa de Mercado e Análise Competitiva

O mercado de poker online, avaliado em **US$ 57,01 bilhões em 2024** e com projeção de crescimento para **US$ 141,1 bilhões até 2033**, demonstra um cenário robusto e em expansão.  
No Brasil, o poker é reconhecido como *"esporte da mente"* desde 2010, indicando um ambiente favorável ao desenvolvimento de ferramentas de apoio aos jogadores.

A principal oportunidade identificada reside na lacuna de ferramentas de análise de desempenho personalizadas para jogadores casuais, como Eduardo, que buscam métricas claras e consolidadas sem a complexidade de soluções profissionais.

O mercado oferece diversas ferramentas de rastreamento e análise de poker, que podem ser classificadas em:

### Concorrentes Diretos
- **Softwares Profissionais** (e.g., PokerTracker 4, Hold'em Manager 3, Hand2Note):  
  Oferecem funcionalidades avançadas (HUDs, relatórios detalhados), mas são complexos, caros (a partir de US$ 60) e podem sobrecarregar jogadores casuais com informações excessivas.  
  O PokerTracker 4 funciona em Mac ou Windows, enquanto o Hold'em Manager 3 é apenas para Windows.
- **Ferramentas Específicas** (e.g., ICMizer, GTOWizard, Equilab, Holdem Notes):  
  Focam em aspectos pontuais do jogo (cálculos de EV, estudo de ranges, anotações ao vivo), mas não oferecem uma visão consolidada de desempenho geral.

### Concorrentes Indiretos
- **Planilhas Manuais**: Solução comum, mas trabalhosa, propensa a erros e limitada na geração de métricas complexas.
- **Ausência de Análise**: Muitos jogadores casuais não utilizam ferramentas, baseando-se apenas na intuição.

### Diferenciais Competitivos do *Poker Stats*
O *Poker Stats* se posiciona de forma única ao oferecer:
- **Personalização e Minimalismo**: Foco exclusivo nas métricas essenciais para o perfil de Eduardo, evitando sobrecarga de informações.
- **Acessibilidade e Usabilidade**: Interface simples e intuitiva, desenvolvida para jogadores casuais com familiaridade tecnológica básica, sem a complexidade de softwares profissionais.
- **Foco na Plataforma Bodog**: Otimizado para a coleta e análise de dados da plataforma Bodog, atendendo a uma necessidade específica do público-alvo.


## Análise de Viabilidade
A viabilidade técnica do projeto é alta, uma vez que a equipe de desenvolvimento possui experiência comprovada nas tecnologias que serão utilizadas, principalmente Python e SQLite. O aplicativo será entregue em formato executável (.exe), garantindo facilidade de instalação e uso no ambiente do cliente.

O prazo estimado para o desenvolvimento é de pouco mais de 2 meses, considerado viável diante da complexidade do projeto e da experiência da equipe. O cronograma prevê a entrega do produto completo dentro do período estipulado, com etapas de validação interna para garantir qualidade e estabilidade.

Embora a entrega do software ocorra ao término do desenvolvimento, o cliente acompanhará o andamento do projeto em cada etapa, recebendo apresentações periódicas sobre o progresso. Isso permitirá maior transparência e a oportunidade de sugerir ajustes enquanto o desenvolvimento estiver em curso.

## Impacto da Solução
Espera-se que o “Poker Stats” traga benefícios diretos e indiretos para o grupo de jogadores administrado por Eduardo, impactando tanto a eficiência da gestão quanto a qualidade das decisões tomadas:

- **Clareza e Consolidação de Informações:** O sistema permitirá que os jogadores reúnam todos os históricos de torneios em um único ambiente, eliminando a necessidade de consolidação manual e garantindo uma visão centralizada e confiável do desempenho coletivo e individual.  
- **Agilidade na Análise de Desempenho:** Com relatórios automáticos de métricas como ROI, lucro e taxa de vitórias, o tempo gasto em cálculos manuais será drasticamente reduzido, possibilitando que o cliente obtenha insights em poucos minutos após cada importação de dados.  
- **Identificação de Padrões Estratégicos:** Os filtros de análise e relatórios personalizados permitirão que o grupo reconheça tendências, como modalidades mais rentáveis, horários mais vantajosos ou estilos de jogo mais lucrativos, possibilitando ajustes estratégicos embasados em dados concretos.  
- **Apoio à Tomada de Decisões Financeiras:** Com métricas claras de desempenho e histórico de evolução, os jogadores terão subsídios sólidos para gerir sua banca (bankroll), definindo limites adequados e escolhendo modalidades de jogo de acordo com a rentabilidade observada.  
- **Aprimoramento Contínuo do Jogo:** O acompanhamento histórico da evolução das métricas dará aos jogadores feedback objetivo sobre seus avanços, permitindo que cada integrante do grupo visualize sua progressão ao longo do tempo e corrija pontos fracos de forma direcionada.  
- **Eficiência Operacional e Redução de Erros:** A automação do processamento de arquivos e a padronização dos dados minimizam inconsistências, duplicações ou falhas manuais, aumentando a confiabilidade das estatísticas apresentadas.  
- **Diferenciação e Adequação ao Contexto do Cliente:** Ao contrário das ferramentas genéricas disponíveis no mercado, o “Poker Stats” é personalizado para as métricas de maior interesse do grupo, oferecendo simplicidade, foco e relevância, sem sobrecarga de informações desnecessárias.  


## Histórico de Versões

<font size="3"><p style="text-align: left">**Tabela 2** - Histórico de versões.</p></font>

| Versão |        Descrição         |                      Autor(es)                      |    Data    |
| :----: | :----------------------: | :-------------------------------------------------: | :--------:  
|  1.0   | Criação do documento | [Carlos Henrique](https://github.com/Depaiiva), [Felipe Rodrigues](https://github.com/felipeJRdev)                | 15/09/2025 | 
|  2.0   | Ajustes do documento | [Renan Pereira](https://github.com/renanpr7)               | 15/09/2025 | 