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
    
    import PlotsUtils as pu
    
    print (dados["consumo"])
    #pu.dfPlot(dados, xValue="consumo", kind= "distplot", xName= "Teste", title= "titutlo teste", bins= 10, size_inches=[12,6], grid= True)
    pu.dfPlot(dados, xValue="temp_max", yValue="consumo", kind= "jointplot", xName= "Teste", title= "titutlo teste", bins= 10, size_inches=[12,6], grid= True)