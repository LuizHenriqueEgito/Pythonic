import time
import asyncio

# Await: Pausa a execução da coroutine atual e entrega o controle para o event_loop
# até o resultado ficar pronto. Ele não bloqueia a `thread`.
# Utilizamos `await` geralmente com:
# - timers
# - redes: APIs, HTTP
# - I/O (arquivos)
# - Tarefas concorrentes
# - Banco de dados

SECONDS = 2

class MyAwaitable:
    def __await__(self):
        print(f'Estou na classe e vou demorar: {SECONDS} segundos aqui.')
        yield from asyncio.sleep(SECONDS).__await__()
        return 'Finalizei'

async def async_fn():
    print(f'Estou na função e vou demorar: {SECONDS} segundos aqui.')
    await asyncio.sleep(SECONDS)
    return 42

async def main() -> None:
    # aqui usamos await asyncio.sleep mas podemos usar await para qualquer coisa que é async
    print(f'Iniciei a MAIN e vou ficar: {SECONDS} aqui.')
    await asyncio.sleep(SECONDS)
    # podemos fazer isso
    result = await async_fn()
    # podemos fazer isso
    result_class = await MyAwaitable()
    print(f'{result=}')
    print(f'{result_class=}')
    # mas atenção essa função AINDA não é concorrente

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Esse código demorou: {(end - start):.1f} para ser concluido...')
