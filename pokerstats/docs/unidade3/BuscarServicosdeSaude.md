# ESPECIFICAÇÃO DE CASOS DE USO Buscar Serviços de Saúde 
 
## 1. Nome do Caso de Uso 

- Buscar Serviços de Saúde 

### 1.1 Breve Descrição 

- Permite ao paciente localizar clínicas, hospitais e unidades de saúde próximas. O sistema utiliza 
algoritmos para oferecer sugestões personalizadas com base no perfil e sintomas do usuário , 
facilitando o acesso mesmo em áreas com infraestrutura limitada.


### 1.2 Atores 
- Ator Principal: Paciente. 
- Atores Secundários: Não se aplica.


## 2. Fluxo de Eventos 

### 2.1 Fluxo Principal 
1. O Paciente seleciona a opção de buscar serviços de saúde no menu. 
2. O Sistema recupera os dados do perfil do paciente (idade e histórico). (RN01) 
3. O Paciente insere os sintomas observados ou critérios de busca. 
4. O Sistema valida a captura da localização geográfica atual do paciente. (FE01) 
5. O Sistema aplica o algoritmo de recomendação cruzando perfil, sintomas e localização. 
(RN01) 
6. O Sistema filtra os resultados priorizando a proximidade geográfica. (RN03) 
7. O Sistema apresenta a lista de unidades de saúde encontradas. (FA02) 
8. O Paciente seleciona uma unidade específica da lista. 
9. O Sistema exibe os detalhes de funcionamento da unidade selecionada. 
10. O Sistema processa o mapa simplificado de acesso ao local. (RN02) 
11. O Sistema disponibiliza a visualização do mapa (permitindo cache offline). (FA01) 
12. O caso de uso encerra.

### 2.2 Fluxos Alternativos 

- [FA01] Acesso Offline ao Mapa 
Origem: Este fluxo se inicia no Passo 11 do Fluxo Principal. 
Condição: Se o sistema detectar que o dispositivo do paciente está sem conexão com a 
internet. 
Ação: O Sistema recupera os dados armazenados em cache e exibe o mapa simplificado da 
unidade, garantindo a orientação do paciente mesmo desconectado. 
Retorno: O fluxo retorna para o Passo 12 do Fluxo Principal (Encerramento do caso de 
uso). 

- [FA02] Nenhum serviço encontrado 
Origem: Este fluxo se inicia no Passo 7 do Fluxo Principal. 
Condição: Se o algoritmo de busca não encontrar nenhuma unidade de saúde compatível 
com os critérios e sintomas informados. 
Ação: O Sistema exibe uma mensagem informando a ausência de resultados e sugere que o 
paciente amplie o raio de busca ou modifique os filtros de sintomas. 
Retorno: O fluxo retorna para o Passo 3 do Fluxo Principal, permitindo que o paciente 
insira novos critérios de busca.

### 2.3 Fluxos de Exceção

- [FE01] Falha na Geolocalização 
    Origem: Este fluxo ocorre no Passo 4 do Fluxo Principal. 
    Condição: Se o sistema não conseguir obter as coordenadas de GPS do dispositivo (por falha de hardware ou falta de permissão). 
    Ação: 
        1. O Sistema exibe uma mensagem de erro informando a impossibilidade de 
        localizar o dispositivo automaticamente. 
        2. O Sistema solicita que o paciente digite o endereço ou bairro manualmente. 
        3. O Paciente insere a localização desejada. 
    Retorno: O fluxo retorna para o Passo 5 do Fluxo Principal, onde o sistema utilizará o endereço inserido manualmente para processar o algoritmo de recomendação. 

## 3. Requisitos Especiais 

- Compatibilidade com Dispositivos Simples: A funcionalidade deve operar em 
smartphones de entrada. 
- Conectividade Limitada: O sistema deve suportar operações com internet instável.


## 4. Regras de Negócio 

- [RN01] Sugestão Inteligente: O sistema deve cruzar dados de idade/perfil com 
sintomas para sugerir a especialidade correta (ex: pediatria). 
- [RN02] Mapa Simplificado: O sistema deve gerar mapas otimizados para fácil leitura 
em dispositivos simples. 
- [RN03] Prioridade de Proximidade: O algoritmo deve priorizar unidades 
geograficamente mais próximas.

## 5. Precondições 

- O Paciente deve ter realizado o cadastro prévio e estar logado 

## 6. Pós-condições 

- Resultados de Busca Apresentados: O Paciente recebeu a lista de unidades e o mapa 
simplificado correspondente à sua busca. 
- Dados de Analytics Registados: Os critérios da busca (sintomas, região e tipo de 
demanda) foram registrados anonimamente pelo sistema para a geração futura de 
relatórios de impacto social e epidemiológico (conforme objetivo de monitorar doenças 
recorrentes). 
- Cache de Mapa Atualizado: O mapa simplificado e as instruções de acesso da unidade 
selecionada foram armazenados na

## 7. Pontos de Extensão

- Caso de Uso de Extensão: Visualizar Campanhas Móveis. 
- Localização: Passo 7 do Fluxo Principal. 
- Condição: Se o paciente estiver em área sem unidades fixas ou indicar falta de 
transporte.
