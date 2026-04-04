# TODO: Entenda melhor o que está acontecendo
# ele acessa a memoria compartilhada apenas pelo nome?
from multiprocessing import Process
from multiprocessing import shared_memory
import numpy as np

def worker(name):
    # conecta à memória existente
    shm = shared_memory.SharedMemory(name=name)
    array = np.ndarray((5,), dtype=np.int64, buffer=shm.buf)
    # modifica
    array *= 2
    shm.close()

def main() -> None:
    # cria array
    data = np.array([1, 2, 3, 4, 5], dtype=np.int64)

    # cria memória compartilhada
    shm = shared_memory.SharedMemory(create=True, size=data.nbytes)

    # copia dados para memória
    shared_array = np.ndarray(data.shape, dtype=data.dtype, buffer=shm.buf)
    shared_array[:] = data[:]

    # cria processo
    p = Process(target=worker, args=(shm.name,))
    p.start()
    p.join()

    print("Resultado:", shared_array)

    shm.close()
    # libera memória
    shm.unlink()


if __name__ == "__main__":
    main()