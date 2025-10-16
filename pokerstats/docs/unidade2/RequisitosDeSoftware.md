# 7. REQUISITOS DE SOFTWARE

Esta seção descreve os requisitos necessários para o desenvolvimento do software. Ela está dividida em requisitos funcionais e não funcionais, que apresentam as funcionalidades do sistema e as qualidades que ele deve possuir para atender às expectativas dos usuários.

## 7.1 Lista de Requisitos Funcionais

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

## 7.2 Lista de Requisitos Não Funcionais

Os requisitos não funcionais especificam as qualidades e restrições do sistema, como desempenho, segurança e usabilidade, que não estão diretamente relacionadas às funcionalidades oferecidas, mas são essenciais para garantir a qualidade do software. A classificação segue o modelo de usabilidade, confiabilidade, desempenho, suportabilidade e restrições.

| Categoria         | Código | Descrição                                                                                                                    | Rastreabilidade |
|-------------------|--------|------------------------------------------------------------------------------------------------------------------------------|----------------|
| Desempenho        | RNF01  | O sistema deve processar um lote de 100 arquivos de histórico e gerar as análises correspondentes em menos de 10 segundos.   | C05           |
| Usabilidade       | RNF02  | As operações de importação de arquivos e visualização das métricas devem ser concluídas em, no máximo, 3 ações do usuário. | C05           |
| Confiabilidade    | RNF03  | O sistema deve garantir a consistência e a integridade dos dados durante os processos de importação, padronização e cálculo.| C01, C03, C05 |
| Suportabilidade   | RNF04  | A aplicação deve ser compatível e executável no sistema operacional Windows.                                                 | C05           |
| Implementação     | RNF05  | O sistema deve ser desenvolvido em linguagem Python e distribuído como um arquivo executável (.exe).                        | C05, C01      |
| Interface         | RNF06  | O sistema deve utilizar um banco de dados local para armazenar o histórico de importações e os dados processados.           | C05           |
