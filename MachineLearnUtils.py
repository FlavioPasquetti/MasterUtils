from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import statsmodels.api as sm
import pickle
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

    y_previsto= modelo.predict(X_test)

    R2 = metrics.r2_score(y_test, y_previsto).round(2)
    EQM = metrics.mean_squared_error(y_test, y_previsto).round(2)
    REQM = np.sqrt(metrics.mean_squared_error(y_test, y_previsto)).round(2)

    metricas= pd.DataFrame([EQM, REQM, R2], ["EQM", "REQM", "R2"], columns= ["Metricas"])
    print (metricas)

    coeficientes= pd.DataFrame(data= np.append(modelo.intercept_, modelo.coef_), index= ["Intercepto"] + xValues, columns= ["Parametros"])
    print (coeficientes) 

    if (plotGraph):
        y_previsto_train= modelo.predict(X_train)

        pu.dfPlot (dataFrame, y_previsto_train, yValue= y_train, xName= "Previsto", yName= "Real", title= "(Modelo Regressão Linear) Previsão X Real", kind= "scatterplot", size_inches=(8,6))
        
        residuoQuadrado = (y_train - y_previsto_train)**2
        pu.dfPlot (dataFrame, y_previsto_train, yValue= residuoQuadrado, xName= "Previsto", yName= "Residual", title= "(Modelo Regressão Linear) Residuos X Previsão", kind= "scatterplot", size_inches=(8,6))

    return modelo

#-----------------------------------------------------------------------------------------------------------------------------
def regressionLinearWithLog (dataFrame, yValue, xValues, test_size= 0.5, plotGraph= False):

    y= dataFrame[yValue]
    X= dataFrame[xValues]

    X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= test_size)

    X_train_com_constante = sm.add_constant(X_train)

    modelo= sm.OLS(y_train, X_train_com_constante, hasconst= True).fit()

    # P > |t| para a variavel deve ser menor que 0.05 para ser uma variavel significativa na regressão.. se for maior que esse valor pode ser retirada.
    print (modelo.summary())

    coeficientes= pd.DataFrame(data= np.append(modelo.intercept_, modelo.coef_), index= ["Intercepto"] + xValues, columns= ["Parametros"])
    print (coeficientes) 

    if (plotGraph):
        y_previsto_train= modelo.predict(X_train)

        pu.dfPlot (dataFrame, y_previsto_train, yValue= y_train, xName= "Previsto", yName= "Real", title= "(Modelo Regressão Linear) Previsão X Real", kind= "scatterplot", size_inches=(8,6))
        
        residuoQuadrado = (y_train - y_previsto_train)**2
        pu.dfPlot (dataFrame, y_previsto_train, yValue= residuoQuadrado, xName= "Previsto", yName= "Residual", title= "(Modelo Regressão Linear) Residuos X Previsão", kind= "scatterplot", size_inches=(8,6))

    return modelo

#-----------------------------------------------------------------------------------------------------------------------------
def predictValues (modelo, dataFramePredict, log= False):

    if (log):
        np.exp(modelo.predict(dataFramePredict))
    else:
        return modelo.predict(dataFramePredict)

#-----------------------------------------------------------------------------------------------------------------------------
def saveModelo (modelo, path):
    
    output= open(path, "wb")
    pickle.dump(modelo, output)
    output.close()

#-----------------------------------------------------------------------------------------------------------------------------
def loadModelo (path):
    
    input= open(path, "rb")
    modelo= pickle.load(input)
    input.close()

    return modelo

#-----------------------------------------------------------------------------------------------------------------------------
def correlacaoVars (df):

    print (df.corr())

#=============================================================================================================================
if __name__ == "__main__":

    dados = pd.read_csv(r"./arquivosTeste/Consumo_cerveja.csv", sep= ";")

    teste_regressaoLinear= True

    if (teste_regressaoLinear): 
        y= dados ["consumo"]
        X= dados [["temp_max", "chuva", "fds"]]
        
        correlacaoVars(dados)

        modeloRegres= regressaoLinear(dados, yValue= "consumo", xValues= ["temp_max", "chuva", "fds"], plotGraph= True)

        dataPredict= mu.convertListToPandas (columnsList= [[30.5, 40.1], [12.2, 0.5], [0, 1]], nomesColunas= ["temp_max", "chuva", "fds"])
        print (dataPredict)
        print (modeloRegres.predict(dataPredict))

        saveModelo(modeloRegres, r"./arquivosTeste/Consumo_cerveja")
        modelo = loadModelo(r"./arquivosTeste/Consumo_cerveja")
        print (modelo.predict(dataPredict))
