# Tax API

API que oferece serviços relacionados à tributação

## Configurando o ambiente de desenvolvimento

1) Instale as dependências do projeto utilizando o Poetry:

```
poetry install
```

## Rodando a app localmente

### Rodando as migrações de banco de dados

1) Inicie o banco de dados local utilizando o docker-compose
docker-compose up db

2) Execute o Alembic para rodar as migrações até a última revision
```
poetry run alembic upgrade head
```

Precisa adicionar uma nova revision do banco? Adicione uma nova migração com o comando:
```
poetry run alembic revision --autogerate -m "descrição da migração"
```

### Iniciando a aplicação
```
poetry run fastapi dev src/main.py
```

O serviço pode ser acessado através da URL: http://127.0.0.1:8000
A documentação do serviço está disponível em: http://127.0.0.1:8000/docs

### Executando os testes localmente

1) Executando a pipeline de testes
```
poetry run pytest
```