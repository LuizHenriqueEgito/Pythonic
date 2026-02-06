'''
Docstring for 0.6-ConcurrencyParallelismAsynchronism.00_threading.code.001_starting
Quem faz o I/O é a thread main mas as threads secundárias estão recebendo os valores
e manuseando eles, salvando em results.
'''

import threading
from queue import Queue

N_THREADS = 3

# Estrutura compartilhada
queues = {}
results = {}
stop_flags = {} 

def worker(name, queue, stop_event) -> None:
    t = threading.current_thread()
    print(f'{'Ligando':=^50}\n Thread name: {t.name} | Thread id: {t.ident}')
    results[name] = []

    while not stop_event.is_set():
        msg = queue.get()  # bloqueia até chegar algo
        if msg is None:
            break
        results[name].append(msg)
    # Precisa retornar para sair da função e parar
    return None

    print(f"[{name}] finalizada")

def main():
    thread_names = [f'worker-{i}' for i in range(N_THREADS)]

    threads = []
    for name in thread_names:
        q = Queue()
        # threading.Event(): Começa como False é uma flag para o controle da nossa thread
        # ele não encerra a thread mas ele nos ajuda a fazer a função ter um return
        # quando a função te um return a thread ainda existe mas a função não executa mais.
        stop_event = threading.Event()

        # Cria thread
        t = threading.Thread(
            target=worker,
            name=name,
            args=(name, q, stop_event)
        )

        # cria a queue que manda e trava cada thread
        queues[name] = q
        # cada thread se atualiza se deve, ou não continuar
        stop_flags[name] = stop_event

        t.start()
        threads.append(t)

    active_index = 0
    active_thread = thread_names[active_index]

    print("Digite mensagens. 'exit' encerra a thread ativa.")

    while True:
        value = input(f"[{active_thread}] > ")

        if value == "exit":
            # Atualiza o stop_event para True
            stop_flags[active_thread].set()
            # Envie None para a Queue daquela thread
            queues[active_thread].put(None)
            # remove essa thread das opções para não voltarmos para ela
            thread_names.pop(active_index)

            if not thread_names:
                break

            active_index %= len(thread_names)
            active_thread = thread_names[active_index]
            continue

        queues[active_thread].put(value)
        # alterna thread
        active_index = (active_index + 1) % len(thread_names)
        active_thread = thread_names[active_index]

    for t in threads:
        t.join()

    print("\nResultado final:")
    print(results)

if __name__ == "__main__":
    main()
