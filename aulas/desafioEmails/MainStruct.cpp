#include <iostream>
#include "struct.h"

using namespace std;

void cadastrarAlunoNovo(Email lista[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        cout << "Digite aqui o nome do aluno " << (i + 1) << ": ";
        string nome;
        getline(cin, nome);

        setAluno(lista[i], nome);
    }
}

int main() {
    Email lista[3];

    cadastrarAlunoNovo(lista, 3);

    for (int i = 0; i < 3; i++) {
        cout << "Nome do aluno: " << lista[i].aluno << endl;
        cout << "Email do aluno: " << lista[i].email << endl;
    }

    return 0;
}