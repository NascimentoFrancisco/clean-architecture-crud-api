# CLEAN ARCHITECTURE CRUD API

Este projeto refere-se a CRUD simples sendo uma API REST construída em Python usando o framework Flask para a criação dos endpoints. No entanto, a regra de negócio é completamente independente do framework, pois neste projeto foram implementadas regras da **Clean Architecture** *(Arquitetura Limpa)* estabelecidas por [Robert Cecil Martin](https://pt.wikipedia.org/wiki/Robert_Cecil_Martin).

Para este projeto foram utilizadas algumas bibliotecas interessantes, tanto para a construção da aplicação quanto para a estilização do código. Abaixo estão as bibliotecas mais relevantes:

* pylint
* pytest
* pre-commit
* black
* flake8
* SQLAlchemy

## Guia de uso

### Com docker compose

Caso queira usar este projeto por meio do doker, faça alterações necesárias:
> No arquivo `.env`:
~~~
HOST=db # Aqui deve ser db, pois é o mesmo bome dado lá no docker-compose.yml
USER_DATABASE= Your database user
PASSWORD= Your database password
PORT= Your database port
DATABASE= Your name database
JWT_SECRET_KEY= Your JWT_SECRET_KEY
REDIS_HOST= #Aqui substitua localhost por redis, ficando redis://redis:your port
~~~

## Sem docker
Antes de continuar, é relevante informar que este repositório utiliza um banco de dados MySQL, mas é possível utilizar qualquer outro banco relacional, bastando realizar as configurações de conexão necessárias na infraestrutura do projeto. Para configurar essas conexões, recomenda-se consultar a documentação do [SQLAlchemy](https://docs.sqlalchemy.org/en/20/dialects/) para identificar as práticas corretas.

Após clonar o projeto, certifique-se de ter um virtualenv em sua máquina para assim instalar as dependências desta aplicação:

> Instalação de dependências:
~~~
pip3 install -r requirements.txt
~~~

> Configure de variáveis de ambiente `.env` baseando-se no .env_exemple:
~~~ bash
HOST= Your database host
USER_DATABASE= Your database user
PASSWORD= Your database password
PORT= Your database port
DATABASE= Your name database
JWT_SECRET_KEY= Your JWT_SECRET_KEY
REDIS_HOST= Your redis hosts
~~~

> Abra o seu gerenciador de banco de dados e crie o bnco de dados com o seguinte comando SQL:
~~~ SQL
CREATE DATABASE IF NOT EXISTS user_database;
~~~
Logo em seguida crie a tabela:
~~~ SQL
CREATE TABLE IF NOT EXISTS `user_database`.`users` (
    id VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    primary key (id)
);
~~~
> Execute o redis em sa máquina:
~~~ bash
redis-server
~~~
> Execute os testes para ver se está tudo correto:
~~~ bash
python3 pytest
~~~ 

> Execute a aplicação:
~~~ bash
python3 run.py
~~~

> Acesse a documentação da API em:
~~~
http://localhost:5000/docs/
~~~

## Materiais utilizados

> Arquitetura limpa

* https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
* https://www.zup.com.br/blog/clean-architecture-arquitetura-limpa

> Estilização do códico e API

* https://peps.python.org/pep-0008/
* https://black.readthedocs.io/en/stable/
* https://flake8.pycqa.org/en/latest/
* https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status
* https://jsonapi.org/

> Commits personalizados

* https://pre-commit.com/
