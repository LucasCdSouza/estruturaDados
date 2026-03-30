from email import Email


def cadastrar_aluno_novo(lista):
    for i in range(len(lista)):
        nome = input(f"Digite o nome do aluno {i+1}: ")
        lista[i].set_aluno(nome)


def main():

    lista = [Email() for _ in range(3)]

    cadastrar_aluno_novo(lista)

    for aluno in lista:
        print("Nome do aluno:", aluno.get_aluno())
        print("Email do aluno:", aluno.get_email())


if __name__ == "__main__":
    main()