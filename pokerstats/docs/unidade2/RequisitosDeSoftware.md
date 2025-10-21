# REQUISITOS DE SOFTWARE

Esta seção descreve os requisitos necessários para o desenvolvimento do software. Ela está dividida em requisitos funcionais e não funcionais, que apresentam as funcionalidades do sistema e as qualidades que ele deve possuir para atender às expectativas dos usuários. 

## Características da Solução

Para facilitar a visão da rastreabilidade, abaixo as características da solução apresentadas novamente:

- **[C01]** O sistema permitirá a importação de múltiplos arquivos de histórico de jogo da plataforma Bodog, com padronização de formatos e unificação das informações em um ambiente centralizado.
- **[C02]** A aplicação permitirá a segmentação das análises de desempenho com base no tipo de torneio e jogador.
- **[C03]** O software irá calcular e exibir automaticamente as métricas essenciais de desempenho, incluindo lucro, ROI, porcentagem de vitórias e ITM (In The Money).
- **[C04]** Serão disponibilizadas análises de desempenho com comparativos históricos para visualização da evolução do jogador ao longo do tempo.
- **[C05]** O sistema será otimizado para o processamento eficiente de grandes volumes de dados, com geração de análises de forma rápida.
- **[C06]** A aplicação permitirá o registro e a visualização do histórico de transações financeiras (depósitos e saques), auxiliando na gestão de banca do jogador.

## Lista de Requisitos Funcionais

<font size="3"><p style="text-align: left">**Tabela 1** - Requisitos Funcionais.</p></font>

Os requisitos funcionais descrevem as funcionalidades funcionais que o sistema deve implementar para atender às necessidades do negócio. Eles incluem integrações, processos e interações do usuário com o sistema.

| Código | Nome                                 | Descrição                                                                                                                             | Rastreabilidade |
|--------|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|----------------|
| RF01   | Importar e Consolidar Histórico      | O sistema deve permitir a importação de arquivos de histórico e consolidar os dados em uma base local.                                 | C01           |
| RF02   | Calcular Lucro Total                 | O sistema deve calcular o lucro total dos jogos importados.                                                                            | C03           |
| RF03   | Calcular ROI                        | O sistema deve calcular o Retorno Sobre o Investimento (ROI) dos jogos importados.                                                     | C03           |
| RF04   | Calcular Taxa de Vitórias            | O sistema deve calcular a porcentagem de vitórias do jogador nos torneios.                                                             | C03           |
| RF05   | Segmentar Análises por jogador       | O sistema deve permitir a segmentação das análises de desempenho com base no jogador.                                                 | C02           |
| RF06   | Segmentar Análises por tipo de torneio| O sistema deve permitir a segmentação das análises de desempenho com base no tipo de torneio.                                         | C02           |
| RF07   | Visualizar Gráfico de Linha de Evolução| O sistema deve gerar um gráfico de linha que exibe a evolução de uma métrica selecionada ao longo do tempo.                           | C04           |
| RF08   | Listar Histórico de Importações      | O sistema deve listar todos os arquivos de histórico já importados. A lista deve conter, para cada arquivo: nome, data e quantidade.   | C01           |
| RF09   | Exibir Histórico de Transações       | O sistema deve registrar e exibir o histórico de transações da conta do jogador (depósitos e saques).                                 | C06           |
| RF10   | Calcular ITM (In The Money)          | O sistema deve calcular a porcentagem de vezes que o jogador termina em uma posição premiada (ITM).                                   | C03           |

## Lista de Requisitos Não Funcionais

<font size="3"><p style="text-align: left">**Tabela 2** - Requisitos não funcionais.</p></font>

Os requisitos não funcionais especificam as qualidades e restrições do sistema, como desempenho, segurança e usabilidade, que não estão diretamente relacionadas às funcionalidades oferecidas, mas são essenciais para garantir a qualidade do software. A classificação segue o modelo de usabilidade, confiabilidade, desempenho, suportabilidade e restrições.

| Categoria         | Código | Descrição                                                                                                                    | Rastreabilidade |
|-------------------|--------|------------------------------------------------------------------------------------------------------------------------------|----------------|
| Desempenho        | RNF01  | O sistema deve processar um lote de 100 arquivos de histórico e gerar as análises correspondentes em menos de 10 segundos.   | C05           |
| Usabilidade       | RNF02  | As operações de importação de arquivos e visualização das métricas devem ser concluídas em, no máximo, 3 ações do usuário. | C05           |
| Confiabilidade    | RNF03  | O sistema deve garantir a consistência e a integridade dos dados durante os processos de importação, padronização e cálculo.| C01, C03, C05 |
| Suportabilidade   | RNF04  | A aplicação deve ser compatível e executável no sistema operacional Windows.                                                 | C05           |
| Implementação     | RNF05  | O sistema deve ser desenvolvido em linguagem Python e distribuído como um arquivo executável (.exe).                        | C05, C01      |
| Interface         | RNF06  | O sistema deve utilizar um banco de dados local para armazenar o histórico de importações e os dados processados.           | C05           |

## Histórico de Versões

<font size="3"><p style="text-align: left">**Tabela 3** - Histórico de versões.</p></font>

| Versão |        Descrição         |                      Autor(es)                      |    Data    |
| :----: | :----------------------: | :-------------------------------------------------: | :--------:  
|  1.0   | Criação do documento |  [Felipe Rodrigues](https://github.com/felipeJRdev)      | 15/10/2025 | 
|  2.0   | Ajustes no documento |  [Felipe Rodrigues](https://github.com/felipeJRdev)      | 20/10/2025 | 