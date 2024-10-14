# Projeto Django MVT

Este repositório contém um projeto Django estruturado utilizando a arquitetura MVT (Model-View-Template). Siga as instruções abaixo para configurar o ambiente e rodar o projeto localmente.

## Pré-requisitos

Certifique-se de que os seguintes programas estejam instalados em sua máquina:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Instruções de instalação

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/henriquepontees/piolin.git
    cd piolin
    ```
    **Criando ambiente virtual**:

    ```bash
    python -m venv venv
    venv\Scripts\activate

2. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

## Configuração do banco de dados

1. **Aplique as migrações** para criar as tabelas do banco de dados:

    ```bash
    python manage.py migrate
    ```

2. **Crie um superusuário** para acessar o painel administrativo:

    ```bash
    python manage.py createsuperuser
    ```

    Siga as instruções no terminal para definir um nome de usuário, e-mail e senha.

## Executando o servidor

Inicie o servidor de desenvolvimento Django:

```bash
python manage.py runserver
