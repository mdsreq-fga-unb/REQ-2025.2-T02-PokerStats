# ESPECIFICAÇÃO DE CASO DE USO

## 1. Nome do Caso de Uso Gerenciar Campanha

### 1.1 Breve Descrição:

- Permite que a organização parceira cadastre, edite ou remova iniciativas de saúde (como vacinação, mutirões ou ações educativas) na plataforma. O objetivo é registrar os detalhes da ação e definir o público-alvo para que o sistema possa divulgar a campanha para os pacientes adequados.

### 1.2 Atores

- Ator Principal: Organização Parceira (ONGs, hospitais, instituições governamentais).
- Atores Secundários: Não aplicável (o sistema processa internamente).


## 2. Fluxo de Eventos

### 2.1 Fluxo Principal 
2.1.1. A Organização Parceira seleciona a opção de gerenciar campanhas no menu principal. 
2.1.2. O Sistema exibe a lista de campanhas já cadastradas pela organização e a opção de "Nova Campanha".
2.1.3. A Organização Parceira seleciona a opção "Nova Campanha".
2.1.4. O Sistema apresenta o formulário de cadastro solicitando: título, descrição, tipo de ação, local, data/hora e critérios de segmentação (faixa etária, localização, condições de saúde).
2.1.5. A Organização Parceira preenche as informações da campanha (ex: Mutirão de Oftalmologia para maiores de 40 anos). 
2.1.6. A Organização Parceira solicita a confirmação do cadastro. 
2.1.7. O Sistema valida os dados inseridos.
 2.1.8. O Sistema registra a campanha no banco de dados. 
2.1.9. O Sistema exibe uma mensagem de sucesso confirmando que a campanha foi criada e está pronta para divulgação.

### 2.2 Fluxos Alternativos

[FA01] Editar Campanha Existente
    Origem: Passo 2.1.2.
    Descrição: A Organização Parceira seleciona uma campanha existente na lista e escolhe a opção "Editar". O Sistema carrega os dados atuais (passo 2.1.4). A Organização altera as informações necessárias.
    Retorno: O fluxo retorna ao passo 2.1.6 (Solicitar confirmação).
[FA02] Excluir Campanha
    Origem: Passo 2.1.2.
    Descrição: A Organização Parceira seleciona uma campanha e escolhe a opção "Excluir". O Sistema solicita uma confirmação de segurança. A Organização confirma a exclusão. O Sistema remove a campanha e atualiza a lista.
    Retorno: O caso de uso encerra


### 2.3 Fluxos de Exceção

[FE01] Dados Obrigatórios Incompletos
    Disparo: Passo 2.1.7 (Validação).
    Descrição: O Sistema identifica que campos obrigatórios (como Local ou Data) não foram preenchidos.
    Ação do Sistema: O Sistema exibe uma mensagem de alerta indicando quais campos faltam e mantém os dados já preenchidos para correção.
[FE02] Data Inválida
    Disparo: Passo 2.1.7 (Validação).
    Descrição: O Sistema identifica que a data informada para a campanha é anterior à data atual (passado).
    Ação do Sistema: O Sistema informa que a campanha deve ser agendada para uma data futura e solicita a correção.