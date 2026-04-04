from multiprocessing import Process, Array


ARRAY_DIM = 10
# Mesma coisa do Value, mas ao invés de um valor único temos um Array compartilhado
def worker(arr, idx, valor):
    arr[idx] = valor
    print(f"[Worker] escreveu {valor} na posição {idx}")


def main():
    arr = Array('i', ARRAY_DIM)

    processes = []

    for i in range(ARRAY_DIM):
        p = Process(target=worker, args=(arr, i, i * 10))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("\n[Main] Resultado final:")
    print(list(arr))


if __name__ == "__main__":
    main()