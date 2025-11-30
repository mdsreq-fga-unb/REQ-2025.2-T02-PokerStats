# Engenharia de Requisitos


- Engenharia de Requisitos alinhada às Fases / Marcos de Execução do XP: A Engenharia de Requisitos, quando aplicada dentro de um processo ágil como o Extreme Programming (XP), distribui suas atividades ao longo dos marcos naturais do ciclo de vida do XP. A seguir, as atividades, técnicas, evidências e artefatos do projeto “Poker Stats” são organizados conforme as fases:

## Atividades e Técnicas da ER 

---

### 1. Exploration (Exploração)

- Levantamento inicial, descoberta do domínio e entendimento do problema.

#### Elicitação e descoberta

- **Brainstorm**: Técnica coletiva usada para gerar o máximo de ideias sobre funcionalidades e características do produto. No “Poker Stats”, permitiu definir conceitos iniciais como minimalismo, foco na plataforma Bodog e necessidade de consolidação automática de dados.
Evidência: Proposta de solução.

- **Entrevista**: Reuniões com o cliente para levantar necessidades reais, contexto de uso e problemas enfrentados. As entrevistas com Eduardo revelaram as principais métricas desejadas (lucro por torneio, ROI, saldo diário).
Evidência: Prints das reuniões com o cliente.

- **Análise de concorrentes**: Avaliação de ferramentas como PokerTracker para identificar lacunas e definir o posicionamento do “Poker Stats” como solução minimalista e acessível.
Evidência: Tópico 2.4 do Documento de Visão.

### 2. Planning / Commitment (Planejamento e Compromisso)

- Decisão do escopo da próxima Release e definição do MVP.

#### Análise e consenso

- **Priorização MOSCOW**: Classificação dos requisitos em Must, Should, Could e Won’t. Essencial para definir o escopo do MVP, garantindo a entrega de funcionalidades críticas como Importação de Histórico e Cálculo de ROI.
Evidência: Tabela e gráfico MoSCoW.

- **User points**: Estimativa relativa de esforço, complexidade e risco usando a escala (MB, B, M, A, MA). Esse esforço foi cruzado com MoSCoW para montar o MVP equilibrando valor x custo.
Evidência: Avaliação técnica no backlog (coluna Nível de Esforço).

- **Análise de custo / benefício**: Avalia o retorno esperado em relação ao esforço de implementação. No projeto, ajudou a priorizar funcionalidades de maior impacto na gestão da banca.
Evidência: Gráfico MoSCoW + análise de complexidade técnica.

- **Discussão em equipe**: Reuniões de alinhamento entre os membros do time para debater requisitos, riscos e soluções técnicas. Essenciais no modelo Kanban + XP para garantir que histórias atendam ao DoR antes do desenvolvimento.
Evidência: Prints ou gravações das reuniões.

#### **Declaração**: 

- **User Story**: Uma User Story (ou “história do usuário”) é uma ferramenta usada em metodologias ágeis (como Scrum ou Kanban) para capturar uma funcionalidade do ponto de vista do usuário final. Ela descreve quem precisa de algo, o que precisa e por quê, ajudando a equipe a entender o valor da funcionalidade antes de desenvolvê-la.
Evidêcia: As users Story no backlog

### 3. Iterations to Release (Iterações até a Release)

- Desenvolvimento contínuo; requisitos são refinados imediatamente antes da implementação.

#### Representação:

- **Protótipos**: Mockups rápidos usados para validar visualização de dados, gráficos, métricas e fluxo de navegação. Permitiram feedback contínuo de Eduardo durante as iterações.
Evidência: Protótipos utilizados.

#### **Verificação e validação**:

- **Dor e Dod**: O DoR é o acordo da equipe que define quando um requisito está apto para o desenvolvimento, garantindo que a História de Usuário esteja clara, o valor de negócio compreendido e que os Critérios de Aceitação estejam definidos e testáveis, evitando que o time comece a trabalhar em requisitos ambíguos. Já o DoD é o acordo que define quando uma funcionalidade está verdadeiramente concluída, agregando valor utilizável ao produto. No projeto, o DoD reforça as Práticas XP, exigindo que o código siga padrões, que os Testes estejam passando (seguindo a abordagem TDD) e que o código seja revisado e validado pelo cliente, assegurando a robustez necessária para o tratamento de dados .
	Evidência: Documento de DoR e DoD.

- **Feedback**: Um feedback do cliente sobre o sistema, incluindo layout e funcionalidades implementadas, coletado por meio de um formulário no Google Forms.
	Evidencias: formularios respondido no google formularios.

### 4. Productionizing (Preparação para Produção)


#### **Organização e atualização**

- Revisão do backlog: Atividade contínua para garantir que o backlog esteja priorizado, atualizado e alinhado com as necessidades do cliente. Inclui reorganização de prioridades (MoSCoW), reestimativas e refinamento.
No modelo Kanban + XP do projeto, mantém o fluxo sempre pronto para novas entregas.
Evidência: Backlog organizado e quadro Kanban atualizado.









<font size="3"><p style="text-align: left">**Tabela 2** - Histórico de versões.</p></font>

| Versão |        Descrição         |                      Autor(es)                      |    Data    |
| :----: | :----------------------: | :-------------------------------------------------: | :--------:  
|  1.0   | Criação do documento no pages | [Felipe Junior](https://github.com/Felipej3ds)          | 19/10/2025 | 
| 1.1   | Atualizar o documento no pages |[Felipe Junior](https://github.com/Felipej3ds)          | 05/11/2025 | 