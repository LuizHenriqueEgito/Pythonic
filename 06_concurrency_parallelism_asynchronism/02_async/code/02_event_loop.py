# O asyncio usa o event_loop por debaixo dos panos, é ele quem faz a orquestração de todo o fluxo
# dentro de uma thread, ele:
# - Agenda tarefas
# - Pausa e retorna coroutines
# - Espera eventos (I/O, timers)
# - Decide o que deve rodar "agora"
# asyncio.run() abstrai a camada do event_loop
import asyncio

async def main():
    print('Iniciando...')
    await asyncio.sleep(1)
    print('Finalizado!')

if __name__ == '__main__':
    print('Rodando sem `event_loop`')
    asyncio.run(main())
    print('-' * 30)
    print('Rodando com `event_loop`')
    # asyncio.run(): abstrai tudo isso
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()