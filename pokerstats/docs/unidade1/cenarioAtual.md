# Cenário Atual do Cliente e do Negócio

## Introdução ao Negócio e Contexto
O mercado de poker online reúne operadores e grupos de jogadores que realizam partidas regulares em plataformas centralizadas. Nesse contexto, Eduardo administra um grupo de jogadores que atua exclusivamente na plataforma Bodog, concentrando toda a geração de relatórios e registros dessa operação em uma única fonte.

O grupo realiza várias sessões de jogo ao longo do mês, produzindo documentos e arquivos de sessão que registram o histórico das partidas. Atualmente, esses artefatos chegam de forma fragmentada – geralmente como relatórios e planilhas por jogador ou por sessão e o cliente precisa consolidar manualmente essas informações para obter uma visão do desempenho coletivo e individual.

Ao final do mês, com o grande volume de jogos, Eduardo enfrenta o desafio de analisar o que foi mais lucrativo e rentável para o grupo. Ele recebe planilhas da plataforma, mas a organização e a análise se tornam difíceis devido ao grande volume de torneios, às limitações dos dados presentes nessas planilhas e à complexidade de calcular métricas importantes como win rate e lucro de forma manual. Essa dificuldade o impede de focar nas escolhas certas para a gestão do grupo.

## Identificação da Oportunidade ou Problema
A principal oportunidade identificada no cenário do cliente reside na falta de ferramentas de análise de desempenho que se adequem às preferências e ao contexto específico do grupo de Eduardo. Embora existam ferramentas de rastreamento e análise de desempenho no mercado (geralmente soluções terceirizadas como o PokerTracker), elas não atendem à necessidade do usuário por uma plataforma personalizada, minimalista e focada em suas métricas de interesse. O cliente e seu grupo, que participam dos jogos, são forçados a operar com pouca compreensão clara de seu histórico financeiro e de performance, pois as soluções existentes não lhes proporcionam a visão desejada ou sobrecarregam com informações irrelevantes.

O problema central que o projeto "Poker Stats" visa resolver é a "cegueira" do cliente em relação aos resultados do seu grupo. Sem acesso fácil e consolidado a métricas vitais que se alinham às suas preferências, como lucro total, lucro por torneio, Retorno Sobre Investimento (ROI), histórico de transações de conta e porcentagem de vitórias, os jogadores não conseguem:

- **Identificar padrões de desempenho:** Dificuldade em reconhecer onde e quando são mais bem-sucedidos, como em quais tipos de torneios/mesas ou com quais estilos de jogo se destacam.  
- **Avaliar e ajustar estratégias:** Impossibilidade de analisar a eficácia das suas abordagens de jogo e determinar os ajustes necessários.  
- **Tomar decisões informadas:** Ausência de dados concretos para decidir sobre a gestão da banca (bankroll), o tipo de jogo a focar ou quando aumentar/diminuir os limites, baseado em informações claras e relevantes.  
- **Aprimoramento contínuo:** A falta de feedback numérico e estatístico que se alinha às suas preferências impede que o jogador visualize sua evolução e corrija falhas.  

O "Poker Stats" surge para iluminar esse cenário, oferecendo uma plataforma personalizada, minimalista e focada nas métricas de interesse do usuário. A oportunidade é informar o cliente com o conhecimento necessário para gerenciar sua banca de forma inteligente, aprimorar sua visão geral sobre a performance do grupo e, em última instância, transformar uma atividade baseada em intuição em uma prática baseada em dados relevantes e acessíveis.

![alt text](../imagens/DiagramaIshikawa.jpg)

## Desafios do Projeto
O desenvolvimento do "Poker Stats" apresenta desafios técnicos e operacionais significativos que exigem planejamento cuidadoso e soluções robustas para garantir a entrega de uma ferramenta eficaz e confiável. Os principais obstáculos a serem superados incluem:

### Desafios na Aquisição e Consistência de Dados
- **Incompletude e Limitação dos Dados da Plataforma (Bodog):** Embora focado inicialmente na plataforma Bodog, o principal desafio reside na natureza dos dados disponibilizados por ela. Os históricos de mãos ou relatórios de transações podem carecer de detalhes específicos ou serem incompletos em relação a todas as métricas desejadas para uma análise aprofundada. Isso exige métodos inteligentes para inferir ou complementar informações ausentes.  
- **Confiabilidade da Coleta:** A dependência de métodos de importação de dados por parte do usuário (como o upload de históricos de mãos exportados) exige que o sistema seja resiliente a possíveis incompletudes ou erros nos arquivos de origem, especialmente devido às limitações do Bodog.  
- **Volume e Qualidade dos Dados:** O Poker Stats precisará lidar com um volume potencialmente grande de dados de jogo e transações financeiras. Garantir a integridade, precisão e ausência de duplicações nesses dados é fundamental para a credibilidade das estatísticas geradas, especialmente ao lidar com a qualidade dos dados fornecidos pela fonte.  

### Desafios Técnicos no Processamento e Análise de Dados
- **Cálculo de Métricas Complexas:** Desenvolver algoritmos precisos para o cálculo de métricas avançadas de poker (como ROI ajustado, variância) exige um entendimento aprofundado das nuances do poker e da estatística.  
- **Otimização de Performance:** Processar grandes volumes de dados de forma rápida e eficiente para gerar relatórios e visualizações em tempo hábil é crucial para a experiência do usuário. Otimização de banco de dados e de algoritmos serão necessárias.  
- **Escalabilidade da Arquitetura:** A arquitetura do sistema deve ser projetada para escalar horizontalmente, suportando um número crescente de usuários e o volume de dados gerado por eles ao longo do tempo.  

### Desafios de Interface e Experiência do Usuário (UI/UX)
- **Visualização de Dados Complexos:** O principal desafio é transformar dados numéricos e estatísticos complexos em gráficos, tabelas e painéis intuitivos e de fácil compreensão para jogadores de diferentes níveis de familiaridade com análise de dados.  
- **Personalização e Flexibilidade:** Permitir que o usuário personalize quais métricas visualizar, aplique filtros (por tipo de jogo, buy-in, período) e configure seus próprios relatórios de forma simples.  
- **Acessibilidade e Usabilidade:** Garantir que a ferramenta seja acessível e fácil de usar para todos os usuários, desde os menos experientes em tecnologia até os mais avançados.  

### Desafios de Manutenção e Sustentabilidade
- **Adaptação a Mudanças na Plataforma:** A plataforma Bodog pode alterar seus formatos de logs, interfaces ou regras de jogo. O "Poker Stats" precisará ser flexível para se adaptar rapidamente a essas mudanças e garantir a continuidade da coleta e processamento de dados.  
- **Concorrência e Diferenciação:** Embora o problema de falta de métricas seja claro, o mercado pode ter outras soluções (mesmo que parciais ou mais complexas). O desafio é manter o "Poker Stats" relevante e diferenciado.  
- **Suporte aos Usuários:** Fornecer suporte adequado aos usuários para garantir a utilização eficaz da ferramenta e resolver eventuais problemas.  

## Segmentação do Cliente
O público-alvo do "Poker Stats" é composto pelo grupo de jogadores e o cliente que buscam aprimorar sua compreensão sobre seus próprios resultados por meio de métricas e estatísticas detalhadas. A ferramenta foi concebida para ser acessível a um amplo espectro de jogadores, podendo ser segmentada da seguinte forma:

### Por Nível de Habilidade
- **Todos os Níveis:** O "Poker Stats" será relevante e utilizável por jogadores iniciantes, intermediários e avançados. A interface e as funcionalidades serão projetadas para oferecer insights valiosos, independentemente do grau de experiência do jogador.  

### Por Frequência e Objetivo de Jogo
- **Jogadores Casuais e Regulares:** O foco principal da ferramenta é atender jogadores que participam de jogos com amigos ou que jogam regularmente, mas sem um objetivo estritamente profissional ou altamente competitivo no início. Esses jogadores buscam entender melhor seu desempenho para tomar decisões mais informadas e aumentar seus lucros no longo prazo.  
- **Jogadores Competitivos (Uso Secundário):** Embora não seja o foco primário, jogadores com objetivos competitivos também poderão utilizar o "Poker Stats" como uma ferramenta complementar para analisar seus resultados, identificar padrões e refinar suas estratégias.  

### Por Tipo de Jogo e Plataforma
- **Sit-and-Go e Multi-Table:** A ferramenta será inicialmente otimizada para analisar resultados de jogos no formato sit-and-go e multi-table.  
- **Plataforma Bodog:** O foco inicial na coleta e processamento de dados será direcionado para jogadores que utilizam a plataforma Bodog.  

### Por Necessidade de Análise
- **Jogadores em Busca de Métricas:** O segmento central são jogadores que reconhecem a lacuna existente nos sites de poker e desejam ter acesso consolidado a estatísticas de desempenho (lucro, ROI, transações, porcentagem de vitória, etc.) para sair do "jogo no escuro" e basear suas decisões em dados concretos.  
