import threading
import time

N_WORKERS = 5
lista = []

def worker():
    while len(lista) < 20:
        # Além do tamanho da lista ficar maior pois não da para controlar
        # os valores não ficam do jeito que queremos
        tamanho = len(lista)
        # sleep para mudar de thread
        time.sleep(0.1)
        lista.append(tamanho)

def main():
    threads = [
        threading.Thread(target=worker, args=())
        for i in range(N_WORKERS)
    ]
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(lista)


if __name__ == '__main__':
    main()
