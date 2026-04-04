# Pipe é um canal de comunicação simples entre processos
from multiprocessing import Process, Pipe


def worker(conn) -> None:
    # 2. recebe mensagem do pai (que foi o input do usuario)
    msg = conn.recv()
    print(f'[Filho] Recebeu: {msg}')

    # 3. via conexão o processo filho envia a msg para o processo pai com send
    resposta = f'Filho processou: {msg.upper()}'
    conn.send(resposta)

    conn.close()

def main() -> None:
    # cria as conexões
    parent_conn, child_conn = Pipe()
    # inicia o processo
    p = Process(target=worker, args=(child_conn,))
    p.start()

    msg = input('Digite uma mensagem: ')

    # 1. envia para o processo filho
    parent_conn.send(msg)

    # 4. recebe resposta do filho
    resposta = parent_conn.recv()
    print(f'[Pai] Recebeu: {resposta}')

    p.join()

if __name__ == "__main__":
    main()
