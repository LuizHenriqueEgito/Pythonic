import asyncio
import random

async def producer(q: asyncio.Queue):
    for i in range(5):
        delay = round(random.uniform(1, 5), 0)
        await asyncio.sleep(delay)  # simula tempo de produção
        item = f"{i}"
        await q.put(item)
        print(f"\033[93m[PRODUCER]\033[0m Produziu {item} | Tempo de processamento: {delay}\n")
    # sinal de que acabou
    await q.put(None)


async def consumer(q: asyncio.Queue):
    while True:
        item = await q.get()

        if item is None:
            q.task_done()
            break

        print(f"\033[35m[CONSUMER]\033[0m Consumindo {item}\n")
        await asyncio.sleep(random.uniform(1, 2))  # simula processamento

        q.task_done()


async def main():
    q = asyncio.Queue()

    prod = asyncio.create_task(producer(q))
    cons = asyncio.create_task(consumer(q))

    await prod
    # espera todos os itens serem processados
    await q.join()
    await cons


if __name__ == '__main__':
    asyncio.run(main())