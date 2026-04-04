import time
from multiprocessing import Process, Semaphore
from colorama import init
init()

# Códigos de cores ANSI
GREEN = '\033[92m'
ORANGE = '\033[93m'
RESET = '\033[0m'

# Semaphore trava a entrada, é como uma fila um novo processo só entra quando outro sai
# só N_SEMAPHORE por vez
N_SEMAPHORE = 2
N_PROCESS = 5

def worker(semaphore, n):
    print(f'Processo {n} esperando...')
    
    with semaphore:
        print(f'{GREEN}Processo {n} entrou!{RESET}')
        time.sleep(3)
        print(f'{ORANGE}Processo {n} saindo...{RESET}')

def main() -> None:
    semaphore = Semaphore(N_SEMAPHORE)

    processos = []
    
    for n_process in range(N_PROCESS):
        p = Process(target=worker, args=(semaphore, n_process))
        processos.append(p)
        p.start()

    for p in processos:
        p.join()


if __name__ == "__main__":
    main()