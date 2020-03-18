from random import uniform

class Perpectron:
    weight = []
    output = 1.0
    sum = 1.0

#    def __init__(self, w):
#        self.weight = w

#Gera os pesos a partir de numeros aleatórios no subconjunto (-1, 1)
    def generateWeight(self):
        for i in range(20):
            self.weight.append(uniform(-1,1))

#Retorna o valor de saida
    def getOutput(self):
        return self.output




