import threading
import time


N_THREADS_SEMAPHORE = 2
semaphore = threading.Semaphore(N_THREADS_SEMAPHORE)

def worker(thread_id: int):
    print(f'[Thread {thread_id}] - esperando no SEMAFORO...')
    with semaphore:
        print(f'[Thread {thread_id}] - passou no SEMAFORO!')
        time.sleep(2)
        print(f'[Thread {thread_id}] - saindo do SEMAFORO...\n')


def main() -> None:
    threads = []
    for thread_id in range(10):
        t = threading.Thread(target=worker, args=(thread_id,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    print('Processo finalizado...')


if __name__ == '__main__':
    main()