**Especificação de Caso de Uso: Manter Perfil do Paciente** 

**1.1 Breve Descrição**

Este caso de uso permite ao **Paciente** registrar e, posteriormente, atualizar suas informações pessoais e condições de saúde preexistentes na plataforma Connect Care. O objetivo é garantir que o sistema possua dados cadastrais e clínicos atualizados para oferecer um atendimento mais preciso e personalizado.

**1.2 Atores**

O ator principal deste caso de uso é o **Paciente**, que interage com o sistema para gerenciar seu próprio perfil.

**2\. Fluxo de Eventos**

**2.1 Fluxo Principal: Atualizar Perfil**

O Fluxo Principal descreve o caminho mais comum, onde o Paciente, já cadastrado, acessa o sistema para atualizar suas informações.

2.1.1 O Paciente acessa a funcionalidade "Meu Perfil" no sistema.  
2.1.2 O Sistema exibe o formulário de perfil preenchido com os dados atuais do Paciente.  
2.1.3 O Paciente edita os campos desejados (ex: endereço, telefone, condições de saúde preexistentes).  
2.1.4 O Paciente confirma a atualização dos dados.  
2.1.5 O Sistema valida os dados editados, verificando se os campos obrigatórios foram preenchidos e se estão no formato correto**\[FE01\]**(Referência: RN01, RN02).  
2.1.6 O Sistema persiste com as novas informações no banco de dados.  
2.1.7 O Sistema exibe uma mensagem de sucesso: "Perfil atualizado com sucesso."  
2.1.8 O Caso de Uso é encerrado.

**2.2 Fluxos Alternativos (FA)**

**FA01: Registro Inicial do Perfil (Inclusão)**

Este fluxo ocorre quando o Paciente acessa a funcionalidade pela primeira vez e precisa registrar suas informações detalhadas.

2.2.1 O Paciente acessa a funcionalidade "Meu Perfil" e o Sistema detecta que o perfil detalhado está incompleto (Inicia no 2.1.1).  
2.2.2 O Sistema exibe o formulário de perfil com campos vazios ou com dados básicos (nome,idade,sintomas) preenchidos.  
2.2.3 O Paciente preenche todos os campos obrigatórios e opcionais.  
2.2.4 O Paciente confirma o registro.  
2.2.5 O Sistema valida os dados preenchidos**\[FE01\]**(Referência: RN01, RN02).  
2.2.6 O Sistema verifica se o Paciente já possui um registro completo no banco de dados**\[FE02\]**.  
2.2.7 O Sistema persiste as informações no banco de dados.  
2.2.8 O Sistema exibe uma mensagem de sucesso: "Perfil registrado com sucesso." (Retorna ao 2.1.8).

**2.3 Fluxos de Exceção (FE)**

**FE01: Dados Inválidos ou Incompletos**

Ocorre no passo 2.1.5 (Atualização) ou 2.2.5 (Registro).

2.3.1 O Sistema detecta que um campo obrigatório não foi preenchido ou está em formato inválido (viola RN01 ou RN02).  
2.3.2 O Sistema exibe uma mensagem de erro indicando o campo específico e a regra violada (ex: "Nome inválido. Deve conter apenas letras e ter no mínimo 3 caracteres.").  
2.3.3 O Sistema retorna ao passo 2.1.3 (Atualização) ou 2.2.3 (Registro) para que o Paciente corrija os dados.

**FE02: Paciente Já Cadastrado (Apenas no Registro Inicial)**

Ocorre no passo 2.2.6 (Registro Inicial).

2.3.4 O Sistema detecta que o Paciente já possui um perfil detalhado completo no banco de dados.  
2.3.5 O Sistema exibe uma mensagem: "Seu perfil já está completo. Você será redirecionado para a tela de atualização."  
2.3.6 O Sistema redireciona o Paciente para o passo 2.1.2 (Fluxo Principal).

**3\. Requisitos Especiais**

1. **RS01:** O formulário de perfil deve ser responsivo e compatível com dispositivos móveis (smartphones e tablets).

2. **RS02:** O sistema deve garantir a criptografia dos dados de saúde preexistentes (condições clínicas) armazenados.

**4\. Regras de Negócio (RN)**

3. **RN01:** O campo **Nome Completo** deve conter apenas caracteres alfabéticos e espaços, e deve ter no mínimo 3 caracteres.

4. **RN02:** O campo **Data de Nascimento** deve ser uma data válida e o Paciente deve ter idade maior ou igual a 0 (zero) anos.

5. **RN03:** O campo **Condições de Saúde Preexistentes** é opcional e permite texto livre para descrição de sintomas ou condições médicas passadas.

**5\. Precondições**

6. **PC01:** O Paciente deve estar autenticado no sistema Connect Care.

7. **PC02:** O sistema deve estar conectado ao banco de dados para leitura e escrita.

**6\. Pós-condições**

8. **PS01:** As informações do perfil do Paciente (pessoais e de saúde) estarão atualizadas no banco de dados.

9. **PS02:** Um log de auditoria deve ser gerado registrando a data, hora e o Paciente que realizou a alteração.

**7\. Pontos de Extensão**

10. **PE01:** No passo 2.1.6 (Persistência), este caso de uso pode ser estendido por "Notificar Equipe de Saúde" (para alertar sobre uma nova condição de saúde preexistente).

11. **PE02:** No passo 2.1.2 (Exibição do formulário), este caso de uso pode ser estendido por "Consultar Histórico de Alterações" (para o Paciente visualizar mudanças anteriores).