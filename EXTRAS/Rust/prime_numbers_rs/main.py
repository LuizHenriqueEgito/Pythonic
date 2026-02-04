import time
from prime_numbers_rs import is_prime_rust

# esse código em python demora muito, mas muito mais do que aqui
start = time.perf_counter()
list_primes = is_prime_rust(5_000_000)
elapsed = time.perf_counter() - start
print(len(list_primes))
print(f"Tempo: {elapsed:.3f} segundos")
N = 50
list_ = [x for x in range(N)]
f = [num for num, cond in zip(list_, list_primes) if cond]
print(f)
