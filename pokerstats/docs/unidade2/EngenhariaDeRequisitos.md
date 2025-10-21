# Engenharia de Requisitos

## Atividades e Técnicas da ER em Kanban + Práticas XP

No projeto **Poker Stats**, o trabalho é organizado em um **fluxo contínuo**, focado em entregar valor rapidamente e com alta qualidade técnica.

As técnicas utilizadas foram baseadas no livro *eXtreme Programming: práticas para o dia a dia no desenvolvimento ágil de software* (WILDT et al., 2013).

---

### 1. Gestão do Backlog (O Fluxo de Descoberta)

Atividades que ocorrem antes e durante o desenvolvimento:

- **Elicitação e Descoberta:**  
  - **Entrevistas:** Realizadas com o cliente (Eduardo) para entender métricas importantes (lucro, ROI, etc.) e dificuldades com relatórios manuais.

- **Análise e Consenso:**  
  - **Priorização Contínua:** Uso de ranking no backlog para garantir foco nas funcionalidades de maior valor.  
  - **Discussões em Equipe (Refinamento):** Reuniões técnicas para definir fórmulas e viabilidade da extração de dados da Bodog.  
  - **Visualizar o Fluxo de Trabalho:** Tornar o processo visível (Kanban) para detectar gargalos e promover decisões baseadas em dados reais.  
  - **Gerenciamento de Fluxo:** Acompanhamento de métricas (tempo de ciclo, gargalos) para garantir fluxo eficiente.  
  - **Implementar Ciclos de Feedback:** Reuniões de revisão e melhoria contínua para ajustar produto e processo.  

- **Declaração:**  
  - **Criação de Épicos e User Stories:** Exemplo: “Como Eduardo, quero calcular o ROI de cada torneio para saber onde sou mais lucrativo.”  
  - **Tornar as Políticas Explícitas:** Definição clara de critérios, prioridades e práticas (como TDD e padrões de código).

---

### 2. Fluxo de Desenvolvimento (O Fluxo de Entrega)

Atividades que ocorrem quando um item é puxado para desenvolvimento:

- **Representação:**  
  - **TDD (Test-Driven Development):** Escrever testes antes do código, garantindo validação contínua e documentação viva.  
  - **Protótipos Rápidos:** Wireframes e mockups do dashboard para alinhar visualmente as métricas com o cliente.  
  - **Refatoração:** Melhoria contínua do código sem alterar seu comportamento, assegurando legibilidade e manutenção.  

- **Verificação e Validação:**  
  - **DoR e DoD:** Verificar se os critérios estão prontos e concluídos corretamente.  
  - **Checklists de Validação:** Garantir que os requisitos atendam aos critérios de aceitação.  
  - **Propriedade Coletiva do Código:** Todos os desenvolvedores têm acesso e responsabilidade sobre o código.  
  - **Integração Contínua:** Garantir builds e testes automáticos frequentes, mantendo o sistema sempre funcional.  

- **Organização e Atualização:**  
  - **Quadro Kanban:** Visualização contínua do status de cada tarefa.  
  - **Limitação de WIP:** Foco em poucas tarefas simultâneas para manter fluxo previsível.  
  - **Pequenas Entregas:** Publicações frequentes para obter feedback rápido.  
  - **Mapa de Rastreabilidade:** Relação entre histórias, requisitos e objetivos do negócio.  

---

### 3. Melhoria Contínua do Processo

Atividades periódicas de análise e refinamento do processo:

- **Análise e Organização:**  
  - **Métricas de Fluxo (Lead Time, Cycle Time):** Medição do tempo total e por fase das tarefas.  
  - **Reuniões de Cadência:** Discussão dos gargalos e melhorias possíveis com base em dados reais.  

- **Atualização do Processo:**  
  - **Ajustes no Quadro Kanban:** Exemplo — adicionar coluna “Validação de Dados” para checar consistência dos arquivos Bodog.  
  - **Refinamento das Políticas Explícitas:** Atualização do DoR e DoD para incluir novos critérios, como validações de ROI e Lucro.  
  - **Ritmo Sustentável:** Garantir equilíbrio entre produtividade e qualidade, evitando sobrecarga da equipe.  

---

## Engenharia de Requisitos e o Kanban/XP

A seguir, apresenta-se a relação entre as **áreas da Engenharia de Requisitos** e as **práticas aplicadas** no contexto do projeto *Poker Stats*, combinando **Kanban** e **Extreme Programming (XP)**.  
O objetivo é evidenciar como as atividades da ER foram incorporadas ao fluxo ágil e à cultura de qualidade contínua da equipe.

---

| **Área de Atividades** | **Atividades de ER** | **Práticas Técnicas (Kanban + XP)** | **Resultado Esperado** |
|------------------------|----------------------|--------------------------------------|-------------------------|
| **Gestão do Backlog (Descoberta)** | Elicitação e Análise de Domínio | Entrevistas com o cliente, análise dos arquivos Bodog, identificação de métricas prioritárias (lucro, ROI, ITM) | Entendimento profundo das necessidades do cliente e das restrições técnicas dos dados. |
| **Gestão do Backlog (Análise e Consenso)** | Priorização e Refinamento Contínuos | Técnica MoSCoW, Discussões em Equipe, Visualização do Fluxo, Gestão de Gargalos | Backlog vivo, priorizado por valor de negócio e viabilidade técnica, com visibilidade total do progresso. |
| **Declaração** | Criação de Épicos e User Stories | Formato padrão (“Como..., quero..., para que...”), Critérios de Aceitação, Definition of Ready (DoR) | Requisitos claros, testáveis e alinhados com os objetivos de valor para o cliente. |
| **Fluxo de Desenvolvimento (Representação)** | Tradução dos Requisitos em Código | Desenvolvimento Orientado a Testes (TDD), Protótipos Rápidos, Refatoração Contínua | Código limpo, testável e validado continuamente; interfaces alinhadas às expectativas do cliente. |
| **Fluxo de Desenvolvimento (Validação)** | Verificação e Validação dos Requisitos | Checklists de Aceitação, Definition of Done (DoD), Propriedade Coletiva do Código, Integração Contínua (CI) | Qualidade técnica e funcional garantidas; código revisado e testado por toda a equipe. |
| **Organização e Atualização do Fluxo** | Visualização e Controle do Trabalho | Quadro Kanban, Limitação de WIP, Pequenas Entregas, Mapa de Rastreabilidade | Fluxo de trabalho previsível, transparente e rastreável entre requisitos, código e produto. |
| **Melhoria Contínua** | Análise e Evolução do Processo | Métricas de Fluxo (Lead Time, Cycle Time), Reuniões de Cadência, Ajustes no Quadro, Refinamento das Políticas Explícitas | Processos aprimorados com base em dados reais e feedback coletivo. |
| **Sustentabilidade do Processo** | Gestão de Ritmo e Equilíbrio | Ritmo Sustentável, Revisão de Políticas (DoR/DoD), Feedback Contínuo com o Cliente | Entregas frequentes, previsíveis e de alta qualidade, mantendo o bem-estar e o desempenho da equipe. |

---
## Histórico de Versões

<font size="3"><p style="text-align: left">**Tabela 2** - Histórico de versões.</p></font>

| Versão |        Descrição         |                      Autor(es)                      |    Data    |
| :----: | :----------------------: | :-------------------------------------------------: | :--------:  
|  1.0   | Criação do documento | [Felipe Junior](https://github.com/Felipej3ds)          | 19/10/2025 | 