import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def matrizCorrelacao(df):
    #Define a relacao entre as variaveis do dataframe

    return df.corr()


if __name__ == "__main__":

    dados = pd.read_csv(r"./arquivosTeste/Consumo_cerveja.csv", sep= ";")

    dados.shape
    print(dados.describe().round(2))

    print (matrizCorrelacao(dados))
    