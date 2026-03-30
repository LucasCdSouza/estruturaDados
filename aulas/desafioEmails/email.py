class Email:

    def __init__(self):
        self.aluno = ""
        self.email = ""

    def gerar_email(self, nome):
        partes = nome.lower().split(" ")

        if len(partes) > 1:
            return f"{partes[0]}.{partes[-1]}@ufn.edu.br"

        return f"{partes[0]}@ufn.edu.br"

    def set_aluno(self, nome):
        self.aluno = nome
        self.email = self.gerar_email(nome)

    def get_aluno(self):
        return self.aluno

    def get_email(self):
        return self.email