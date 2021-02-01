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

Caso você não tenha o MongoDB instalado na sua máquina, suba um container rodando `docker-compose up -d`.

Assim que as dependências estiverem instaladas na máquina, rode o comando `python -m api` para inicializar o servidor.

Por padrão, o servidor vai rodar na rota `http://0.0.0.0:8000/`.

Rotas e requisições estão no arquivo `postman.json`.

## Documentação 

- Swagger: `http://0.0.0.0:8000/docs`
- Redoc: `http://0.0.0.0:8000/redoc`


## Testes

Para testar o projeto, execute o comando `python -m pytest`, a dependência pytest já vem instalada por padrão.

![alt text](https://github.com/leoalvs/backend-test/blob/main/tests.png?raw=true)

## Maiores desafios

- Gerenciamento de tempo.
- Estudo dos componentes nunca utilizados.
- Fork do buslane.

## Plano de melhorias

- Criar filtros dinamicos no repositório.
- Incluir IoC para aumentar desacoplamento do código.
- Criar modelo de retorno de erros da api.
- Aumentar cobertura de testes e adicionar testes de falha.
- Terminar de dockerizar.
- Adicionar logs.

## Links úteis

- [FastApi](https://fastapi.tiangolo.com/) - Documentação oficial
- [Benchmark](https://ahmed-nafies.medium.com/why-did-we-choose-fast-api-over-flask-and-django-for-our-restful-micro-services-77589534c036) - Comparação do FastApi com outros frameworks
- [Awesome README.md](https://github.com/matiassingers/awesome-readme) - Awesome READMEs
