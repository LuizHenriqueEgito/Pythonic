import time
from typing import Generator
from multiprocessing import Process, Queue


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def chunk_list_generator(list_, chunk_size) -> Generator[list[int], None, None]:
    for i in range(0, len(list_), chunk_size):
        yield list_[i:i + chunk_size]


def filter_primes(numbers: list[int]) -> list[int]:
    return [n for n in numbers if is_prime(n)]


def worker(chunk, q: Queue):
    q.put(filter_primes(chunk))


def main(numbers, chunk_size=200, max_processes=16):
    chunks = list(chunk_list_generator(numbers, chunk_size))
    queue = Queue()
    processes = []
    results = []
    
    # Criar todos os processos de uma vez
    for chunk in chunks:
        p = Process(target=worker, args=(chunk, queue))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
    # Coletar resultados da fila
    while not queue.empty():
        results.extend(queue.get())
    # ordeando para manter a ordem
    return sorted(results)


def sequential_worker(numbers):
    return [n for n in numbers if is_prime(n)]

if __name__ == '__main__':
    N = 500_000
    CHUNK_SIZE = 100_000
    N_PROCESS = 5
    print(f"Procurando números primos até {N:_}...")
    numbers_list = list(range(N))
    
    # PARALELIZANDO
    start_parallel = time.time()
    primes_parallel = main(
        numbers_list,
        chunk_size=CHUNK_SIZE,
        max_processes=N_PROCESS
    )
    time_parallel = time.time() - start_parallel
    print('Versão paralela foi finalizada...')

    # SEQUENCIAL (SEM PARALELIZAR)
    print("Executando versão sequencial...")
    start_seq = time.time()
    primes_seq = sequential_worker(numbers_list)
    time_seq = time.time() - start_seq
    
    # Verificar se os resultados são iguais
    print(f"Primeiros 10 primos: {primes_parallel[:10]}")
    print(f"Últimos 10 primos:   {primes_parallel[-10:]}")
    print(f"\nPERFORMANCE")
    print(f"Tempo paralelo: {time_parallel:.2f} segundos")
    print(f"Tempo sequencial: {time_seq:.2f} segundos")
    print(f"Speedup: {time_seq / time_parallel:.2f}x")