import time
from prime_numbers_fn import parallel_worker

if __name__ == '__main__':
    # para meio bilhão demorou cerca de 11 minutos
    N = 500_000_000  # isso não rodaria nunca em python puro
    numbers_list = list(range(N))

    start_parallel = time.time()
    primes = parallel_worker(numbers_list)
    time_parallel = time.time() - start_parallel
    print(f'Tempo gasto: {time_parallel}')
    print(f'Primeiros 10 itens: {primes[:10]}')
    print(f'Últimos 10 itens: {primes[-10:]}')
    print(f'Tempo utilizado: {time_parallel:.2f}')
