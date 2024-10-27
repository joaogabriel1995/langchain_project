# messaging/rabbitmq_listener.py

import asyncio
import aio_pika
from config.settings import settings

class RabbitMQListener:
    def __init__(self, queues):
        self.queues = queues
        self.connection = None
        self.channel = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(settings.model_dump().get("rabbitmq_url"), port=5673)
        self.channel = await self.connection.channel()
        print("Connected to RabbitMQ")

    async def listen_to_queue(self, queue_name, callback):
        queue = await self.channel.declare_queue(queue_name, durable=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print(f"Received message from {queue_name}: {message.body}")
                    callback(message.body)

    async def start_listening(self, tasks):
        await self.connect()
        await asyncio.gather(*tasks)

    async def close(self):
        if self.channel:
            await self.channel.close()
        if self.connection:
            await self.connection.close()

def callback1(message):
    print("Callback1:", message)

def callback2(message):
    print("Callback2:", message)

# Função principal para iniciar o listener
async def main():
    queues = ['fila1', 'fila2', 'fila3']
    listener = RabbitMQListener(queues)
    task1 = listener.listen_to_queue("fila1", callback1)
    task2 = listener.listen_to_queue("fila2", callback2)
    tasks = [task1, task2]
    await listener.start_listening(tasks)
