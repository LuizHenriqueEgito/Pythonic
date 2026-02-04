# esse código roda infinito pois não conseguimos pegar o GIL de volta, dado a recursividade
import threading
import time

lock = threading.Lock()

def f():
    print("f: tentando adquirir lock")
    with lock:
        print("f: lock adquirido")
        g()
    print("f: terminou")  # nunca termina

def g():
    print("g: tentando adquirir lock (DEADLOCK AQUI)")
    time.sleep(2)
    print("Não vai conseguir terminar o programa.")
    with lock:  # deadlock
        print("g: lock adquirido")  # nunca chegamos aqui pois f() trava o Lock


def main():
    t = threading.Thread(target=f)
    t.start()
    t.join()

if __name__ == '__main__':
    main()
