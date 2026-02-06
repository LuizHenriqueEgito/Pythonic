# Controlando quando um thread inicia com Events
import time
from threading import Thread, Event

SLEEP = 2

def worker(event: Event) -> None:
    print('Worker waiting for evento to start...')
    event.wait()  # espera até o evento
    print('Worker starting work!')
    for _ in range(10):
        print('Working...')
        time.sleep(SLEEP)
    print('Worker finished.')


def main() -> None:
    event = Event()
    thread = Thread(target=worker, args=(event,))
    thread.start()
    time.sleep(SLEEP)
    print("Main thread sets the event.")
    event.set()  # aqui o evento é iniciado
    thread.join()
    print('Main thread finished.')

if __name__ == '__main__':
    main()