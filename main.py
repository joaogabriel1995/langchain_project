from fastapi import FastAPI
from contextlib import asynccontextmanager
from api.v1.router import api_router
from messaging.rabbitmq_listener import main
import asyncio

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicia o listener RabbitMQ em segundo plano ao iniciar a aplicação
    task = asyncio.create_task(main())
    print("RabbitMQ listener started in the background.")
    
    try:
        yield  # Permite que o FastAPI continue sua inicialização normalmente
    finally:
        # Finaliza o listener quando a aplicação é desligada
        task.cancel()
        await task
        print("RabbitMQ listener has been stopped.")

app = FastAPI(lifespan=lifespan)

# Inclui as rotas do projeto
app.include_router(api_router, prefix="/api/v1")
