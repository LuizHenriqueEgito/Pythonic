'''
Problema tenho uma lista indo de 1 até 10 milhões
eu quero passar por essa lista e pegar quem é primo e salvar em uma lista
eu vou contar o tempo de fazer isso sem multiprocess e depois usando multiprocess
e outras libs que também fazem multiprocess 
'''
# TODO: Refatore e comente esse código
import math
import time
from functools import wraps
from multiprocessing import Pool


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Função '{func.__name__}' executou em {end - start:.2f} segundos")
        return result
    return wrapper


def is_prime(list_numbers: list[int]) -> bool:
    primes = []
    for n in list_numbers:
        if n < 2:
            continue
        if n in (2, 3):
            primes.append(n)
        if n % 2 == 0 or n % 3 == 0:
            continue
        
        # Checagem eficiente: apenas 6k ± 1 até sqrt(n)
        limit = int(math.isqrt(n)) + 1
        for i in range(5, limit, 6):
            if n % i == 0 or n % (i + 2) == 0:
                continue
        primes.append(n)
    return primes

@timeit
def run(list_numbers: list[int]) -> list[int]:
    return is_prime(list_numbers=list_numbers)

@timeit
def run_multiprocess(list_numbers: list[int]) -> list[int]:
    N_CPU = 5
    chunk = len(list_numbers) // N_CPU
    list_chunks = [list_numbers[i*chunk:(i+1)*chunk] for i in range(N_CPU)]


    with Pool(processes=N_CPU) as pool:
        results = pool.map(is_prime, list_chunks)

    # junta os resultados de todos os chunks
    return [num for sublist in results for num in sublist]

if __name__ == '__main__':
    N = 5_000_000
    LIST_NUMBERS = [x for x in range(N)]
    print('Sem multiprocess')
    # Para 5MM levou 107.5s
    list_primes = run(list_numbers=LIST_NUMBERS)
    print(len(list_primes))
    print('Com multiprocess e 5 núcloes')
    # Para 5MM levou 22.63s
    list_primes_multiprocess = run_multiprocess(list_numbers=LIST_NUMBERS)
    print(len((list_primes_multiprocess)))
    # Foi 4.75x mais rápido
    # com Rust isso demora 4.55 segundos
    # Foi aproximadamente 5x mais rapido (~4.97x)
