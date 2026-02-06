'''
Docstring for 0.6-ConcurrencyParallelismAsynchronism.00_threading.code.002_threads
Eu vou abrir 6 threads cada uma vai ficar lançando dados, cada thread terá como nome
o valor de uma face do dado. Quando a thread lançar o dado e der o valor do seu nome
ela para jogar. A thread vencedora ganha quando fizer isso em menos jogadas.
'''
import time
import random
import threading

threads_names = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis']

NAME_TO_NUMBER = {
    'um': 1,
    'dois': 2,
    'três': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
}

ranking = {}
# Faz o Lock(), trava o uso do GIL para prints que desejo ver
print_lock = threading.Lock()

# Função que irá identificar a thread e ficar jogando o dado.
def worker(name: str):
    t = threading.current_thread()
    target = NAME_TO_NUMBER[name]
    resultados = []

    with print_lock:
        print(f"{'Ligando':=^50}")
        print(f"Thread: {t.name} | ID: {t.ident} | Número alvo: {target}")
        print("=" * 50)
    time.sleep(0.5)

    while True:
        dado = random.randint(1, 6)
        resultados.append(dado)
        time.sleep(0.1)

        print(f"[worker {name}] > dado: {dado}")

        if dado == target:
            print(f"[worker {name}] > Conseguiu!")
            # Trava o GIL e escreve em ranking
            ranking[name] = resultados
            return None

# Função main para execução das threads
def main():
    # lista para adicionar todas as threads e dar join depois.
    threads = []

    for name in threads_names:

        t = threading.Thread(
            target=worker,
            name=f"worker-{name}",
            args=(name,)
        )

        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nRANKING FINAL:")

    ranking_ordenado = sorted(
        ranking.items(),
        key=lambda item: len(item[1])  # sorteia pelo numero de jogadas
    )

    for posicao, (name, lista) in enumerate(ranking_ordenado, start=1):
        print(
            f"{posicao}º lugar → {name:<10} | "
            f"lançamentos: {len(lista):<3} | "
            f"histórico: {lista}"
        )
    campeao, lista_campeao = ranking_ordenado[0]
    print(f"\nCAMPEÃO: {campeao} com {len(lista_campeao)} lançamentos!")


if __name__ == "__main__":
    main()
