'''
Esse código vai rodar em uma threading diferente.
Em resumo:
Abrimos uma thread para rodar a função spin,
e ela fica lá printando o movimento, e na thread principal
a função slow está rodando, quando slow finaliza done.set() 
é a flag para a thread secundaria finalizar e spinner.join 
encerra a thread e a gente pega o resultado result de slow.
'''
import itertools
import time
from threading import Thread, Event

def spin(msg: str, done: Event) -> None:
    'Função de animação com loop infinito.'
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')  # (6)

def slow() -> int:
    'Função de espera'
    SECONDS = 3
    time.sleep(SECONDS)
    return 42

def supervisor() -> int:
    done = Event()  # Flag de parada, sinaliza a threading quando parar.
    # Dá inicio a threading.
    spinner = Thread(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')  # 
    spinner.start()
    # Roda uma função lenta na threading principal.
    result = slow()
    # Sinaliza para a threading secundaria parar (sair do loop)
    done.set()
    # Finaliza a thread
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()
