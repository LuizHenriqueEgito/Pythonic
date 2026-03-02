'''
Neste exemplo eu irei simular algumas requisições a um banco de dados
em que cada requisição pode variar entre 1 e 4 segundos utilizando async
e outras libs que usam assincronismo.
'''
import asyncio
from random import randint

async def get_db(request: int):
    time = randint(1, 15)
    print(f'Sou a requisição nº: {request} e vou levar: {time} segundos para finalizar')
    await asyncio.sleep(time)
    print(f'Request nº {request} finalizada levando: {time} segundos')
    msg = f'retornei: {request}'
    return msg

async def coroutine(n_requests):
    return await asyncio.gather(
        *[get_db(request) for request in range(n_requests)]
    )

if __name__ == '__main__':
    print('Rodando a função async')
    retorno_final = asyncio.run(coroutine(10))
    print(retorno_final)