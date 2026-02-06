import time
import threading

from colorama import Fore, Style

N_WORKERS = 5
lista = []
lock_gil = threading.Lock() 

def worker():
    t = threading.current_thread()
    while True:
        tamanho = len(lista)
        print(f'{Fore.WHITE}[{t.name}] > {Fore.RED}Tamanho antes do Lock: {tamanho}')
        # sleep para mudar de thread
        time.sleep(0.1)
        with lock_gil:
            if len(lista) == 20:
                print(Style.RESET_ALL, end="")
                break
            tamanho = len(lista)
            print(f'{Fore.WHITE}[{t.name}] > {Fore.GREEN}Tamanho no Lock: {tamanho}')
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
