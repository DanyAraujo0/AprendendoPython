# API de Produtos

Este projeto consiste em uma API RESTful para gerenciamento de produtos, desenvolvida em Python. A API permite realizar operações de CRUD (Create, Read, Update, Delete) para produtos, utilizando MongoDB como banco de dados.

## Funcionalidades

- **Criação de Produtos**: Adicionar novos produtos ao banco de dados.
- **Leitura de Produtos**: Consultar uma lista com todos os produtos cadastrados ou usando o filtro de preço min e max.
- **Atualização de Produtos**: Modificar as informações de um produto existente.
- **Exclusão de Produtos**: Remover um produto do banco de dados.
- **Tratamento de Exceções para cada funcionalidade**: Exibir mensagens de erro amigavéis ao usúario se error.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal para o desenvolvimento da API.
- **MongoDB**: Banco de dados NoSQL utilizado para armazenar os dados dos produtos.
- **FastAPI**: Framework utilizado.
- **Pytest**: Biblioteca de testes utilizado para garantir a qualidade e o correto funcionamento dos endpoints da API.

## Testes

Os testes da API foram desenvolvidos com o **Pytest**. Eles cobrem todas as funcionalidades de CRUD, garantindo que cada endpoint se comporte como esperado. Os testes incluem:

- **Testes de Criação**: Verificação da criação de novos produtos com dados válidos e inválidos.
- **Testes de Leitura**: Verificação da consulta de produtos existentes e tratamento de casos de produtos não encontrados.
- **Testes de Atualização**: Verificação da modificação de produtos e validação dos dados de entrada.
- **Testes de Exclusão**: Verificação da remoção de produtos e confirmação de que o produto não existe mais.
