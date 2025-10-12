cat > 7_requisitos_de_software.md << 'EOF'
# 7. REQUISITOS DE SOFTWARE

Esta seção define os requisitos funcionais e não funcionais do Poker Stats.

## 7.1 Requisitos Funcionais

| Código | Nome | Descrição | Rastreabilidade |
|--------|------|------------|----------------|
| RF01 | Importar e Consolidar Histórico | Permitir importação e consolidação de arquivos da Bodog. | C01 |
| RF02 | Calcular Lucro Total | Calcular o lucro total dos jogos. | C03 |
| RF03 | Calcular ROI | Calcular o Retorno Sobre o Investimento (ROI). | C03 |
| RF04 | Calcular Taxa de Vitórias | Calcular a porcentagem de vitórias. | C03 |
| RF05 | Exibir Painel de Métricas | Mostrar métricas de desempenho em painel. | C03 |
| RF06 | Segmentar Análises | Filtrar por tipo de torneio. | C02 |
| RF07 | Visualizar Gráfico de Evolução | Exibir evolução de métricas ao longo do tempo. | C04 |
| RF08 | Listar Histórico de Importações | Listar arquivos importados. | C01 |
| RF09 | Exibir Histórico de Transações | Mostrar depósitos e saques. | C06 |
| RF10 | Calcular ITM | Calcular porcentagem de vezes “In The Money”. | C03 |

## 7.2 Requisitos Não Funcionais

| Categoria | Código | Descrição | Rastreabilidade |
|------------|---------|------------|----------------|
| Desempenho | RNF01 | Processar 100 arquivos em <10s | C05 |
| Usabilidade | RNF02 | Importação e visualização em até 3 cliques | C05 |
| Confiabilidade | RNF03 | Garantir integridade dos dados | C01, C03 |
| Suportabilidade | RNF04 | Compatível com Windows | C05 |
| Implementação | RNF05 | Desenvolvido em Python (.exe) | C05, C01 |
| Interface | RNF06 | Usar banco de dados local | C05 |

EOF
