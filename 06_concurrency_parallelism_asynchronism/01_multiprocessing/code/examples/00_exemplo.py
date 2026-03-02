'''
Esse códogio roda em um processo diferente.
Multiprocess: múltiplos núcleos da CPU.

Esse código vai rodar em uma núcleo diferente.
Em resumo:
Abrimos um processo (núcleo) para rodar a função spin,
e ele fica lá printando o movimento, e no núcleo principal
a função slow está rodando, quando slow finaliza done.set() 
é a flag para o núcleo secundario finalizar e spinner.join 
encerra o núcleo e então pegamos o resultado result de slow.
'''
import itertools
import time
from multiprocessing import Process, Event
from multiprocessing import synchronize
# Isso significa que objetos cruzando fronteiras entre processos tem que ser serializados e deserializados, criando custos adicionais.


def spin(msg: str, done: Event) -> None:
    'Função de animação com loop infinito.'
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def slow() -> int:
    'Função de espera'
    SECONDS = 3
    time.sleep(SECONDS)
    return 42

def supervisor() -> int:
    done = Event()  # Flag de parada, sinaliza ao processo quando parar.
    spinner = Process(target=spin,args=('thinking!', done))
    # Dá inicio ao processo em outro núcleo.
    print(f'spinner object: {spinner}')
    spinner.start()
    # Roda uma função lenta no núcleo principal.
    result = slow()
    # Sinaliza para o núcleo secundario parar (sair do loop)
    done.set()
    # Finaliza o núcleo
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()