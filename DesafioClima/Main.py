from Metodo import Metodo


def main():
    climas = Metodo.ler_csv("dados.csv") #chama o método que lê o CSV e retorna uma lista com os objetos da classe Clima
    Metodo.dados_estacao(climas) #chama o método que processa os dados


if __name__ == "__main__": #executa o main apenas por este arquivo
    main()