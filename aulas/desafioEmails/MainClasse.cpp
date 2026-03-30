#include <iostream>
#include "Email.h"

using namespace std;

void cadastrarAlunoNovo(Email lista[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        cout << "Digite o nome do aluno " << (i + 1) << ": ";
        string nome;
        getline(cin, nome);

        lista[i].setAluno(nome);
    }
}

int main() {
    Email lista[3];

    cadastrarAlunoNovo(lista, 3);

    for (int i = 0; i < 3; i++) {
        cout << "Nome do aluno: " << lista[i].getAluno() << endl;
        cout << "Email do aluno: " << lista[i].getEmail() << endl;
    }

    return 0;
}