from collections import deque
from Metodo import Metodo 

class FichaAtendimento:

    @staticmethod   
    def menu():
        """
        Método de classe que mostra o menu de opções para o usuário
        """
        filaNormal = deque()
        filaPrioritaria = deque()
        contadorNormal = 1
        contadorPrioritario = 501
        contadorAtendimentos = 0

        while True:
            print("\nM E N U")
            print("1 - Ficha normal")
            print("2 - Ficha prioritaria")
            print("3 - Chamar ficha")
            print("4 - Listar fichas faltantes")
            print("5 - Sair")
                
            opcao = input("Opção: ")
            if opcao == "1":
                contadorNormal = Metodo.gera_ficha_normal(filaNormal, contadorNormal)
            elif opcao == "2":
                contadorPrioritario = Metodo.gera_ficha_prioritaria(filaPrioritaria, contadorPrioritario)
            elif opcao == "3":
                Metodo.gera_atendimento(filaNormal, filaPrioritaria, contadorAtendimentos)
            elif opcao == "4":
                Metodo.gera_fichas_faltantes()
            elif opcao == "5":
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")