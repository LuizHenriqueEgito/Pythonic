import threading
import time

N_THREADS = 3


def worker(name: str, n_times: int) -> None:
    # mostra a thread atual
    t = threading.current_thread()
    print(f'{'Ligando':=^50}\n Thread name: {t.name} | Thread id: {t.ident}\n---')
    time.sleep(0.2)
    for _ in range(n_times * 1):
        print(f'[{name}] > Imprimiu : {n_times} | Vai dormir {n_times * 1} vezes.')
        time.sleep(n_times)
    return None

def main():
    thread_names = [f'worker-{i}' for i in range(N_THREADS)]

    # Cria thread
    threads = []
    for idx, name in enumerate(thread_names):
        n_times = idx + 1
        t = threading.Thread(
            target=worker,
            name=name,
            args=(name, n_times)
        )
        # inicia a thread (isso não trava o código continua)
        t.start()
        # salva elas para finaliza-las depois
        threads.append(t)

    # Aqui o código espera, até que elas tenham finalizado para terminar
    for t in threads:
        t.join()

    print('Finish...')

if __name__ == '__main__':
    main()