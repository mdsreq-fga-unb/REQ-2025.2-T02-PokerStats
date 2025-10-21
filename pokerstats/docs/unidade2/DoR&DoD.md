# 8. Definition of Ready (DoR) e Definition of Done (DoD)

## 8.1 Definition of Ready (DoR)

O **DoR (Definition of Ready)** é um acordo da equipe que define quando um requisito está preparado para ser puxado para o desenvolvimento.  
Garante que a equipe tenha as informações necessárias antes de iniciar.

Um requisito está **"Ready"** quando:

- **Informação Necessária:**  
  A História de Usuário está clara, o valor de negócio é compreendido e os detalhes são suficientes para o desenvolvimento.

- **Critérios de Aceitação Definidos:**  
  Os Critérios de Aceitação existem, estão claros, são testáveis e foram discutidos pela equipe e cliente.

- **Granularidade Adequada:**  
  O requisito é pequeno o suficiente para ser concluído dentro do fluxo Kanban (não é um Épico).

- **Interface Mapeada (se aplicável):**  
  Protótipos ou wireframes existem e foram alinhados.

- **Dependências Conhecidas:**  
  Dependências técnicas (ex: bibliotecas específicas) ou de outros requisitos foram identificadas.

---

## 8.2 Definition of Done (DoD)

O **DoD (Definition of Done)** é o acordo da equipe que demonstra a qualidade do trabalho realizado,  
definindo quando uma funcionalidade está realmente completa.

Um requisito está **"Done"** quando:

- **Entrega Incremento de Produto:**  
  A funcionalidade agrega valor utilizável ao produto.

- **Critérios de Aceitação Atendidos:**  
  Todos os Critérios de Aceitação definidos foram cumpridos e validados.

- **Código Aderente aos Padrões:**  
  O código segue os padrões de codificação da equipe.

- **Testes Automatizados Passando:**  
  Os testes unitários e de integração relevantes foram implementados e estão passando com sucesso (seguindo a abordagem TDD).

- **Código Revisado:**  
  O código foi revisado por outro membro da equipe (revisão assíncrona, ex: Pull Request) e os feedbacks aplicados.

- **Integração Contínua (CI) OK:**  
  O código foi integrado à base principal e a build automatizada (incluindo testes) passou com sucesso.

- **Documentação Atualizada:**  
  A documentação mínima necessária (técnica ou de uso) está atualizada.

- **Validação do Cliente Realizada:**  
  A funcionalidade foi demonstrada ao cliente (Eduardo) e aceita.
