import csv
from Clima import Clima

class Metodo:

    @staticmethod
    def ler_csv(dados_clima):

        # lista que usei para armazenar os objetos Clima criados a partir do CSV
        climas = []

        with open(dados_clima, newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)

            for linha in leitor:
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

                    climas.append(clima)

        return climas

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
    def analisar_dados(climas):

        # listas que usei para armazenar os objetos Clima de cada estação do ano
        Verao = []
        Inverno = []
        Outono = []
        Primavera = []

        for c in climas:
            estacao = Metodo.estacao_ano(c.mes)

            if estacao == "Verão":
                Verao.append(c)
            elif estacao == "Inverno":
                Inverno.append(c)
            elif estacao == "Outono":
                Outono.append(c)
            elif estacao == "Primavera":
                Primavera.append(c)


        # variáveis para armazenar a soma dos níveis de chuva de cada estação
        soma_Verao = sum(c.nivel_chuva for c in Verao)
        soma_Inverno = sum(c.nivel_chuva for c in Inverno)
        soma_Outono = sum(c.nivel_chuva for c in Outono)
        soma_Primavera = sum(c.nivel_chuva for c in Primavera)

        # contagem de registros por temperatura em cada estação
        quente = {
            "Verão": sum(1 for c in Verao if c.temperatura == "Quente"),
            "Outono": sum(1 for c in Outono if c.temperatura == "Quente"),
            "Inverno": sum(1 for c in Inverno if c.temperatura == "Quente"),
            "Primavera": sum(1 for c in Primavera if c.temperatura == "Quente"),
        }

        ameno = {
            "Verão": sum(1 for c in Verao if c.temperatura == "Ameno"),
            "Outono": sum(1 for c in Outono if c.temperatura == "Ameno"),
            "Inverno": sum(1 for c in Inverno if c.temperatura == "Ameno"),
            "Primavera": sum(1 for c in Primavera if c.temperatura == "Ameno"),
        }

        frio = {
            "Verão": sum(1 for c in Verao if c.temperatura == "Frio"),
            "Outono": sum(1 for c in Outono if c.temperatura == "Frio"),
            "Inverno": sum(1 for c in Inverno if c.temperatura == "Frio"),
            "Primavera": sum(1 for c in Primavera if c.temperatura == "Frio"),
        }

        chuvas = {
            "Verão": soma_Verao,
            "Outono": soma_Outono,
            "Inverno": soma_Inverno,
            "Primavera": soma_Primavera
        }

        print("\nQuantidade de registros por estação:")
        print("Verão:", len(Verao))
        print("Outono:", len(Outono))
        print("Inverno:", len(Inverno))
        print("Primavera:", len(Primavera))

        print("\nResumo climático:")
        print("Estação que mais chove:", max(chuvas, key=chuvas.get))
        print("Estação que menos chove:", min(chuvas, key=chuvas.get))
        print("Estação mais quente:", max(quente, key=quente.get))
        print("Estação mais amena:", max(ameno, key=ameno.get))
        print("Estação mais fria:", max(frio, key=frio.get))

        # optei por usar um dicionário para armazenar os dados por ano 
        # cada chave do dicionário é um ano
        # o valor é outro dicionário que armazena a soma dos níveis de chuva e a contagem de registros por temperatura para aquele ano.
        dados_anos = {}

        for c in climas:
            ano = c.ano

            if ano not in dados_anos:
                dados_anos[ano] = {
                    "chuva": 0,
                    "quente": 0,
                    "frio": 0
                }

            dados_anos[ano]["chuva"] += c.nivel_chuva

            if c.temperatura == "Quente":
                dados_anos[ano]["quente"] += 1

            if c.temperatura == "Frio":
                dados_anos[ano]["frio"] += 1

        # para determinar o ano mais quente, mais frio e mais chuvoso, 
        # usei a função max() com uma função lambda para comparar os valores.
        ano_mais_quente = max(dados_anos, key=lambda x: dados_anos[x]["quente"]) 
        ano_mais_frio = max(dados_anos, key=lambda x: dados_anos[x]["frio"])
        ano_mais_chuvoso = max(dados_anos, key=lambda x: dados_anos[x]["chuva"])

        print("\nAnálise por ano:")
        print("Ano mais quente:", ano_mais_quente)
        print("Ano mais frio:", ano_mais_frio)
        print("Ano com mais chuva:", ano_mais_chuvoso)