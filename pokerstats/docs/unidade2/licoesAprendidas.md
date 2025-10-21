cat << 'EOF' > Licoes_Aprendidas_Unidade2.md
# Lições Aprendidas – Unidade 2

## Definição do Nível de Abstração dos Requisitos
**Desafio:**  
No início da definição dos requisitos, a equipe teve dificuldade em determinar o nível de detalhe ideal para cada tipo de requisito (de usuário e de sistema). Alguns eram genéricos demais, semelhantes a épicos, enquanto outros estavam excessivamente detalhados logo de início, dificultando a adaptação às mudanças.

**Ação de Melhoria:**  
Aprendemos a importância do *refinamento progressivo* e da adaptação do nível de granularidade conforme o avanço do projeto. Passamos a iniciar com **épicos e features** derivados das características da solução e a detalhar **histórias de usuário menores** apenas quando próximas da implementação, adotando a abordagem *just-in-time*. Isso tornou o backlog mais flexível e reduziu o retrabalho.

---

## Garantia da Qualidade dos Requisitos e do Backlog
**Desafio:**  
As primeiras histórias de usuário apresentavam ambiguidades e falta de testabilidade, dificultando estimativas e a validação de valor para o cliente.

**Ação de Melhoria:**  
Adotamos os frameworks **INVEST** (Independent, Negotiable, Valuable, Estimable, Small, Testable) para garantir a qualidade das histórias e **DEEP** (Detailed Appropriately, Estimated, Emergent, Prioritized) para manter um backlog saudável.  
Implementamos formalmente o **Definition of Ready (DoR)** e o **Definition of Done (DoD)** como checkpoints obrigatórios para garantir que cada requisito estivesse completo antes de entrar no fluxo e realmente pronto ao ser entregue.

---

## Consistência na Declaração e Representação dos Requisitos
**Desafio:**  
No início, o formato das declarações era inconsistente — havia mistura entre frases funcionais (“O sistema deve…”) e histórias de usuário — o que prejudicava a comunicação interna e com o cliente. Além disso, havia incerteza sobre como representar requisitos de forma mais visual e compreensível.

**Ação de Melhoria:**  
Definimos o formato **“Como [papel], quero [atividade], para que [valor]”** como padrão oficial para as histórias de usuário, complementado por **protótipos e diagramas UML** quando necessário. Essa padronização melhorou a clareza, a rastreabilidade e o alinhamento entre equipe e cliente durante as discussões e validações.

---

## Gerenciamento Dinâmico do Backlog (Organização e Atualização)
**Desafio:**  
Inicialmente, o backlog era tratado como uma lista estática, sem revisões ou ajustes contínuos. Isso gerava desalinhamento entre prioridades e capacidade real da equipe.

**Ação de Melhoria:**  
Passamos a encarar o backlog como um **artefato vivo**, sujeito a evolução constante. Instituímos **sessões de refinamento regulares (backlog grooming)** para revisar, estimar e repriorizar itens conforme valor de negócio, risco e dependências.  
Também passamos a priorizar usando **MoSCoW**, considerando **valor, esforço e risco**, o que aumentou a previsibilidade e eficiência do fluxo.

---

## Seleção e Combinação de Técnicas de Engenharia de Requisitos
**Desafio:**  
Com a grande variedade de técnicas possíveis (entrevistas, brainstorming, prototipagem, checklists, etc.), houve dificuldade inicial em definir quais aplicar em cada momento do ciclo.

**Ação de Melhoria:**  
A equipe aprendeu a combinar técnicas conforme o objetivo de cada fase:  
- **Elicitação:** Entrevistas e brainstorming;  
- **Análise e Consenso:** Negociação e análise de custo/benefício;  
- **Declaração e Representação:** Prototipagem e diagramas UML;  
- **Verificação e Validação:** Checklists e revisões de código;  
- **Organização:** Priorização MoSCoW e Story Points.  

Esse aprendizado formou um **“toolbox de Engenharia de Requisitos”** próprio da equipe, fortalecendo o processo de desenvolvimento e melhorando a qualidade das entregas.

---

**Resumo Geral da Unidade 2:**  
Durante esta unidade, a equipe amadureceu na aplicação prática das técnicas de Engenharia de Requisitos dentro do processo **Kanban + Práticas XP**.  
Passamos a compreender o backlog como um sistema vivo, aprendemos a equilibrar detalhe e flexibilidade, e incorporamos práticas de qualidade (DoR, DoD, INVEST, DEEP) que elevaram o nível de organização e previsibilidade do projeto *Poker Stats*.

