# Pool é um grupo de processos pronto para trabalhar
# Ao invés de criar manualmente o Pool já faz isso para você
# isso se parece muito com Lisp (list processor - programação funcional)
from multiprocessing import Pool

def worker(x):
    return x * 2

def main() -> None:
    with Pool(2) as p:
        resultados = p.map(worker, [1, 2, 3, 4, 5])

    print(resultados)


if __name__ == "__main__":
    main()