import time
from concurrent.futures import ThreadPoolExecutor

N_WORKERS = 2
SLEEP = 2

def task(n: int) -> int:
    print(f'[TASK] - {n} is starting.')
    time.sleep(SLEEP)
    print(f'[TASK] - {n} is complete!')
    return n * n

def main() -> None:
    with ThreadPoolExecutor(max_workers=N_WORKERS) as executor:
        results = executor.map(task, range(5))
    print(f'Results: {list(results)}')
    print('Main thread finished!')

if __name__ == '__main__':
    main()