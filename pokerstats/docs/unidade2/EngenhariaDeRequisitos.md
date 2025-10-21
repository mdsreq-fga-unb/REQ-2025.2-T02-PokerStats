# **ENGENHARIA DE REQUISITOS**

## **Atividades e Técnicas da ER em Kanban \+ Práticas XP**

No projeto Poker Stats, o trabalho é organizado em um fluxo contínuo, focado em entregar valor de forma rápida e com alta qualidade técnica.

As técnicas foram retiradas do livro *eXtreme Programming: práticas para o dia a dia no desenvolvimento ágil de software* (WILDT et al., 2013).

### **1\. Gestão do Backlog (O Fluxo de Descoberta)**

*(Atividades que ocorrem antes de o desenvolvimento começar mas continuam durante o desenvolvimento)*

* **Elicitação e Descoberta:**  
  * **Entrevistas:** Realizar entrevistas contínuas com o cliente (Eduardo) para aprofundar o entendimento sobre as métricas mais importantes (lucro, ROI, etc.) e os desafios que ele enfrenta com os relatórios manuais atuais.  
  * **Análise de Domínio de Negócio:** Analisar os arquivos de histórico e planilhas exportados da plataforma Bodog para entender a estrutura dos dados, suas limitações e as regras do poker online que impactam os cálculos.  
* **Análise e Consenso:**  
  * **Priorização Contínua:** Utilizar um ranking simples no backlog para definir a prioridade das funcionalidades em tempo real, garantindo que a equipe sempre trabalhe no que gera mais valor para a análise de desempenho de Eduardo.  
  * **Discussões em Equipe (Refinamento):** Realizar reuniões técnicas para analisar os itens mais prioritários, discutindo a viabilidade de extrair dados específicos dos arquivos da Bodog e definindo as fórmulas matemáticas para as métricas.  
  * **Visualizar o fluxo de trabalho:** Visualizar o Fluxo de Trabalho é o princípio central do Kanban, que propõe tornar visível cada etapa do processo de desenvolvimento desde a criação até a entrega, permitindo que todos compreendam o estado atual das tarefas. Essa visibilidade facilita a identificação de gargalos e promove decisões baseadas em dados reais. No XP, essa transparência reforça práticas como pequenas entregas e feedback contínuo, pois ajuda a equipe a compreender onde o trabalho está parado e onde ajustes são necessários para garantir a entrega constante.  
  * **Gerenciamento de fluxo:** Gerenciar o Fluxo envolve monitorar e ajustar continuamente o andamento das tarefas para garantir que o processo de desenvolvimento seja fluido e eficiente. No Kanban, isso é feito analisando métricas como tempo de ciclo e gargalos, promovendo melhorias no processo. No XP, o gerenciamento do fluxo se relaciona com pequenas entregas e integração contínua, pois ambas exigem acompanhamento constante para manter o software em progresso estável, entregando valor em ciclos curtos e previsíveis.  
  * **Implementar ciclos de feedback:** Implementar Ciclos de Feedback é o ato de buscar e aplicar constantemente o retorno de clientes, usuários e da própria equipe para ajustar o produto e o processo. No XP, o feedback é um dos pilares fundamentais, pequenas entregas e revisões contínuas. No Kanban, os ciclos de feedback ocorrem em revisões regulares do fluxo e reuniões de melhoria, permitindo que a equipe aprenda com os resultados e adapte o processo, garantindo que o sistema evolua de acordo com as necessidades.  
* **Declaração:**  
  * **Criação de Épicos e User Stories:** Organizar as necessidades em Épicos como "Cálculo de Métricas Essenciais" e quebrá-los em User Stories como "Como Eduardo, quero calcular o ROI de cada torneio para saber onde sou mais lucrativo".  
  * **Tornar as políticas explícitas:**  Tornar as Políticas Explícitas significa definir e comunicar claramente as regras, critérios e práticas que regem o trabalho da equipe como prioridades, critérios de inclusão e revisões. No XP, a explicitação das políticas se reflete nas regras simples e acordadas em equipe, como padrões de codificação e práticas de TDD, fortalecendo o consenso e a responsabilidade coletiva sobre a qualidade do produto.

### **2\. Fluxo de Desenvolvimento (O Fluxo de Entrega)**

*(Atividades que ocorrem quando um item é "puxado" para o desenvolvimento)*

* **Representação:**  
  * **Desenvolvimento Orientado a Testes (TDD):** é uma prática em que a equipe define detalhadamente os requisitos na forma de testes automatizados antes de implementar a funcionalidade. O processo consiste em escrever primeiro um teste que descreva o comportamento esperado do sistema, por exemplo, o cálculo de uma métrica com dados de exemplo, e depois desenvolver o código necessário para que o teste seja aprovado. Essa abordagem garante que cada requisito seja explicitamente validado e facilita refatorações seguras. No contexto do XP (Extreme Programming), TDD é central, pois promove qualidade, documentação viva e feedback rápido.   
  * **Protótipos Rápidos:** Criar protótipos e wireframes para o dashboard de visualização de dados, ajudando a alinhar com Eduardo a melhor forma de apresentar as métricas complexas de forma intuitiva.  
  * **Refatoração:**  prática de refatorar continuamente o código, ou seja, melhorar sua estrutura interna sem alterar o comportamento externo, tornando-o mais legível, modular e fácil de manter. Essa atividade elimina duplicações, simplifica métodos e organiza melhor as responsabilidades do sistema, garantindo que o design permaneça limpo e sustentável ao longo do tempo. No XP (Extreme Programming), a fatoração é um princípio essencial, pois apoia o design simples, o TDD e a evolução contínua do software com segurança.  
* **Verificação e Validação:**  
  * **Verificação de DoR e DoD:** Verificar os "Definition of Ready" (DoR) e "Definition of Done" (DoD) estão validados para cada Requisito em reuniões com a equipe.  
  * **Validação de requisitos por meio de checklists:** Validar se os requisitos atendem às expectativas do  usuário por meio de checklists    
  * **Propriedade coletiva do código:** é a prática em que todo o time de desenvolvimento tem acesso e responsabilidade compartilhada sobre todo o código do projeto, podendo modificar qualquer parte sempre que necessário para melhorar a qualidade ou corrigir problemas. No XP (Extreme Programming), essa prática fortalece a colaboração, elimina barreiras entre desenvolvedores e garante que o conhecimento sobre os requisitos e suas implementações seja distribuído, reduzindo dependências individuais.  
  * **Integração contínua:** é a prática de integrar e testar o código com frequência — várias vezes ao dia em um repositório compartilhado, garantindo que as alterações sejam verificadas automaticamente e que o sistema permaneça funcional a cada atualização. No Kanban, a integração contínua contribui para o fluxo estável de trabalho, evitando acúmulo de falhas e retrabalhos, já que problemas são identificados e resolvidos no momento em que surgem, mantendo o processo fluindo de forma previsível e eficiente.  
* **Organização e Atualização:**  
  * **Quadro Kanban:** A organização é feita visualmente no quadro, mostrando o status real de cada métrica ou funcionalidade em desenvolvimento.  
  * **Limitação do Trabalho em Progresso (WIP):** A equipe limita o número de métricas sendo desenvolvidas ao mesmo tempo. Isso garante foco total em terminar um cálculo de cada vez, assegurando sua precisão antes de iniciar o próximo. No Kanban, essa limitação é essencial para manter o fluxo de trabalho estável e previsível. No XP, ela se conecta ao Ritmo Sustentável e ao TDD, já que trabalhar em pequenas partes do sistema permite testar, integrar e entregar continuamente, mantendo alta qualidade e reduzindo desperdício de esforço.  
  * **Pequenas entregas:** Pequenas entregas são incrementos do produto desenvolvidos e disponibilizados com frequência, permitindo que funcionalidades completas sejam testadas e avaliadas rapidamente pelos usuários ou stakeholders. Esse conceito está presente tanto no XP (Extreme Programming), que valoriza entregas contínuas de software funcional para obter feedback rápido e reduzir riscos, quanto no Kanban, onde as tarefas são visualizadas e liberadas progressivamente ao longo do fluxo de trabalho, garantindo que o trabalho em progresso seja limitado e priorizado, favorecendo ajustes ágeis e evolução incremental do sistema.

### **3\. Melhoria Contínua do Processo**

*(Atividades que ocorrem de forma periódica ou contínua para refinar o processo)*

* **Análise e Organização:**  
  * **Análise de Métricas de Fluxo (Lead Time, Cycle Time):** Analisar quanto tempo uma nova métrica leva desde a ideia até a entrega para identificar gargalos (ex: "estamos demorando muito na fase de testes manuais com os arquivos").  
  * **Reuniões de Cadência (Revisão de Processo):** Realizar reuniões periódicas para discutir em grupo os problemas identificados, como dificuldades recorrentes na interpretação dos arquivos da Bodog.  
* **Atualização do Processo:**  
  * **Ajustes no Quadro Kanban:** Otimizar o fluxo de trabalho visualmente, por exemplo, adicionando uma coluna dedicada para a "Validação de Dados". Isso cria uma etapa formal de verificação da consistência dos arquivos da Bodog antes do desenvolvimento.  
  * **Refinamento das Políticas Explícitas:** Aprimorar as regras do time, quando precisar, principalmente a Definition of Done (DoD). Por exemplo, incluir um critério obrigatório como "checklist de verificação dos cálculos de ROI e Lucro foi executado", garantindo a precisão das métricas antes de cada entrega.  
  * **Ritmo sustentável:**  prática de manter uma cadência de trabalho equilibrada e constante, evitando sobrecarga e garantindo produtividade de longo prazo. No XP, isso significa que a equipe deve trabalhar em um ritmo que possa ser mantido indefinidamente, promovendo qualidade e foco em entregas consistentes. No Kanban, o ritmo sustentável está diretamente ligado à limitação do trabalho em progresso (WIP) e à gestão do fluxo, pois controlar a quantidade de tarefas ativas impede acúmulo de estresse, melhora a previsibilidade e ajuda a equipe a manter a performance sem comprometer a qualidade do produto.

## **Engenharia de Requisitos e o Kanban/XP:**

<font size="3"><p style="text-align: left">**Tabela 1** - ER relacionada ao Processo.</p></font>

| Area de atividades | Atividades ER | Prática | Técnica | Resultado Esperado |
| :---- | :---- | :---- | :---- | :---- |
| Gestão do Backlog | Elicitação e Descoberta | Levantamento de Requisitos  | Entrevista.  Análise de Domínio de Negócio. | Análise dos arquivos de histórico da Bodog. Compreensão aprofundada  das necessidades do cliente e das restrições dos dados. |
|  | Análise e Consenso | Revisão do Processo  | Priorização Continua.  Discussões em Equipe. | Discussões técnicas de refinamento. Backlog sempre priorizado pelo que gera mais valor e com os itens do topo tecnicamente viáveis. |
|  | Declaração | Definição de Épicos e User Stories  | Criação de Épicos e User Stories.  Definição de Critérios de Aceitação e Definition of Ready. | Definição de Critérios de Aceitação (DoR)  Requisitos claros, focados no valor para o usuário e prontos para o desenvolvimento sem ambiguidades. |
| Fluxo de Desenvolvimento | Representação | Criação de Protótipos  | TDD. Protótipos Rápidos. | Protótipos Rápidos do dashboard. Testes que funcionam como uma especificação viva e protótipos que validam a interface antes da codificação. |
|  | Verificação e Validação | Verificação do Código | Revisão de Código e Integração Contínua. Testes de Aceitação Automatizados. | Demonstrações para o cliente (Eduardo). Qualidade interna do código garantida e validação de que a funcionalidade atende à necessidade do cliente. |
|  | Organização e Atualização | Organização do Kanban | Quadro Kanban. Limitação do Trabalho em Progresso (WIP). | Limitação do Trabalho em Progresso (WIP).  Transparência total sobre o andamento e um fluxo de trabalho sustentável e eficiente. |
| Melhoria Contínua do Processo   | Análise e Organização  | Análise da Equipe | Análise de Métricas de Fluxo (Lead Time, Cycle Time). Reuniões de Cadência (Revisão de Processo). | Reuniões de Cadência para revisão do processo. Identificação de gargalos e oportunidades de melhoria com base em dados reais. |
|  |  | Organização do Quadro | Ajustes no Quadro e Políticas Explícitas. | Um processo de desenvolvimento que evolui e se torna cada vez mais eficiente ao longo do tempo. |

## Histórico de Versões

<font size="3"><p style="text-align: left">**Tabela 2** - Histórico de versões.</p></font>

| Versão |        Descrição         |                      Autor(es)                      |    Data    |
| :----: | :----------------------: | :-------------------------------------------------: | :--------:  
|  1.0   | Criação do documento | [Felipe Junior](https://github.com/Felipej3ds)          | 19/10/2025 | 