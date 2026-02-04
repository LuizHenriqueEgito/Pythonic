# esse código roda infinito pois não conseguimos pegar o GIL de volta, dado a recursividade
# `RLock` significa Reentrant Lock (lock reentrante).
# É um lock que a mesma thread pode adquirir mais de uma vez
# Sem causar deadlock
# Um `Lock` não é reentrante.
import threading
import time

lock = threading.RLock()

def f():
    print("f: tentando adquirir lock")
    with lock:
        print("f: lock adquirido")
        g()
    print("f: terminou")  # nunca termina

def g():
    print("g: tentando adquirir lock (DEADLOCK AQUI)")
    with lock:  # deadlock
        print("g: lock adquirido")  # nunca chegamos aqui pois f() trava o Lock


def main():
    t = threading.Thread(target=f)
    t.start()
    t.join()


if __name__ == '__main__':
    main()
