# Task basicamente é uma coroutine sendo executada pelo event loop
# Ele faz rodar em paralelo, podemos fazer isso com gather e vai ficar ainda melhor
# Gather usar Tasks por baixo dos panos.
import time
import asyncio

async def worker(name: str, sleep: int = 1) -> None:
    print(f'[{name}] > começou.')
    await asyncio.sleep(sleep)
    print(f'[{name}] > finalizou.')

async def main():
    # criando as tasks
    t1 = asyncio.create_task(worker('X', 2))
    t2 = asyncio.create_task(worker('Y', 3))
    t3 = asyncio.create_task(worker('Z', 1))
    print('Tasks criadas.')
    await t1
    await t2
    await t3


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    # perceba que o código demorou apenas 3 segundos para finalizar
    print(f'Esse código demorou: {(end - start):.1f} para ser concluido...')