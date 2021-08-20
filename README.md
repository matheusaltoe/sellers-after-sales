# Sellers After Sales
Foi desenvolvido um backend voltado a solicitação de agendamento de envio de comunicação. A linguaguem de programação utilizada foi Python, o framework escolhido foi FastAPI devido ao seu desempenho, rápido desenvolvimento, suporte assíncrono, comunicação com JSON, documentação gerada pelo padrão open api, uso da biblioteca Pydantic para validações e definição de schema. O banco de dados é PostgreSQL sendo gerenciado pelo SQLAlchemy como ORM. Como um sistema de mensageria há a implementação do RabbitMQ com o uso do client Pika, as mensagens são enviadas para a fila e processadas para serem salvas no banco de dados. Para testes unitários e integração há o auxílio do Pytest e Faker. Toda a estrutura da aplicação está sendo executada em contêineres utilizando Docker e Docker Compose, facilitando o desenvolvimento e possibilitando uma programação escalável, para posteriormente ser implementado em serviços na nuvem como AWS ECS, Lambda (serverless).

##### Docker Compose

Tendo configurado o Docker Compose, basta executar o comando abaixo para instalar as dependências:

```
docker-compose up --build
```

##### API's

Inicialmente há três endpoints destinados a cadastrar, consultar e deletar informações de agendamento de comunicação.

```GET /api/v1/scheduler/communication```

```POST /api/v1/scheduler/communication```

```DELETE /api/v1/scheduler/communication/{communication_id}```

##### Documentation

As documentações geradas automaticamente no padrão OpenAPI podem ser consultadas nos seguintes endereços:


```http://localhost:8000/docs``` 

```http://localhost:8000/redoc``` 



 
