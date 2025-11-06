# "**DoR e DoD:**

### **Definition of Ready (DoR)**

A **Definition of Ready (DoR)** é um conjunto de critérios que um item ou uma *User Story* do backlog deve atender para ser considerado pronto para iniciar o trabalho. Assim que um item do backlog atende a esses critérios, ele pode ser puxado para o fluxo de desenvolvimento Kanban. Para que um item seja considerado **Ready**, ele precisa atender aos seguintes critérios:

**Protótipo Pronto (Design/Wireframe aprovado)**

* Quando a User Story envolve interface ou fluxo visual, deve existir um protótipo no **Figma** com telas e interações principais mapeadas; o protótipo precisa estar aprovado pelo cliente.  
* O protótipo no Figma deve conter notas/anotações claras sobre comportamento esperado (por exemplo: estados vazios, mensagens de erro, limites de paginação).

**Regras de Negócios Claras (O que o sistema deve fazer)**

* As regras de negócio que definem o comportamento esperado do sistema devem estar documentadas de forma objetiva e sem ambiguidade (ex.: fórmula do ROI, tratamento de duplicatas de importação, comportamento ao faltar campo X).

* Exemplos de dependências técnicas externas necessárias para suportar essas regras devem estar listados (ex.: bibliotecas/plataformas previstas  e formatos de arquivo esperados da Bodog).

**Historia de Usuario Prontas**

* A User Story deve seguir o modelo:  
   **“Eu, como \[Ator\], devo ser capaz de \[ação\], para que \[benefício/objetivo\]”**  
  * Exemplo completo: “Eu, como jogador, devo ser capaz de importar múltiplos históricos exportados da Bodog para que o sistema consolide e gere minhas métricas mensais automaticamente.”  
* A história deve conter: descrição, escopo limitado, critérios de aceitação claros e testáveis (passos e resultados esperados), estimativa de esforço e priorização no backlog.  
* Deve caber em uma iteração curta (equivalente a 2–3 semanas no contexto do nosso fluxo Kanban).

  ### **Definition of Done (DoD)**

A **Definition of Done (DoD)** é o conjunto de critérios que uma *User Story* precisa atender para ser considerada concluída e pronta para entrega/validação. Uma User Story é considerada **Done** quando atende a todos os itens abaixo:

**Entrega Valor Funcional (incremento utilizável)**

* A história entrega um incremento que traz valor ao usuário final (feature visível/operacional no produto).

**Documentação Atualizada (técnica e de uso)**

* **Técnica:** documentação mínima atualizada inclui: como executar localmente, dependências (arquivo de requirements/pyproject), endpoints (se houver), esquema de dados relevante, notas sobre migrações/importações e instruções de rollout em ambiente Windows (já que o produto é empacotado como .exe).  
* **De uso:** instruções para o usuário final (passos para usar a funcionalidade, pré-requisitos e exemplos de entrada/saída) atualizadas no manual ou na seção de ajuda.

**Codigo Revisado**

* O código passou por revisão ( code review) e os comentários relevantes foram resolvidos. *(mantivemos o critério “CÓDIGO REVISADO” conforme sua definição: code review — não incluímos descrições genéricas sobre “boas práticas”).*

**Testes TDD Realizadas (Cobertura adequada de testes)**

* Testes escritos em abordagem TDD foram implementados e executados com sucesso, cobrindo as regras de negócio e fluxos principais (importação, consolidação, cálculos).  
* Relatórios de execução dos testes (logs/pipelines) confirmam que os testes passaram.

**Integração Completa (Front e back-end comunicando)**

* A funcionalidade está integrada ponta a ponta: front-end consome corretamente os endpoints do back-end e as interações esperadas foram validadas.

**Critérios de Aceite Atendidos (Funcionalidade validada)**

* Todos os critérios de aceitação definidos na User Story foram validados e atendidos.  
* A funcionalidade foi demonstrada ao cliente/PO; feedbacks críticos foram aplicados ou registradas ações de follow-up com responsáveis e prazos.

**Integração Contínua** 

* A mudança foi integrada ao branch principal sem conflitos e passou pelos pipelines de CI configurados (build \+ testes).

## Histórico de Versões

<font size="3"><p style="text-align: left">**Tabela 1** - Histórico de versões.</p></font>

| Versão |        Descrição         |                      Autor(es)                      |    Data    |
| :----: | :----------------------: | :-------------------------------------------------: | :--------:  
|  1.0   | Criação do documento | [Thales Duarte](https://github.com/Thales-Duarte)         | 18/10/2025 | 