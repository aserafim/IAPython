from random import randint, randrange, uniform
from src import Neuronio
from src import CamadaSensor


sensores = CamadaSensor.Sensores()

path = "../data/caracteres-limpo.csv"

sensores.leitura(path)

print(sensores.dadosEntrada)

sensores.getDados()

print(sensores.neuroniosSensores[62].output)

