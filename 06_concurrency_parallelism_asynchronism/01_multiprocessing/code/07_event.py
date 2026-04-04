# Event é um sinal entre processos
# event.wait() → espera o sinal
# event.set() → libera
# event.clear() → reseta (volta a travar)
# Event é o botão para iniciar
import time
from multiprocessing import Process, Event

def worker(event, n):
    print(f'Processo {n} esperando o sinal...')
    # espera o sinal do event para começar
    event.wait()
    print(f'Processo {n} começou!')

def main():
    event = Event()
    processos = []

    for i in range(3):
        p = Process(target=worker, args=(event, i))
        processos.append(p)
        p.start()

    # após 3 segundos libera todos os processos
    time.sleep(3)
    print('\nLiberando todos os processos!\n')
    # libera
    event.set()

    for p in processos:
        p.join()

if __name__ == "__main__":
    main()