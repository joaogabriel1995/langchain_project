
# Langchain Project

Este projeto utiliza FastAPI para a criação de uma API e RabbitMQ para a mensageria assíncrona. É uma aplicação que integra processamento de mensagens com filas do RabbitMQ e inclui uma API REST para interações externas.

## Estrutura do Projeto

- **FastAPI**: Framework para construir APIs rápidas e escaláveis em Python.
- **RabbitMQ**: Sistema de mensageria que permite o processamento assíncrono de mensagens.
- **aio_pika**: Biblioteca para comunicação assíncrona com RabbitMQ.
- **Uvicorn**: Servidor ASGI usado para rodar a aplicação FastAPI.

## Pré-requisitos

- Python 3.10+
- RabbitMQ (deve estar em execução)
- Variáveis de ambiente configuradas no arquivo `.env` para RabbitMQ

### Arquivo `.env` de Exemplo

Na raiz do projeto, crie um arquivo `.env` com as seguintes variáveis de ambiente:

```env
RABBITMQ_INTERNAL_PORT=5672
RABBITMQ_URL=amqp://localhost:5673
```

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Inicialização do Projeto

1. **Certifique-se de que o RabbitMQ está em execução** e acessível na URL definida em `RABBITMQ_URL` no arquivo `.env`.

2. **Inicie o servidor FastAPI** com Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

3. **Acesse a documentação da API**:
   - Abra o navegador e vá para [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para visualizar a documentação interativa da API gerada automaticamente pelo FastAPI.

## Estrutura do Código

- `main.py`: Ponto de entrada da aplicação FastAPI. Configura o ciclo de vida do servidor e inicializa o listener do RabbitMQ em segundo plano.
- `config/settings.py`: Configurações do projeto e variáveis de ambiente.
- `messaging/rabbitmq_listener.py`: Implementação do listener RabbitMQ para escutar e processar mensagens de diferentes filas.
- `api/v1/router.py`: Rotas da API (endpoints da aplicação).
- `requirements.txt`: Lista de dependências do projeto.
