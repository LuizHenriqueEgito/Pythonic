from multiprocessing import Process, Value
import time

# Value: Cria uma memória compartilhada que ambos os processos podem acessar
def worker(contador):
    for _ in range(5):
        time.sleep(1)
        contador.value += 1
        print(f"[Worker] contador = {contador.value}")


def main():
    # Criando um contador compartilhado (com Value)
    contador = Value('i', 0)

    p = Process(target=worker, args=(contador,))
    p.start()

    for _ in range(5):
        time.sleep(1)
        print(f"[Main] contador = {contador.value}")

    p.join()


if __name__ == "__main__":
    main()