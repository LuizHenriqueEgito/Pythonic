import time
from queue import Queue
from threading import Thread


PRODUCER_SLEEP = 1
CONSUMER_SLEEP = 2

def producer_fn(q: Queue) -> None:
    for i in range(5):
        item = f"item-{i}"
        print(f"[Producing] - {item}\n")
        q.put(item)
        time.sleep(PRODUCER_SLEEP)
    q.put(None)  # Sinal para consumer que a producer finalizou


def consumer_fn(q: Queue) -> None:
    while True:
        item = q.get()
        if item is None:
            break
        print(f"[Consuming] - {item}\n")
        time.sleep(CONSUMER_SLEEP)

def main():
    q = Queue()
    producer_thread = Thread(target=producer_fn, args=(q,))
    consumer_thread = Thread(target=consumer_fn, args=(q,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print("Main thread finished.")

if __name__ == '__main__':
    main()