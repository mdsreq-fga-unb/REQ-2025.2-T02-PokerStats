# Guia de Contribuição

## Versionamento

| **Versão** | **Data** | **Modificação** | **Responsável** |
| :-: | :-: | :-: | :-: |
| 0.1 | 16/10/25 | Criação adaptada para Poker Stats | Poker Stats Team |

*Tabela 1: Versionamento*

---

## Objetivo

Este guia define padrões e critérios para colaboração no projeto Poker Stats, promovendo organização, rastreabilidade e um fluxo de desenvolvimento mais eficiente e seguro para todos os participantes.

## Políticas

### Issues

A criação de issues do projeto será realizada via **GitHub Projects**. Recomenda-se criar issues claras e atômicas para cada atividade, seguindo os princípios:

- Cada issue deve ter objetivo único. Para atividades de maior escopo, utilize épicos.
- Associe pelo menos um responsável (assignee) à issue.
- Titule de forma simples, descritiva e concisa.
  - Para atividades mais complexas, detalhe nos comentários.
- Atribua labels e milestone quando aplicável.
- Recomenda-se comentar na issue durante o andamento, registrando evolução, dúvidas ou dificuldades.



*Tabela 2: Critérios de Pontuação do Planning Poker*

### User Stories

Adote o template abaixo para descrever histórias de usuário no GitHub Projects:

```
<!---USXX - Descrição da US-->
 
## **Descrição**
 
"Eu, como [PAPEL DE USUÁRIO], desejo [REALIZAR ALGO COM O SISTEMA] para que [OBJETIVO FINAL DA HISTÓRIA]"
 
## **Critérios de Aceitação:**
 
- [] **Critério de Aceitação 01**: <descrever critério>;
- [] **Critério de Aceitação N**: <descrever critério>;
 
## **Tarefas:**
 
- [] **Tarefa 01:** <descrever tarefa>;
- [] **Tarefa N:** <descrever tarefa>;
 
## **Protótipo:**
 
<!--- Imagens das telas relacionadas à história -->

O protótipo pode ser encontrado em: <link_para_o_protótipo>
```

### BUGs

Use o template a seguir para relatar bugs no GitHub Issues/Projects:

```
<!---[BUG] - Título Descritivo do BUG-->

## **Descrição**

Descrição resumida do bug.

## **Como Reproduzir?**

Passos ou prints para reproduzir o erro.

## **Demais Informações**

Informações extras úteis ou sugestões de correção.
```

### ENHANCEMENTs

Use o template abaixo para melhorias/otimizações:

```
<!---[ENHANCEMENT] - Título Descritivo da Melhoria-->

## **Descrição**

O que será melhorado, como e objetivo final.

## **Demais Informações**

Detalhes complementares, se necessário.
```

### Branching

O fluxo de branching do Poker Stats segue um modelo inspirado no GitFlow, com pequenas adaptações:

| **Branch** | **Objetivo** | **Nomenclatura da Branch** |
| :-: | :-: | :-: |
| main | Versão estável, pronta para produção.  | main |
| qa | Código testado/pronto para homologação. | qa |
| dev | Desenvolvimento ativo (pode ser instável). | dev |
| feat | Implementar novas funcionalidades. | feat#id-issue/nome |
| fix | Correções pontuais/bugs. | fix#id-issue/nome |
| doc | Atualizações de documentação. | doc#id-issue/nome |

*Tabela 3: Detalhamento das branches*

### Commiting

Siga o padrão *Conventional Commits*. Exemplo de mensagem:

```
<tipo>(#id-issue): breve descrição

[Comentários, se necessário]
[Co-autores, caso existam]
Co-authored-by: handle_coautor <email@dominio.com>
```

Principais tipos de commit:

| **Tipo** | **Objetivo** |
| :-: | :-: |
| feat | Adiciona funcionalidade |
| fix | Corrige problema |
| docs | Atualiza documentação |
| chore | Atividade rotineira |
| style | Ajusta configuração/estética |
| ref | Refatora código |
| test | Cria ou ajusta teste |
| ci | Relacionado a integração contínua |

*Tabela 4: Tipos de commit*

Recomendações:
- Título dos commits deve ser objetivo e autoexplicativo.
- Commits devem ser atômicos (apenas uma alteração/finalidade).

### Pull Requests

Todos os pull requests devem ser revisados por outro membro e seguir o modelo:

Título:
```md
[TIPO] Título (relacionado à Issue #id)
```

Descrição:
```md
# Descrição
Breve resenha do PR e relação com a issue.
```

Checklist:
```md
# Checklist
- [x] Segue o guia de contribuição
- [x] Testado e revisado por outro membro
- [x] Identação e documentação adequadas
- [x] Tabela de versionamento incluída em documentos
```

## Referências
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Git branching strategy diagrams](https://brntn.me/blog/git-branching-strategy-diagrams/)
- [GitHub pull request template](https://axolo.co/blog/p/part-3-github-pull-request-template)
- **COHN, Mike**. **User Stories Applied**: for agile software development. Boston: Addison-Wesley Professional, 2004.
