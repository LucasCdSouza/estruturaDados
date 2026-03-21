from Metodo import Metodo


def main():
    climas = Metodo.ler_csv("dados.csv")
    Metodo.analisar_dados(climas)


if __name__ == "__main__":
    main()