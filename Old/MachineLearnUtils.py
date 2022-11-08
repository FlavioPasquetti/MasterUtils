from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.svm import LinearSVC, SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.neighbors import KNeighborsClassifier
import graphviz #Necessario instalar no windows -> https://graphviz.org/download/



import statsmodels.api as sm
import statsmodels.formula.api as smf
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

    EQM = modelo.mse_resid
    coeficientes= pd.DataFrame(data= np.append(modelo.intercept_, modelo.coef_), index= ["Intercepto"] + xValues, columns= ["Parametros"])
    print (coeficientes) 

    if (plotGraph):
        y_previsto_train= modelo.predict(X_train)

        pu.dfPlot (dataFrame, y_previsto_train, yValue= y_train, xName= "Previsto", yName= "Real", title= "(Modelo Regressão Linear) Previsão X Real", kind= "scatterplot", size_inches=(8,6))
        
        residuoQuadrado = (y_train - y_previsto_train)**2
        pu.dfPlot (dataFrame, y_previsto_train, yValue= residuoQuadrado, xName= "Previsto", yName= "Residual", title= "(Modelo Regressão Linear) Residuos X Previsão", kind= "scatterplot", size_inches=(8,6))

    return modelo

#-----------------------------------------------------------------------------------------------------------------------------

def classificacao_Linear (dataFrame, yValue, xValues, test_size= 0.5, plotGraph= False):
    
    y= dataFrame[yValue]
    X= dataFrame[xValues]

    X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= test_size)

    modelo= LinearSVC()
    modelo.fit(list(X_train), list(y_train))

    y_previsto= modelo.predict(list(X_test))

    accur = metrics.accuracy_score(y_test, y_previsto).round(2) * 100
    print ("Acuracia da previsao: ", accur, "%")

    return modelo

#-------------------------

if __name__ == "__main__":

    if (False):
        
        # features (1 sim, 0 não)
        # pelo longo?
        # perna curta?
        # faz auau?
        porco1 = [0, 1, 0]
        porco2 = [0, 1, 1]
        porco3 = [1, 1, 0]
        porco4 = [1, 0, 0]
        porco5 = [1, 1, 0]
        cachorro1 = [0, 1, 1]
        cachorro2 = [1, 0, 1]
        cachorro3 = [1, 1, 1]
        cachorro4 = [0, 1, 1]
        cachorro5 = [0, 1, 1]

        # 1 => porco, 0 => cachorro
        treino_x = [porco1, porco2, porco3, porco4, porco5, cachorro1, cachorro2, cachorro3, cachorro4, cachorro5]
        treino_y = [1,1,1,1,1,0,0,0,0,0] # labels / etiqueta

        df = pd.DataFrame(data=list(zip(treino_x, treino_y)), columns=["Entradas", "Resultados"])

        classificacao_Linear (df, "Resultados", "Entradas", test_size= 0.1, plotGraph= True)

#-----------------------------------------------------------------------------------------------------------------------------

def classificacao_NaoLinear (dataFrame, yValue, xValues, test_size= 0.5, plotGraph= False):
    
    y= dataFrame[yValue]
    X= dataFrame[xValues]

    raw_X_train, raw_X_test, y_train, y_test= train_test_split(X, y, test_size= test_size)

    scaler = StandardScaler ()
    scaler.fit(list(raw_X_train))
    X_train= scaler.transform(list(raw_X_train))
    X_test= scaler.transform(list(raw_X_test))

    modelo= SVC()
    modelo.fit(list(X_train), list(y_train))

    y_previsto= modelo.predict(list(X_test))

    accur = metrics.accuracy_score(y_test, y_previsto).round(2) * 100
    print ("Acuracia da previsao: ", accur, "%")
    
    return modelo

#-------------------------

if __name__ == "__main__":

    if (False):
        
        # features (1 sim, 0 não)
        # pelo longo?
        # perna curta?
        # faz auau?
        porco1 = [0, 1, 0]
        porco2 = [0, 1, 1]
        porco3 = [1, 1, 0]
        porco4 = [1, 0, 0]
        porco5 = [1, 1, 0]
        cachorro1 = [0, 1, 1]
        cachorro2 = [1, 0, 1]
        cachorro3 = [1, 1, 1]
        cachorro4 = [0, 1, 1]
        cachorro5 = [0, 1, 1]

        # 1 => porco, 0 => cachorro
        treino_x = [porco1, porco2, porco3, porco4, porco5, cachorro1, cachorro2, cachorro3, cachorro4, cachorro5]
        treino_y = [1,1,1,1,1,0,0,0,0,0] # labels / etiqueta

        df = pd.DataFrame(data=list(zip(treino_x, treino_y)), columns=["Entradas", "Resultados"])

        classificacao_NaoLinear (df, "Resultados", "Entradas", test_size= 0.1, plotGraph= True)

#-----------------------------------------------------------------------------------------------------------------------------

def classificacao_decisionTree (dataFrame, yValue, xValues, test_size= 0.5, plotGraph= False, max_depth= None):
    
    y= dataFrame[yValue]
    X= dataFrame[xValues]

    X_train, X_test, y_train, y_test= train_test_split(X.values, y.values, test_size= test_size)

    modelo= DecisionTreeClassifier(max_depth=max_depth)

    modelo.fit(list(X_train), list(y_train))

    y_previsto= modelo.predict(list(X_test))

    accur = metrics.accuracy_score(y_test, y_previsto).round(2) * 100
    print ("Acuracia da previsao: ", accur, "%")
    
    if (plotGraph):

        dot_data = export_graphviz(modelo, out_file=None,
                                filled = True, rounded = True,
                                feature_names = xValues)

        grafico = graphviz.Source(dot_data)
        grafico.render(view=True)

    return modelo

#-------------------------

if __name__ == "__main__":

    if (True):
        
        # features (1 sim, 0 não)
        # pelo longo?
        # perna curta?
        # faz auau?
        peloLongo= [0, 0, 1, 1, 1, 0, 1, 1, 0, 0]
        pernaCurta= [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
        auau= [0, 1, 0, 0, 0, 1, 1, 1, 1, 1]

        # 1 => porco, 0 => cachorro
        animal = [1,1,1,1,1,0,0,0,0,0] # labels / etiqueta

        df = pd.DataFrame(data=list(zip(peloLongo, pernaCurta, auau, animal)), columns=["Pelo Longo", "Perna Curta", "Auau", "Animal"])

        classificacao_decisionTree (df, "Animal", ["Pelo Longo", "Perna Curta", "Auau"], test_size= 0.1, plotGraph= True)

#-----------------------------------------------------------------------------------------------------------------------------

def equationModel (dataFrame, formula):
    #ex: formula: Porcoes ~ Farinha + Chocolate + Farinha:Chocolate"
    # O exemplo acima seria a seguinte formula -> Y = p1*Farinha + p2*Chocolate + p3*Farinha*Chocolate + intercepto + erro
    # ~ representa igual (=) em uma formula
    # : representa um parametro conjunto entre duas variaveis
    #Necessariamente o nome nas formulas deve ser nome de coluna do dataframe

    modelo = smf.ols(data= dataFrame, formula= formula).fit()

    # P > |t| para a variavel deve ser menor que 0.05 para ser uma variavel significativa na regressão.. se for maior que esse valor pode ser retirada.
    print (modelo.summary())

    print (modelo.params)

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
def relacoesVars (df):

    print ("Correlação")
    print (df.corr())

    print ("Covariância")
    print (df.cov())


#=============================================================================================================================
if __name__ == "__main__":

    dados = pd.read_csv(r"./arquivosTeste/Consumo_cerveja.csv", sep= ";")

    teste_regressaoLinear= False

    if (teste_regressaoLinear): 
        y= dados ["consumo"]
        X= dados [["temp_max", "chuva", "fds"]]
        
        relacoesVars(dados)

        modeloRegres= regressaoLinear(dados, yValue= "consumo", xValues= ["temp_max", "chuva", "fds"], plotGraph= True)

        dataPredict= mu.convertListToPandas (columnsList= [[30.5, 40.1], [12.2, 0.5], [0, 1]], nomesColunas= ["temp_max", "chuva", "fds"])
        print (dataPredict)
        print (modeloRegres.predict(dataPredict))

        saveModelo(modeloRegres, r"./arquivosTeste/Consumo_cerveja")
        modelo = loadModelo(r"./arquivosTeste/Consumo_cerveja")
        print (modelo.predict(dataPredict))
