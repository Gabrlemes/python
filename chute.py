import random

class chuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 50
        self.tentarNovamente = True

    def iniciar(self):
        self.GerarNumeroAleatorio()
        self.pedirValor()
        while self.tentarNovamente == True:
            if int(self.valor_chute) > self.valor_aleatorio:
                print('chute um valor mais baixo!')
            elif int(self.valor_chute) < self.valor_aleatorio:
                print('chute um valor mais alto!')
                self.pedirValor()
            self.tentarNovamente = False
            print('você acertou')    

    def pedirValor(self):
        self.valor_chute = input('chute um número: ')

        def gerarNumeroAleatório(self):
            self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = chuteONumero()
chute.iniciar()            