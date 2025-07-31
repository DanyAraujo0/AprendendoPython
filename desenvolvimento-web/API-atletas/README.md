# API de Atletas com FastAPI

Este projeto é uma API RESTful robusta para o gerenciamento de atletas, desenvolvida com Python e o framework **FastAPI**. A aplicação utiliza **PostgreSQL** como banco de dados para garantir a integridade e a persistência dos dados e foi testada utilizando o **Postman** para as requisições HTTP.

Este projeto representa uma evolução na complexidade em relação a APIs mais simples, incorporando uma arquitetura mais estruturada e ferramentas modernas do ecossistema Python.

## Principais Funcionalidades

-   **CRUD de Atletas**: Operações completas para Criar, Ler, Atualizar e Deletar atletas.
-   **Estrutura de Dados**: Modelagem de dados com informações detalhadas dos atletas (nome, CPF, idade, centro de treinamento, categoria, etc.).
-   **Consultas e Filtros**: Possibilidade de consultar atletas com base em diversos parâmetros.
-   **Validação de Dados**: Validação automática das requisições e dados de entrada graças ao Pydantic, integrado ao FastAPI.
- **Tratamento de Exceções para cada funcionalidade**: Exibir mensagens de erro amigavéis ao usúario se error.
-   **Documentação Automática**: Geração de documentação interativa da API (Swagger UI e ReDoc) de forma automática pelo FastAPI.

## Tecnologias Utilizadas

Todas as ferramentas e a versão utilizada estão listadas em [Requiriments](requirements.txt/)

-   **Python**: Linguagem de programação base do projeto.
-   **FastAPI**: Framework web de alta performance para a construção da API.
-   **PostgreSQL**: Banco de dados relacional para armazenamento dos dados dos atletas.
-   **Pydantic**: Para validação e serialização de dados.
-   **SQLAlchemy**: ORM (Object-Relational Mapper) para a interação com o banco de dados PostgreSQL.
-   **Uvicorn**: Servidor ASGI para executar a aplicação FastAPI.