# ESPECIFICAÇÃO DE CASO DE USO

## 1. Nome do Caso de Uso Gerenciar Campanha

### 1.1 Breve Descrição:

- Este caso de uso permite que a Organização Parceira cadastre, altere, exclua e visualize iniciativas de saúde (como campanhas de vacinação, mutirões ou palestras). O objetivo é definir os detalhes da ação e o público-alvo para que o sistema possa, posteriormente, divulgar a campanha para os pacientes elegíveis na comunidade
### 1.2 Atores

- Ator Principal: Organização Parceira (ONGs, hospitais, instituições governamentais).
- Atores Secundários: Não se aplica


## 2. Fluxo de Eventos

### 2.1 Fluxo Principal 
 2.1.1. A Organização Parceira acessa a área de gestão de campanhas no sistema. 
 2.1.2. O Sistema exibe a lista de campanhas ativas e o histórico de ações anteriores. 
 2.1.3. A Organização Parceira seleciona a opção "Criar Nova Campanha". 
 2.1.4. O Sistema solicita os dados da campanha: Título, Descrição, Tipo de Ação (ex: vacinação, exame), Localização, Data/Hora e Duração.
2.1.5. O Sistema solicita a definição do público-alvo (critérios de segmentação: faixa etária, localização geográfica, condições de saúde).
2.1.6. A Organização Parceira insere as informações (Ex: "Exames oftalmológicos para maiores de 40 anos"). 
2.1.7. A Organização Parceira confirma o cadastro. 
2.1.8. O Sistema valida se os critérios de segmentação e dados obrigatórios estão preenchidos (referência [RN01]). 
2.1.9. O Sistema registra a campanha e agenda a divulgação automática para os usuários relevantes. 
2.1.10. O caso de uso termina.

### 2.2 Fluxos Alternativos

[FA01] Alterar Campanha
    Origem: Passo 2.1.2.
    Descrição: A Organização seleciona uma campanha existente e escolhe "Editar". O Sistema carrega os dados atuais. O Ator modifica as informações (como data ou local) e confirma.
    Retorno: O sistema valida e atualiza o registro, retornando ao passo 2.1.2.
[FA02] Cancelar/Excluir Campanha
    Origem: Passo 2.1.2.
    Descrição: A Organização seleciona uma campanha e escolhe "Excluir". O sistema solicita confirmação e verifica se a campanha já ocorreu.
    Retorno: O sistema remove a campanha da lista de divulgação e encerra o caso de uso.


### 2.3 Fluxos de Exceção

[FE01] Dados Incompletos
    Disparo: Passo 2.1.8 (Validação).
    Ação: O Sistema identifica que campos obrigatórios (como Local ou Data) estão vazios. Exibe mensagem de erro "Campos obrigatórios não preenchidos" e mantém os dados na tela para correção.
[FE02] Critérios de Segmentação Inválidos
    Disparo: Passo 2.1.8 (Validação).
    Ação: O Sistema identifica que os critérios de público-alvo são conflitantes ou inexistentes (ex: idade negativa). Exibe alerta e solicita revisão dos filtros.


## 3. Requisitos Especiais

- O sistema deve permitir a geolocalização do local da campanha para facilitar o acesso dos pacientes via mapa.
- A interface de segmentação deve permitir filtros combinados (ex: "Mulheres" + "Acima de 40 anos" + "Região Vila Esperança").


## 4. Regras de Negócio

[RN01] Validação de Data: A data de início da campanha deve ser sempre posterior à data atual (futuro).
[RN02] Segmentação de Público: A campanha só será visível para usuários que atendam aos critérios de faixa etária, localização e condições de saúde definidos no cadastro.


## 5. Precondições

- A Organização Parceira deve estar autenticada no sistema.
- A Organização deve ter seu perfil validado pelo Administrador.


## 6. Pós-condições

- A campanha é persistida no banco de dados.
- O sistema dispara o processo de notificação para os usuários que se enquadram no perfil definido (caso de uso relacionado à divulgação).


## 7. Pontos de Extensão

Não se aplica (baseado no diagrama fornecido, este UC não possui extends ou includes conectados a ele diretamente).


