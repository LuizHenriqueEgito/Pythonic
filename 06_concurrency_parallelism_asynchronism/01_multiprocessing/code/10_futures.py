# futures: É um jeito mais simples e organizado de se usar process
# se parece com Pool
# TODO: Entenda como funciona o submit
from concurrent.futures import ProcessPoolExecutor

def worker(x):
    return x * 2

def main() -> None:
    with ProcessPoolExecutor(max_workers=2) as executor:
        resultados = list(executor.map(worker, [1, 2, 3, 4]))

    print(resultados)


if __name__ == "__main__":
    main()