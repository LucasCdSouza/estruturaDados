import csv
from Clima import Clima

class Metodo:

    @staticmethod
    def ler_csv(dados_clima):

        # lista que usei para armazenar os objetos Clima criados a partir do CSV
        lista_climas = []

        with open(dados_clima, newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)

            for linha in leitor: #lê cada linha do CSV, cria um objeto Clima e o adiciona à lista
                if linha:
                    nivel_chuva = 0

                    if linha[3] == "muita":
                        nivel_chuva = 3
                    elif linha[3] == "média":
                        nivel_chuva = 2
                    elif linha[3] == "pouca":
                        nivel_chuva = 1
                    elif linha[3] == "nada":
                        nivel_chuva = 0

                    clima = Clima(
                        linha[0],  # ano
                        linha[1],  # mês
                        linha[2],  # temperatura
                        nivel_chuva
                    )

                    lista_climas.append(clima) #adiciona o objeto Clima criado à lista

        return lista_climas

    @staticmethod
    def estacao_ano(mes):
        # determina a estação do ano com base no mês informado.

        mes = mes.strip().lower() 

        if mes in ["dezembro", "janeiro", "fevereiro"]:
            return "Verão"
        elif mes in ["março", "marco", "abril", "maio"]:
            return "Outono"
        elif mes in ["junho", "julho", "agosto"]:
            return "Inverno"
        elif mes in ["setembro", "outubro", "novembro"]:
            return "Primavera"
        else:
            return "Desconhecido"

    @staticmethod
    def dados_estacao(climas):

        # listas que usei para armazenar os objetos da classe Clima de cada estação do ano
        lista_Verao = []
        lista_Inverno = []
        lista_Outono = []
        lista_Primavera = []

        for c in climas:
            estacao = Metodo.estacao_ano(c.mes) #chama o método que determina a estação do ano com base no mês do objeto

            if estacao == "Verão":
                lista_Verao.append(c) 
            elif estacao == "Inverno":
                lista_Inverno.append(c)
            elif estacao == "Outono":
                lista_Outono.append(c)
            elif estacao == "Primavera":
                lista_Primavera.append(c)


        # o sum conta a soma dos níveis de chuva de todos os objetos de cada estação
        soma_Verao = sum(c.nivel_chuva for c in lista_Verao) 
        soma_Inverno = sum(c.nivel_chuva for c in lista_Inverno)
        soma_Outono = sum(c.nivel_chuva for c in lista_Outono)
        soma_Primavera = sum(c.nivel_chuva for c in lista_Primavera)

        #contagem de quantos objetos "Quentes existem em cada estação"
        quente = {
            "Verão": sum(1 for c in lista_Verao if c.temperatura == "Quente"),
            "Outono": sum(1 for c in lista_Outono if c.temperatura == "Quente"),
            "Inverno": sum(1 for c in lista_Inverno if c.temperatura == "Quente"),
            "Primavera": sum(1 for c in lista_Primavera if c.temperatura == "Quente"),
        }
        #contagem de quantos objetos "Amenos existem em cada estação"
        ameno = {
            "Verão": sum(1 for c in lista_Verao if c.temperatura == "Ameno"), 
            "Outono": sum(1 for c in lista_Outono if c.temperatura == "Ameno"),
            "Inverno": sum(1 for c in lista_Inverno if c.temperatura == "Ameno"),
            "Primavera": sum(1 for c in lista_Primavera if c.temperatura == "Ameno"),
        }
        #contagem de quantos objetos "Frios existem em cada estação"
        frio = {
            "Verão": sum(1 for c in lista_Verao if c.temperatura == "Frio"),
            "Outono": sum(1 for c in lista_Outono if c.temperatura == "Frio"),
            "Inverno": sum(1 for c in lista_Inverno if c.temperatura == "Frio"),
            "Primavera": sum(1 for c in lista_Primavera if c.temperatura == "Frio"),
        }
        #chuvas armazena a soma dos níveis de chuva de cada estação para facilitar a análise
        chuvas = {
            "Verão": soma_Verao, 
            "Outono": soma_Outono,
            "Inverno": soma_Inverno,
            "Primavera": soma_Primavera
        }
        #saída dos dados processados
        print("\nQuantidade de registros por estação:")
        print("Verão:", len(lista_Verao))
        print("Outono:", len(lista_Outono))
        print("Inverno:", len(lista_Inverno))
        print("Primavera:", len(lista_Primavera))

        print("\nResumo climático:")
        print("Estação que mais chove:", max(chuvas, key=chuvas.get))
        print("Estação que menos chove:", min(chuvas, key=chuvas.get))
        print("Estação mais quente:", max(quente, key=quente.get))
        print("Estação mais amena:", max(ameno, key=ameno.get))
        print("Estação mais fria:", max(frio, key=frio.get))

        analise_anos = {}

        for c in climas:
            ano = c.ano

            if ano not in analise_anos:
                analise_anos[ano] = {
                    "chuva": 0,
                    "quente": 0,
                    "frio": 0
                }

            analise_anos[ano]["chuva"] += c.nivel_chuva

            if c.temperatura == "Quente":
                analise_anos[ano]["quente"] += 1

            if c.temperatura == "Frio":
                analise_anos[ano]["frio"] += 1

        # para determinar o ano mais quente, mais frio e mais chuvoso, 
        # lambda  é usada para a comparação dos valores de temperatura e chuva em cada ano para retornar o maximo de cada categoria
        ano_mais_quente = max(analise_anos, key=lambda x: analise_anos[x]["quente"]) 
        ano_mais_frio = max(analise_anos, key=lambda x: analise_anos[x]["frio"])
        ano_mais_chuvoso = max(analise_anos, key=lambda x: analise_anos[x]["chuva"])

        print("\nAnálise por ano:")
        print("Ano mais quente:", ano_mais_quente)
        print("Ano mais frio:", ano_mais_frio)
        print("Ano com mais chuva:", ano_mais_chuvoso)