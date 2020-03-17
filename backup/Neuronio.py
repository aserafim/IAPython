import pandas as pd

class Receptor:

    dados = []

    # Construtor pedindo peso do neuronio e path
    # do arquivo de dados ????
    def __init__(self, weight, dataPath):
        self.weight = weight
        self.dados = pd.read_csv(dataPath)

    # Getters
    def getData(self):
        print(self.dados)

    def getWeigth(self):
        return self.weight

    # Setters
    def setData(self, dataOrigin):
        self.dados = pd.read_csv(dataOrigin, header=None)

    def setWeight(self, weight):
        self.weight = weight
