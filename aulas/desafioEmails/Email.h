#include <string>
#include <algorithm>

using namespace std;

class Email {
private:
    string aluno;
    string email;

    string gerarEmail(string nome) {
        string nomeLower = nome;

        for (int i = 0; i < nomeLower.length(); i++) {
            nomeLower[i] = tolower(nomeLower[i]);
        }

        int p = nomeLower.find(' ');
        int u = nomeLower.find_last_of(' ');

        if (p != -1) {
            return nomeLower.substr(0, p) + "." + nomeLower.substr(u + 1) + "@ufn.edu.br";
        }

        return nomeLower + "@ufn.edu.br";
    }

public:
    void setAluno(string nome) {
        aluno = nome;
        email = gerarEmail(nome);
    }

    string getAluno() {
        return aluno;
    }

    string getEmail() {
        return email;
    }
};