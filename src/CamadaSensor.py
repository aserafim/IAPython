import numpy
import pandas
from src import Neuronio

class Sensores:

    dataSet = 0
    dadosEntrada = 0
    neuroniosSensores = []

#Le os dados a partir do caminho informado
    def leitura(self, path):
        self.dataSet = pandas.read_csv(path, header=None)

#Cria uma lista de Neuronios com base na quantidade
#de colunas do arquivo de entrada de dados
#e armazena cada uma das entradas na variavel output
#dos respectivos neuronios
    def getDados(self):
        for i in range(self.dataSet.shape[1] - 1):
            self.neuroniosSensores.append(Neuronio.Perpectron())
            self.neuroniosSensores[i].output = self.dataSet.loc[0,i]



    #def gerarListaNeuronios(self):
