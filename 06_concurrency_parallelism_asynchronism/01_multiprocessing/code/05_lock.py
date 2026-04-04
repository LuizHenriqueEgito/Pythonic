# Quando muitos processos acessam o mesmo recurso podemos ter condições de corrida
from multiprocessing import Process, Value, Lock

N_PROCESS = 2
RANGE = 10_000

def worker_nonlock(counter):
    for _ in range(RANGE):
        # operação não safe
        counter.value += 1

def worker(counter, lock):
    for _ in range(RANGE):
        with lock:
            counter.value += 1

def main_nonlock() -> None:
    counter = Value('i', 0)

    process = [
        Process(target=worker_nonlock, args=(counter,))
        for _ in range(N_PROCESS)
    ]
    # incia todos os processos
    for p in process:
        p.start()

    for p in process:
        p.join()

    print(f"[main_nonlock] Resultado: {counter.value:_}")

def main() -> None:
    counter = Value('i', 0)
    lock = Lock()
    process = [
        Process(target=worker, args=(counter, lock))
        for _ in range(N_PROCESS)
    ]
    # incia todos os processos
    for p in process:
        p.start()

    for p in process:
        p.join()

    print(f"[main] Resultado: {counter.value:_}")

if __name__ == "__main__":
    main_nonlock()
    print(f'Resultado deveria ser {N_PROCESS * RANGE:_}')
    main()