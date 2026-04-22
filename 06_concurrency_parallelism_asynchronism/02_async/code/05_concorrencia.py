# Aqui iremos simular asyncronismo varias execuções concorrentes orquestradas pelo event_loop
import time
import asyncio


RESPONSE_TIME = 2
METHODS = ['POST', 'GET', 'PUT', 'DELETE', 'PATH']

async def get_https(method: str, seconds: int = RESPONSE_TIME) -> str:
    await asyncio.sleep(seconds)
    return f'[{method.upper()}] finished.'

async def main(methods: list[str] = METHODS) -> list[str]:
    task_post = asyncio.create_task(get_https(methods[0]))
    task_get = asyncio.create_task(get_https(methods[1]))
    task_put = asyncio.create_task(get_https(methods[2]))
    task_delete = asyncio.create_task(get_https(methods[3]))
    task_path = asyncio.create_task(get_https(methods[4]))

    # Rodando todas elas concorrentemente
    result_post = await task_post
    result_get = await task_get
    result_put = await task_put
    result_delete = await task_delete
    result_path = await task_path

    result = [
        result_post,
        result_get,
        result_put,
        result_delete,
        result_path
    ]

    print(f'{result=}')
    return result



if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Esse código demorou: {(end - start):.1f} para ser concluido...')