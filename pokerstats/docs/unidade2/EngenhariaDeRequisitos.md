# Engenharia de Requisitos

## Atividades e Técnicas da ER 

---

### Planejamento

#### Elicitação e descoberta

- **Brainstorm**: É uma técnica de criatividade coletiva que visa gerar o máximo de ideias e soluções possíveis em grupo, em um ambiente livre de críticas. No projeto "Poker Stats", o brainstorm foi empregado pela equipe para idealizar as funcionalidades e as características do produto (minimalismo, foco em Bodog ) e para gerar a proposta inicial de solução, focada em resolver o problema da falta de dados consolidados de desempenho.
   Evidência: Proposta de solução.

- **Entrevista**: Consiste em sessões de perguntas e respostas, formais ou informais, com o cliente ou usuários-chave para obter uma compreensão profunda de suas necessidades. No "Poker Stats", as entrevistas com Eduardo foram o método primário para entender o cenário atual , a dificuldade de consolidação manual e identificar as métricas-chave que ele realmente valorizava, como o lucro por torneio e o ROI.
  Evidência: Prints de reuniões com o cliente.

- **Análise de concorrentes**: É o estudo de produtos ou sistemas existentes no mercado para identificar lacunas, melhores práticas e definir como o novo produto deve se diferenciar e agregar valor. Esta análise no "Poker Stats" revelou que as soluções profissionais (como PokerTracker) eram complexas e caras , permitindo que o projeto se posicionasse como uma alternativa personalizada, minimalista e acessível, focada na plataforma Bodog e nas métricas essenciais de Eduardo. 
  Evidência: Tópico 2.4 do documento de visão.

#### Análise e consenso

- **Priorização MOSCOW**: uma técnica usada para priorização e classificação dos requisitos em Must have (essencial), Should have (importante), Could have (desejável) e Won't have , baseada no valor de negócio para o cliente. Foi fundamental para definir o escopo do Produto Mínimo Viável (MVP) do "Poker Stats", garantindo que funcionalidades essenciais (como Importação de Histórico e Cálculo de ROI ) fossem entregues na primeira iteração. 
	Evidência: O próprio MoSCoW (gráfico e tabela).

- **User points**: É uma técnica de estimativa relativa (não baseada em horas) que mede o esforço, a complexidade, a incerteza e o risco envolvidos na implementação de uma User Story. No "Poker Stats", a equipe utilizou essa escala (MB, B, M, A, MA ) para ponderar o valor de negócio (MoSCoW) com o custo de desenvolvimento, subsidiando a decisão de quais requisitos incluir no MVP. 
  Evidência: A avaliação técnica no backlog e a coluna "Nível de Esforço" na tabela de priorização.

- **Análise de custo / benefício**: Sendo utilizada para avaliar o valor de um requisito em relação ao custo ou esforço de implementá-lo. No "Poker Stats", esta análise, combinada com o MoSCoW e Story Points, ajudou a equipe a justificar a inclusão ou exclusão de requisitos no MVP, garantindo que o tempo fosse investido nas funcionalidades que maximizam o impacto na gestão da banca de Eduardo. 
  Evidência: O gráfico de MoSCoW e análise de Complexidade Técnica (Story Points - Custo).

- **Discussão em equipe**:  Realização de encontros (formais ou informais) onde os membros do time analisam requisitos, resolvem problemas técnicos e compartilham conhecimento. No contexto de Kanban + XP, essas discussões (Refinamento) são cruciais para manter a disciplina de engenharia e garantir que as Histórias de Usuário atendam ao DoR (Definition of Ready) antes de entrar no fluxo de desenvolvimento. 
  Evidência: Prints ou gravações de reuniões de refinamento (Discussões em Equipe)

#### Declaração

- **Documentação de visão**: O Documento de Visão começa com uma declaração de propósito, uma narrativa concisa que articula por que o projeto é necessário e como ele se alinha aos objetivos estratégicos da organização. Esta declaração estabelece o contexto para todo o empreendimento e fornece uma âncora para as decisões futuras. 
	Evidência: O próprio documento de Visão

### Execução

#### Representação:

- **Protótipos**:São modelos ou representações visuais rápidos das telas ou funcionalidades do sistema, utilizados para obter feedback precoce do cliente sobre a interface (Representação). No "Poker Stats", eles garantiram que a visualização de dados complexos (gráficos de linha, painéis de métricas ) fosse clara, intuitiva e agradasse o usuário casual Eduardo.
 Evidência: Os próprios protótipos.

#### **Verificação e validação**:

- **Dor e Dod**: O DoR é o acordo da equipe que define quando um requisito está apto para o desenvolvimento, garantindo que a História de Usuário esteja clara, o valor de negócio compreendido e que os Critérios de Aceitação estejam definidos e testáveis, evitando que o time comece a trabalhar em requisitos ambíguos. Já o DoD é o acordo que define quando uma funcionalidade está verdadeiramente concluída, agregando valor utilizável ao produto. No projeto, o DoD reforça as Práticas XP, exigindo que o código siga padrões, que os Testes estejam passando (seguindo a abordagem TDD) e que o código seja revisado e validado pelo cliente, assegurando a robustez necessária para o tratamento de dados .
	Evidência: O próprio Dor e DoD

### Review

#### Verificação e validação

- **Feedback**:  O processo contínuo de obtenção de retorno sobre as entregas do produto, essencial em metodologias Ágeis. No "Poker Stats", o feedback formal do cliente ocorria em Validation Meetings após a conclusão de incrementos (validação funcional ), permitindo ajustes rápidos e garantindo que o produto permanecesse alinhado com suas métricas de interesse. 
  Evidência: Registros de reuniões de feedback (implícito nas reuniões de validação e nos registros de entrevistas).

#### **Organização e atualização**

- Revisão do backlog: a atividade contínua de inspeção e adaptação do backlog de requisitos, onde as Histórias de Usuário são refinadas, reavaliadas quanto à prioridade (MoSCoW) e estimativa (Story Points), e organizadas. No "Poker Stats", esta prática garante que a equipe, operando em um fluxo Kanban, esteja sempre pronta para trabalhar no item de maior valor. 
  Evidência: O próprio backlog e o quadro Kanban atualizado.









<font size="3"><p style="text-align: left">**Tabela 2** - Histórico de versões.</p></font>

| Versão |        Descrição         |                      Autor(es)                      |    Data    |
| :----: | :----------------------: | :-------------------------------------------------: | :--------:  
|  1.0   | Criação do documento no pages | [Felipe Junior](https://github.com/Felipej3ds)          | 19/10/2025 | 
| 1.1   | Atualizar o documento no pages |[Felipe Junior](https://github.com/Felipej3ds)          | 05/11/2025 | 