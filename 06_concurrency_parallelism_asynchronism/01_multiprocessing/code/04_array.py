from multiprocessing import Process, Array


def worker(arr, idx, valor):
    arr[idx] = valor
    print(f"[Worker] escreveu {valor} na posição {idx}")


def main():
    arr = Array('i', 5)

    processes = []

    for i in range(5):
        p = Process(target=worker, args=(arr, i, i * 10))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("\n[Main] Resultado final:")
    print(list(arr))


if __name__ == "__main__":
    main()