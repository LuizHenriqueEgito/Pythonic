# Com o Semaphore nos controlamos quantas Tasks vão rodar "simultaneamente" e outra só começa
# quando as que estavam lá terminam.
import time
import asyncio

N_SIMULTANEOUS = 2
RESPONSE_TIME = 2
METHODS = ['POST', 'GET', 'PUT', 'DELETE', 'PATCH']

async def get_https(
        method: str,
        semaphore: asyncio.Semaphore,
        seconds: int = RESPONSE_TIME
    ) -> str:
    async with semaphore:
        print(f'{method} iniciou')
        await asyncio.sleep(seconds)
        print(f'{method} terminou')
    return f'[{method.upper()}] finished.'

async def main(methods: list[str] = METHODS) -> None:
    semaphore = asyncio.Semaphore(N_SIMULTANEOUS)
    result = await asyncio.gather(
        *[get_https(method, semaphore) for method in methods]
    )
    print(f'{result=}')
    return result

if __name__ == '__main__':
    # esse código deve demorar 6 segundos
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Esse código demorou: {(end - start):.1f}s para ser concluido...')