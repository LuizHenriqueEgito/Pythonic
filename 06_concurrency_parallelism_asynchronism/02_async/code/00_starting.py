# async def e await são "açucar sintático" da linguagem
# foobar_1 e foobar_2 são exatamente a mesma coisa
# rode assum: uv run --python 3.8 00_starting.py (pois versões mais novas não permitem @asyncio.corroutine)
import asyncio

@asyncio.coroutine
def foobar_1():
    yield from asyncio.sleep(1)
    print('fobar_1 finalizado.')

async def foobar_2():
    await asyncio.sleep(1)
    print('fobar_2 finalizado.')

async def main():
    await foobar_1()
    await foobar_2()

if __name__ == '__main__':
    asyncio.run(main())

# Retorno:
# 00_starting.py:6: DeprecationWarning: "@coroutine" decorator is deprecated since Python 3.8, use "async def" instead
#   def foobar_1():
# fobar_1 finalizado.
# fobar_2 finalizado.