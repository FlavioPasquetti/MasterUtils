from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd
import numpy as np

import MathUtils as mu
import PlotsUtils as pu

#-----------------------------------------------------------------------------------------------------------------------------
def regressaoLinear (dataFrame, yValue, xValues, test_size= 0.5, plotGraph= False):
    
    y= dataFrame[yValue]
    X= dataFrame[xValues]

    X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= test_size)

    modelo= LinearRegression()
    modelo.fit(X_train, y_train)
    print ("R² Treino = {}".format(modelo.score(X_train, y_train).round(2)))

    y_previsto= modelo.predict(X_test)
    print ("R² Testes = %s" % metrics.r2_score(y_test, y_previsto).round(2))

    coeficientes= pd.DataFrame(data= np.append(modelo.intercept_, modelo.coef_), index= ["Intercepto"] + xValues, columns= ["Parametros"])
    print (coeficientes) 

    if (plotGraph):
        y_previsto_train= modelo.predict(X_train)

        pu.dfPlot (dataFrame, y_previsto_train, yValue= y_train, xName= "Previsto", yName= "Real", title= "(Modelo Regressão Linear) Previsão X Real", kind= "scatterplot", size_inches=(8,6))
        
        residuoQuadrado = (y_train - y_previsto_train)**2
        pu.dfPlot (dataFrame, y_previsto_train, yValue= residuoQuadrado, xName= "Previsto", yName= "Residual", title= "(Modelo Regressão Linear) Residuos X Previsão", kind= "scatterplot", size_inches=(8,6))

    return modelo

#-----------------------------------------------------------------------------------------------------------------------------
def predictValues (modelo, dataFramePredict):

    return modelo.predict(dataFramePredict)
    
#=============================================================================================================================
if __name__ == "__main__":

    dados = pd.read_csv(r"./arquivosTeste/Consumo_cerveja.csv", sep= ";")

    teste_regressaoLinear= True

    if (teste_regressaoLinear): 
        y= dados ["consumo"]
        X= dados [["temp_max", "chuva", "fds"]]
        
        modeloRegres= regressaoLinear(dados, yValue= "consumo", xValues= ["temp_max", "chuva", "fds"], plotGraph= True)

        dataPredict= mu.convertListToPandas (columnsList= [[30.5, 40.1], [12.2, 0.5], [0, 1]], nomesColunas= ["temp_max", "chuva", "fds"])
        print (dataPredict)
        print (modeloRegres.predict(dataPredict))



