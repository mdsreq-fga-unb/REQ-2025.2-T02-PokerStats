# REQUISITOS DE SOFTWARE:

## Backlog Geral

- Esta seção descreve os requisitos necessários para o desenvolvimento do software. Ela está dividida em requisitos funcionais e não funcionais, que apresentam as funcionalidades do sistema e as qualidades que ele deve possuir para atender às expectativas dos usuários.

### Características do produto

Para facilitar a visão da rastreabilidade, abaixo as características da solução apresentadas novamente:

- [C01] O sistema permitirá a importação de múltiplos arquivos de histórico de jogo da plataforma Bodog, com padronização de formatos e unificação das informações em um ambiente centralizado.
- [C02] A aplicação permitirá a segmentação das análises de desempenho com base no tipo de torneio e jogador.
- [C03] O software irá calcular e exibir automaticamente as métricas essenciais de desempenho, incluindo lucro, ROI, porcentagem de vitórias e ITM (In The Money).
- [C04] Serão disponibilizadas análises de desempenho com comparativos históricos para visualização da evolução do jogador ao longo do tempo.
- [C05] O sistema será otimizado para o processamento eficiente de grandes volumes de dados, com geração de análises de forma rápida.
- [C06] A aplicação permitirá o registro e a visualização do histórico de transações financeiras (depósitos e saques), auxiliando na gestão de banca do jogador.

### Lista de Requisitos Funcionais

Os requisitos funcionais descrevem as funcionalidades funcionais que o sistema deve implementar para atender às necessidades do negócio. Eles incluem integrações, processos e interações do usuário com o sistema.

| **Código** | **Nome** | **Descrição** | **Rastreabilidade** | **IH Histórias** |
|-------------|-----------|----------------|----------------------|------------------|
| **RF01** | Importar e Consolidar Histórico | O sistema deve permitir a importação de arquivos de histórico e consolidar os dados em uma base local. | C01 | US1 |
| **RF02** | Calcular Lucro Total | O sistema deve calcular o lucro total dos jogos importados. | C03 | US2 |
| **RF03** | Calcular ROI | O sistema deve calcular o Retorno Sobre o Investimento (ROI) dos jogos importados. | C03 | US3 |
| **RF04** | Calcular Taxa de Vitórias | O sistema deve calcular a porcentagem de vitórias do jogador nos torneios. | C03 | US4 |
| **RF05** | Segmentar Análises por jogador | O sistema deve permitir a segmentação das análises de desempenho com base no jogador. | C02 | US5 |
| **RF06** | Segmentar Análises por tipo de torneio | O sistema deve permitir a segmentação das análises de desempenho com base no tipo de torneio. | C02 | US6 |
| **RF07** | Visualizar Gráfico de Linha de Evolução | O sistema deve gerar um gráfico de linha que exibe a evolução de uma métrica selecionada ao longo do tempo. | C04 | US7 |
| **RF08** | Listar Histórico de Importações | O sistema deve listar todos os arquivos de histórico já importados. A lista deve conter, para cada arquivo, as seguintes informações: nome do arquivo, data de importação e quantidade de torneios processados. | C01 | US8 |
| **RF09** | Exibir Histórico de Transações | O sistema deve registrar e exibir o histórico de transações da conta do jogador (depósitos e saques). | C06 | US9 |
| **RF10** | Calcular ITM (In The Money) | O sistema deve calcular a porcentagem de vezes que o jogador terminou em uma posição premiada (ITM). | C03 | US10 |


### Lista de Requisitos Não Funcionais

Os requisitos não funcionais especificam as qualidades e restrições do sistema, como desempenho, segurança e usabilidade, que não estão diretamente relacionadas às funcionalidades oferecidas, mas são essenciais para garantir a qualidade do software. A classificação segue o modelo  de usabilidade, confiabilidade, desempenho, suportabilidade e restrições.

| **Categoria** | **Código** | **Descrição** | **Rastreabilidade** |
|----------------|-------------|----------------|----------------------|
| **Desempenho** | RNF01 | O sistema deve processar um lote de 100 arquivos de histórico e gerar as análises correspondentes em menos de 10 segundos. | C05 |
| **Usabilidade** | RNF02 | As operações de importação de arquivos e visualização das métricas devem ser concluídas em, no máximo, 3 ações do usuário (cliques) a partir da tela principal. | C05 |
| **Suportabilidade** | RNF04 | A aplicação deve ser compatível e executável no sistema operacional Windows. | C05 |
| **Requisitos de Implementação** | RNF05 | O sistema deve ser desenvolvido em linguagem Python e distribuído como um arquivo executável (.exe), sem a necessidade de um instalador. | C05 |
| **Requisitos de Interface** | RNF06 | O sistema deve utilizar um banco de dados local para armazenar o histórico de importações e os dados processados, sem depender de um servidor externo. | C05 |
