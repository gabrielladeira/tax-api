# Tax API

API que oferece serviços relacionados à tributação

## Configurando o ambiente de desenvolvimento

1) Instale as dependências do projeto utilizando o Poetry:

```
poetry install
```

## Rodando a app localmente

**Utilizando o Poetry**:

1) Iniciando a aplicação
```
poetry run fastapi dev src/main.py
```

O serviço pode ser acessado através da URL: http://127.0.0.1:8000
A documentação do serviço está disponível em: http://127.0.0.1:8000/docs

## Executando os testes localmente

**Utilizando o Poetry**:

1) Executando a pipeline de testes
```
poetry run pytest
```