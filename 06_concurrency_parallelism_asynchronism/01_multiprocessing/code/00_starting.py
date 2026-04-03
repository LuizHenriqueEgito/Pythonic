# Fazendo algo simples mas multiprocess

from time import sleep
from multiprocessing import Process, current_process

SLEEP_TIME = 2

# faz a computação que desejamos
def worker(x: int) -> int:
    process = current_process()
    p_id = process.pid  # id do processo
    name = process.name  # nome do processo
    print(f"[{name} | (PID: {p_id})]: processando {x}")
    sleep(SLEEP_TIME)
    x_pow = x * x
    print(f"[{name} | (PID: {p_id})]: {x}² = {x_pow}")
    return x_pow


def main() -> None:
    # parametriza cada processo
    p1 = Process(target=worker, args=(2,))
    p2 = Process(target=worker, args=(3,))
    p3 = Process(target=worker, args=(4,))

    # inicia os processos
    p1.start()
    p2.start()
    p3.start()

    # espera os processos finalizarem
    p1.join()
    p2.join()
    p3.join()

    print('\nMultiprocess Finalizado com Sucesso.')

if __name__ == '__main__':
    main()