# Aqui iremos simular asyncronismo varias execuções concorrentes orquestradas pelo event_loop
import time
import asyncio


RESPONSE_TIME = 2
METHODS = ['POST', 'GET', 'PUT', 'DELETE', 'PATH']

async def get_https(method: str, seconds: int = RESPONSE_TIME) -> str:
    await asyncio.sleep(seconds)
    return f'[{method.upper()}] finished.'

async def main(methods: list[str] = METHODS) -> list[str]:
    # Se isso fosse um código sequencia era para ele demorar
    # 5 * 2 = 10 segundos
    # mas por ser assincrono vai levar apenas (aproximadamente) 2 segundos
    # isso pois ele lança a função `get_https` para todos de uma vez
    # e pega o retorno de uma vez também.
    result = await asyncio.gather(
        *[get_https(method) for method in methods]  # fazemos assim para ser mais fácil
    )
    # isso também funcionaria, mas desempacotando como foi feito acima é mais elegante
    # result = await asyncio.gather(
    #     get_https(methods[0]),
    #     get_https(methods[1]),
    #     get_https(methods[2]),
    #     get_https(methods[3]),
    #     get_https(methods[4]),
    # )
    print(f'{result=}')
    return result


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Esse código demorou: {(end - start):.1f} para ser concluido...')