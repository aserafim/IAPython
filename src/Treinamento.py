from src import Neuronio
import pandas as pd

class Treinamento:
    def __init__(self,alfa):
        self.alfa = alfa

    def setAlfa(self, alfa):
        self.alfa = alfa

    def getAlfa(self):
        return self.alfa

path = "../data/problemAND.csv"

neu = Neuronio.Receptor(2, path)

neu.getData()