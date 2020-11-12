ANDAR = 1
PESSOA = 1
class Elevador:


    def __init__(self,pessoas = 0,andarAtual = 0):
        self.__andarAtual = andarAtual
        self.__capacidade = pessoas
        self.__totAndares = 14

    def inicializa(self):
        self.__capacidade = qtPessoas = 0
        self.__andarAtual = 0

    def entra(self):
        if self.__capacidade <10:
            self.__capacidade = self.__capacidade +PESSOA

        else:
            print('O elevador já esta cheio. Aguarde.')

    def sai(self):
        if self.__capacidade > 0:
            self.__capacidade = self.__capacidade - PESSOA

        else:
            print('O elevador está vazio.')

    def sobe(self):
        if self.__andarAtual <= self.__totAndares:
            self.__andarAtual = self.__andarAtual + ANDAR

        else:
            print('O elevador já está no último andar')

    def desce(self):
        if self.__andarAtual >=1:
            self.__andarAtual = self.__andarAtual - ANDAR

        else:
            print('O elevador já está no terreo')

    @property
    def andarAtual(self):
        return f'{self.__andarAtual}º andar'

    @property
    def capacidade(self):
        return f'{self.__capacidade} pessoas'

