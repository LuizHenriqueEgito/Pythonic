'''
spin -> sleep(0.1) -> spin -> sleep(0.1) -> spin -> sleep(0.1) -> ... (até 3s)
'''
import asyncio
import itertools

async def spin(msg: str) -> None:
    'Função de animação com loop infinito.'
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            SLEEP = 0.1
            await asyncio.sleep(SLEEP)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

async def slow() -> int:
    'Função de espera'
    SECONDS = 3
    await asyncio.sleep(SECONDS)
    return 42

async def supervisor() -> int:
    'Spin e Slow estão rodando concorrentemente.'
    # spin é uma função async que será executada em paralelo como uma Task do async
    spinner = asyncio.create_task(spin('thinking!'))  # registra spin no loop de eventos e inicia sua exec
    print(f'spinner object: {spinner}')
    # Espera pela tarefa demorada
    result = await slow()
    # Para a exec do spin
    spinner.cancel()  # É como o done.set no threading
    return result

def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')



if __name__ == '__main__':
    main()