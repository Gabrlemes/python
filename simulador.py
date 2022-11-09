import random as random
import PySimpleGUI as sg

class SimuladorDados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # self.mensagem = ('você gostaria de gerar um novo valor para o dado?')
        self.layout = [
            [sg.Text('jogar o dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]
        

    def iniciar(self):
        self.janela = sg.Window('simulador de dado', layout=self.layout)
        self.eventos, self.valores = self.janela.read()
        
        try:
             if self.eventos == 'sim' or self.eventos == 's':
                    self.valorDado()
             elif self.eventos == 'não' or self.eventos == 'n':
                    print('entendido!')
             else:
                    print('favor digitar sim ou não')
        except:
                print('ocorreu um erro inesperado')

    def valorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDados()
simulador.iniciar()