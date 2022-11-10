import random
import PySimpleGUI as sg

class chuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 50
        self.tentar_novamente = True

    def iniciar(self):
        # layout
        layout = [
            [sg.Text('seu chute', size=(20,0))],
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('chutar')],
            [sg.Output(size=(20,10))]
        ]

        # janela
        self.janela = sg.Window('chute o numero!', layout= layout)

        self.gerarNumeroAleatorio()
        try:
            while True:
                self.eventos, self.valores = self.janela.read()
                self.valor_chute = self.valores['ValorChute']
                if self.eventos == 'chutar':
                    while self.tentar_novamente == True:
                        if int(self.valor_chute) > self.valor_aleatorio:
                            print('chute um valor mais baixo!')
                            break
                        elif int(self.valor_chute) < self.valor_aleatorio:
                            print('chute um valor mais alto!')
                            break
                        if int(self.valor_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('você acertou')    
                            break
        except Exception:
            print('FAVOR DIGITAR APENAS NÚMEROS INTEIROS')
            self.iniciar()             
            
    def gerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = chuteONumero()
chute.iniciar()            