# Especificação de Caso de Uso – Agendar Consulta

## 1. Nome do Caso de Uso
**Agendar Consulta**

## 1.1 Breve Descrição
Este caso de uso permite que o **Paciente** localize horários disponíveis e realize o agendamento de uma consulta presencial ou online em uma unidade de saúde, recebendo confirmação com detalhes do atendimento.

## 1.2 Atores
- **Ator Principal:** Paciente  
- **Atores Secundários:** Sistema de Agenda, Profissional de Saúde (consultado apenas para disponibilidade)

---

## 2. Fluxo de Eventos

### 2.1 Fluxo Principal
2.1.1 O Paciente acessa a funcionalidade **“Agendar Consulta”**.  
2.1.2 O Sistema exibe os filtros de busca (localização, tipo de atendimento, especialidade, disponibilidade).  
2.1.3 O Paciente insere os filtros desejados e solicita a busca. **[RN01]**  
2.1.4 O Sistema consulta a disponibilidade nas unidades de saúde cadastradas.  
2.1.5 O Sistema apresenta a lista de serviços e horários disponíveis.  
2.1.6 O Paciente seleciona um serviço e um horário.  
2.1.7 O Sistema exibe os detalhes do atendimento (local, documentos necessários, tipo da consulta).  
2.1.8 O Paciente confirma a solicitação de agendamento.  
2.1.9 O Sistema valida se o horário ainda está disponível. **[RN02]**  
2.1.10 O Sistema registra o agendamento no banco de dados.  
2.1.11 O Sistema envia confirmação da consulta ao Paciente.  
2.1.12 O Caso de Uso é encerrado.

---

### 2.2 Fluxos Alternativos (FA)

#### FA01 – Buscar sem filtros  
**Origem:** passo 2.1.3  
2.2.1 O Paciente opta por não informar filtros.  
2.2.2 O Sistema retorna todos os atendimentos disponíveis ordenados por proximidade.  
**Retorno:** passo 2.1.5.

#### FA02 – Falta de transporte e sugestão de atendimento móvel  
**Origem:** passo 2.1.7  
2.2.3 O Paciente informa dificuldade de deslocamento.  
2.2.4 O Sistema sugere unidades móveis, campanhas itinerantes ou agentes comunitários disponíveis na região.  
**Retorno:** passo 2.1.8.

---

### 2.3 Fluxos de Exceção (FE)

#### FE01 – Horário indisponível  
**Origem:** passo 2.1.9  
2.3.1 O Sistema identifica que o horário selecionado foi ocupado por outro usuário.  
2.3.2 O Sistema exibe mensagem informando a indisponibilidade.  
2.3.3 O Sistema retorna à lista de horários.  
**Retorno:** passo 2.1.5.

#### FE02 – Falha de conexão ou consulta à disponibilidade  
**Origem:** passo 2.1.4  
2.3.4 O Sistema não consegue consultar a agenda das unidades.  
2.3.5 O Sistema informa a falha e solicita nova tentativa.  
**Retorno:** passo 2.1.3.

---

## 3. Requisitos Especiais
- **RE01:** O sistema deve funcionar mesmo em conexões instáveis, permitindo reenvio sem perda de dados.  
- **RE02:** A interface deve ser totalmente responsiva para dispositivos de baixa performance.

---

## 4. Regras de Negócio (RN)
- **RN01:** Filtros de busca são opcionais.  
- **RN02:** Um horário só pode ser reservado se estiver disponível no momento da confirmação.  
- **RN03:** O agendamento deve gerar um identificador único.

---

## 5. Precondições
- O Paciente deve estar autenticado no sistema.  
- O sistema deve estar conectado ao banco de dados de agendamentos.

---

## 6. Pós-condições
- Um novo agendamento é registrado.  
- Uma confirmação é enviada ao Paciente.  
- Um log de auditoria é gerado contendo data, horário e usuário.

---

## 7. Pontos de Extensão
- Este caso de uso pode ser estendido por **“Consultar Histórico de Agendamentos”** nos passos 2.1.1 e 2.1.12.  
- Pode ser estendido por **“Cancelar Agendamento”** após o registro da consulta.
