# Salvando os resultados
import time
from functools import wraps
from typing import Callable
from multiprocessing import Process, current_process, Queue

SLEEP_TIME = 10

# decorator para medir o tempo de execução de uma função
def timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[{func.__name__}] levou {end - start:.4f} segundos")
        return result
    return wrapper

# faz a computação que desejamos
def worker(x: int, queue: Queue) -> None:
    process = current_process()
    p_id = process.pid  # id do processo
    name = process.name  # nome do processo
    print(f"[{name} | (PID: {p_id})]: processando {x}")
    time.sleep(SLEEP_TIME)
    x_pow = x * x
    print(f"[{name} | (PID: {p_id})]: {x}² = {x_pow}")
    queue.put(x_pow)

@timer
def main() -> None:
    # Aqui é onde iremos guardar os resultados
    queue = Queue()

    # parametriza todos os processos
    process = [
        Process(target=worker, args=(i, queue))
        for i in range(1, 16)
    ]

    # incia todos os processos
    for p in process:
        p.start()
    # espera todos os processos finalizarem
    for p in process:
        p.join()

    results = [queue.get() for _ in process]

    print('-' * 3)
    print("Resultados:", results)

if __name__ == '__main__':
    main()