# Uma Thread Daemon não impede o processo Python de encerrar.
# Daemon Thread não é algo em backgroud (meio que todas são)
# Daemon Thread são threads descartáveis.
import threading
import time

def worker():
    while True:
        t = threading.current_thread()
        print(f'[{t.name} - ID: {t.ident}] > Rodando...')
        time.sleep(0.5)

    
def main():
    t = threading.Thread(
        target=worker,
        daemon=True
    )
    t.start()  # inicia
    time.sleep(5)
    print('Main Thread terminou.')
    time.sleep(1)
    print('Finalizando...')

if __name__ == '__main__':
    main()