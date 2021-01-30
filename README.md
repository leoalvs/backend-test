Desafio Back-end Nodis
============
![Coverage](https://img.shields.io/badge/coverage-75%25-green.svg)

Repositório do desafio back-end proposto pelo time de engenharia da Nodis Tecnologia.


## Stack usada
- Python
- FastAPI
- MongoDB

## Setup

Clone esse repositório, crie um novo `venv` e ative-o.

Instale as dependências com `pip install -r requirements`

## Inicializando o servidor

Assim que as dependências estiverem instaladas na máquina, rode o comando `python -m api` para inicializar o servidor.

Por padrão, o servidor vai rodar na rota `http://0.0.0.0:8000/`.

## Documentação 

- Swagger: `http://0.0.0.0:8000/docs`
- Redoc: `http://0.0.0.0:8000/redoc`

## Testes

Para testar o projeto, execute o comando `python -m pytest`, a dependência pytest já vem instlada por padrão.

![alt text](https://github.com/leoalvs/backend-test/blob/main/tests.png?raw=true)

## Plano de melhorias

Criar filtros dinamicos no repositório
Incluir IoC para aumentar desacoplamento do código
Padronizar retorno de erros da api
Adicionar testes de falha
Terminar de dockerizar
Adicionar logs