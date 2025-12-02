# Especificação de Caso de Uso: Monitorar Desempenho do Sistema 

## 1 Nome do Caso de Uso

- Monitorar Desempenho do Sistema

### 1.1 Breve Descrição

- Este caso de uso permite ao Administrador do Sistema acessar painéis e relatórios para 
acompanhar indicadores técnicos, métricas de segurança, desempenho geral e o número de 
usuários ativos na plataforma ConnectCare. O objetivo é garantir a manutenção técnica e 
operacional da plataforma, identificar gargalos e planejar ações de melhoria.

### 1.2 Atores

- Ator Principal: Administrador do Sistema 
- Atores Secundários: Não se aplica (o sistema de monitoramento atua internamente e 
não há interações diretas com outros atores para este fim).

## 2 Fluxo de Eventos 

### 2.1  Fluxo Principal

- Este caso de uso é iniciado quando o Administrador do Sistema (Admin) acessa o módulo de 
monitoramento após autenticação. 

**2.1.1** O Admin seleciona a opção "Monitorar Desempenho do Sistema" no menu principal.  
**2.1.2** O sistema verifica a permissão do Admin para acessar os indicadores de desempenho e 
segurança [RN01] [FE01].  
**2.1.3** O sistema exibe um Dashboard de Desempenho Operacional.  
**2.1.4** O Dashboard apresenta os seguintes indicadores-chave em tempo real ou com 
atualização frequente: * Indicadores Técnicos: Tempo de resposta da aplicação, status dos 
servidores e consumo de recursos. * Métricas de Usuários: Número de usuários ativos, picos 
de acesso e tendência de uso. * Registro de Erros (Log de Incidentes): Contagem de erros 
na plataforma e lista de eventos não esperados. * Segurança: Alertas de tentativas de acesso 
não autorizado ou falhas na segurança dos dados.  
**2.1.5** O Admin pode selecionar um período específico para análise ou um indicador para 
detalhamento [FA01].  
**2.1.6** O Admin realiza as atividades de monitoramento e encerra a sessão.  
**2.1.7** O caso de uso é encerrado. 

### 2.2 Fluxos 

**2.2.1** [FA01] Detalhar Indicador ou Alterar Período 
No passo 2.1.5, o Admin opta por uma visualização detalhada ou por alterar o período de 
análise. 

**2.2.1.1** O Admin clica em um indicador (ex: "Log de Incidentes") ou seleciona um novo período 
(ex: "últimos 7 dias").  

**2.2.1.2** O sistema processa a requisição e exibe o relatório ou gráfico detalhado para o 
indicador/período selecionado [FE02]. 

**2.2.1.3** O sistema permite a exportação do relatório detalhado para formatos CSV ou PDF. 

**2.2.1.4** O Admin retorna ao Dashboard principal (Retorna ao passo 2.1.3).

## 3. Requisitos Especiais

**3.1** O Dashboard de Desempenho deve ser responsivo e renderizar corretamente em 
monitores de alta resolução e dispositivos móveis de manutenção.  

**3.2** O sistema deve realizar a coleta dos indicadores de desempenho de forma não intrusiva, 
garantindo que o processo de monitoramento não afete a performance da plataforma principal.  

**3.3** Os dados de monitoramento críticos (log de segurança e indicadores de erro) devem ser 
retidos por um período mínimo de 180 dias para fins de auditoria e análise de tendências. 

## 4. Regras de Negócio

**4.1.1** [RN01] Permissão de Acesso ao Módulo de Monitoramento Apenas o Administrador do 
Sistema e outros perfis explicitamente configurados para funções de TI podem acessar o 
módulo de desempenho. 

**4.1.2** [RN02] Auditoria de Acesso aos Dados de Monitoramento: Todo acesso, visualização e 
exportação de relatórios de desempenho e segurança deve ser registrado em um log de 
auditoria, contendo o usuário, data, hora e o tipo de informação acessada, para fins de 
conformidade e segurança.

## 5. Precondições 

**5.1** O Administrador do Sistema deve estar autenticado na plataforma ConnectCare. 5.2 Os 
serviços de coleta de métricas e de log de erros devem estar em execução.

## 6. Pós-condições

**6.1** O log de acesso ao módulo de desempenho é registrado para fins de auditoria. 

## 7. Pontos de Extensão 

**Não se aplica.**