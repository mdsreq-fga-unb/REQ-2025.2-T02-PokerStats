# REQ-2025.2-T02-PokerStats
Repositório de projeto da disciplina de REQ-T2 - 2025.2.

## Configuração do Ambiente de Desenvolvimento

### Pré-requisitos

  - [Python 3.8+](https://www.python.org/downloads/)
  - [Git](https://git-scm.com/downloads)

### Instalação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/poker-stats.git
    cd poker-stats
    ```

2.  **Crie o ambiente virtual e instale as dependências:**

      - **Windows:**

        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        pip install -r requirements.txt
        ```

      - **Linux:**

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        ```

## Gerenciando Dependências

Ao adicionar uma nova biblioteca ao projeto, mantenha o arquivo `requirements.txt` atualizado. Para isso, estando no diretório raiz, execute os seguintes passos:

1.  **Instale a nova biblioteca:**

    ```bash
    pip install nome-da-biblioteca
    ```

2.  **Atualize o arquivo `requirements.txt`:**

    ```bash
    pip freeze > requirements.txt
    ```

## Estrutura do Projeto e Onde Codificar

Para manter a organização, cada nova funcionalidade deve ser criada na pasta correspondente à sua responsabilidade:

```
poker-stats/
|
├── main.py              # Ponto de entrada da aplicação. Inicia a GUI.
|
└── src/poker_stats/     # Código fonte principal
    ├── ui/              # Camada de Apresentação: Código da interface gráfica
    ├── core/            # Camada de Negócio: Lógica, regras de negócio e cálculos de métricas.
    └── database/        # Camada de Dados: Módulos para interagir com o banco de dados SQLite.
```

## Como Executar a Aplicação

1.  Certifique-se de que seu ambiente virtual (`venv`) está ativado.
2.  Execute o arquivo principal:
    ```bash
    python main.py
    ```

Com certeza. Aqui está a nova seção para o `README.md` que explica o papel de cada biblioteca principal no projeto.

## Principais Bibliotecas e Suas Funções

Cada biblioteca foi escolhida para cumprir uma responsabilidade específica dentro da arquitetura do projeto.

-   **`CustomTkinter` (Interface Gráfica - Camada `ui`)**
    -   É a biblioteca responsável por construir toda a interface visual da aplicação.

-   **`Pandas` (Lógica de Negócio - Camada `core`)**
    -   Será usado para ler os arquivos de histórico (`.csv`, `.txt`), limpar e tratar os dados, e realizar todos os cálculos de métricas (Lucro, ROI, ITM, etc.).

-   **`Matplotlib` (Visualização de Dados - Camada `ui`)**
    -   Será utilizada para gerar os gráficos e visualizações de dados. Integra-se diretamente com os dados processados pelo Pandas.

-   **`SQLAlchemy` (Acesso a Dados - Camada `database`)**
    -   Ferramenta para interagir com o banco de dados SQLite de forma segura e organizada. Ela traduz código Python em comandos SQL, tornando a tarefa de salvar e consultar dados mais legível e menos propensa a erros.

-   **`PyInstaller` (Empacotamento e Distribuição)**
    -  Biblioteca para transformar todo o código Python e suas dependências em um único arquivo executável (`.exe`).