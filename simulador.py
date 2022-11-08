import random

class SimuladorDados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'você gostaria de gerar um novo valor para o dado?'

    def iniciar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim':
            self.valorDado()

    def valorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDados()
simulador.iniciar()