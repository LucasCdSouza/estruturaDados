import collections

class Metodo:

    @staticmethod
    def gera_ficha_normal(filaNormal, contadorNormal):
        print("Imprimindo ficha normal...", contadorNormal)
        filaNormal.append(contadorNormal)
        return contadorNormal + 1

    @staticmethod
    def gera_ficha_prioritaria(filaPrioritaria, contadorPrioritario):
        print("Imprimindo ficha prioritária...", contadorPrioritario)
        filaPrioritaria.append(contadorPrioritario)
        return contadorPrioritario + 1

    @staticmethod
    def gera_atendimento(filaNormal, filaPrioritaria, contadorAtendimentos):

        if not filaNormal and not filaPrioritaria:
            print("Não há fichas para chamar.")
            return contadorAtendimentos

        print("Chamando ficha...", end=" ")

        
        if contadorAtendimentos % 3 == 0 or not filaNormal:
            if filaPrioritaria:
                ficha = filaPrioritaria.popleft()
                print("PRIORITÁRIA...", ficha)
                return contadorAtendimentos + 1

        # atendimento normal
        if filaNormal:
            ficha = filaNormal.popleft()
            print("NORMAL...", ficha)
            return contadorAtendimentos + 1

        return contadorAtendimentos

    @staticmethod
    def gera_fichas_faltantes(filaNormal, filaPrioritaria):

        if not filaNormal and not filaPrioritaria:
            print("Não há fichas para chamar.")
            return

        if filaNormal:
            print("NORMAL:", len(filaNormal), "-", list(filaNormal))

        if filaPrioritaria:
            print("PRIORITÁRIA:", len(filaPrioritaria), "-", list(filaPrioritaria))