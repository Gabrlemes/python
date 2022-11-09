import random

class chuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 50
        self.tentar_novamente = True

    def iniciar(self):
        self.gerarNumeroAleatorio()
        self.pedirValor()
        try:
            while self.tentar_novamente == True:
                if int(self.valor_chute) > self.valor_aleatorio:
                    print('chute um valor mais baixo!')
                elif int(self.valor_chute) < self.valor_aleatorio:
                    print('chute um valor mais alto!')
                    self.pedirValor()
                if int(self.valor_chute) == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print('você acertou')    
        except:
            print('FAVOR DIGITAR APENAS NÚMEROS INTEIROS')
            self.iniciar()             

    def pedirValor(self):
        self.valor_chute = input('chute um número: ')

    def gerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = chuteONumero()
chute.iniciar()            