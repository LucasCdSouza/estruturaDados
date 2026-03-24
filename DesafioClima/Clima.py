class Clima:
    def __init__(self, ano, mes, temperatura, nivel_chuva):
        self.ano = ano
        self.mes = mes
        self.temperatura = temperatura #apenas ameno, frio e quente
        self.nivel_chuva = nivel_chuva

    def __str__(self): 
        return (
        f"Ano: {self.ano}\n"
        f"Mês: {self.mes}\n"
        f"Temperatura: {self.temperatura}\n"
        f"Chuva: {self.nivel_chuva}\n"
    )