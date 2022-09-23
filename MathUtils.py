from locale import normalize
import pandas as pd
from scipy.stats import binom, poisson, norm

#---------------------------------------------------------------------------------------------
#CONVERSAO PANDAS

def convertListToPandas (columnsList= [], nomesColunas= []):

    if (len(columnsList) != len(nomesColunas)): 
        return None

    df= pd.DataFrame (columnsList).transpose()
    df.columns = nomesColunas

    return df

#---------------------------------------------------------------------------------------------
#CONVERSAO PANDAS

def convertDictToPandas (dict= {}):
    
    #Conferindo se os valores são uma lista
    for key, valueDict in dict.items():

        if (type(valueDict) != list):
            listaValue= [valueDict]
            dict[key]= listaValue

    df= pd.DataFrame.from_dict(dict)

    return df

#---------------------------------------------------------------------------------------------
#AJUSTES DATAFRAME PANDAS

def renamePandas (df, axis, names):
    #axis= 0 = "columns" or 1 = "rows"
    
    if axis == 0:
        df.columns = names

    elif axis == 1:
        df.rows = names


def renameIndexAxisPandas (df, axis, names):
    #axis= 0 = "columns" or 1 = "rows"

    if axis == 0:
        df.rename_axis (names, axis= "columns", inplace= True)

    elif axis == 1:
        df.rename (index= names, inplace= True)


#---------------------------------------------------------------------------------------------
#CONVERSAO PANDAS
def listPandasColumn (df, nameColumn):

    return list(df[nameColumn])

#---------------------------------------------------------------------------------------------
#AJUSTES PANDAS
def ordenarIndex (df):

    df.sort_index(ascending= False, inplace= True)

#---------------------------------------------------------------------------------------------
#ESTATISTICA PANDAS

def estatisticaPandas (df, key, param0= None, param1= None, param2= None):
    #key = max, min, freq, prob, porc, media, median, descrip, segm, moda, quan, desvM, varian, desvP

    #-----------------------------------------------------------
    #max
    if (key== "max"):
        #param0 = columnName
        #param1 = numero de valores

        return df[param0].nlargest(param1)

    #-----------------------------------------------------------
    #min
    elif (key== "min"):
        #param0 = columnName
        #param1 = numero de valores

        return df[param0].nsmallest(param1)

    #-----------------------------------------------------------
    #frequencia
    elif (key== "freq"):
        #param0 = columnName
        #param1 = numero de valores
        
        return df[param0].value_counts().iloc[:param1]
    #-----------------------------------------------------------
    #probabilidade
    elif (key== "prob"):
        #param0 = columnName
        #param1 = numero de valores
        
        return df[param0].value_counts(normalize= True).iloc[:param1]

    #-----------------------------------------------------------
    #porcentagem
    elif (key== "porc"):
        #param0 = columnName
        #param1 = numero de valores
        
        return df[param0].value_counts(normalize= True).iloc[:param1]*100

    #-----------------------------------------------------------
    #media
    elif (key== "media"):
        #param0 = columnName
                
        return df[param0].mean()

    #-----------------------------------------------------------
    #mediana
    elif (key== "median"):
        #param0 = columnName
                
        return df[param0].median()

    #-----------------------------------------------------------
    #descricao
    elif (key== "descrip"):
        #param0 = columnName
                
        return df[param0].describe()
    
    #-----------------------------------------------------------
    #moda
    elif (key== "moda"):
        #param0 = columnName
                
        return df[param0].mode()

    #-----------------------------------------------------------
    #segment
    elif (key == "segm"):
        #Segmenta os dados em um conjunto de classes definidas
        #param0 = columnName
        #param1 = classes
        #param2 = labels

        freq = pd.value_counts ( pd.cut(x= df[param0],     
                                bins= param1, 
                                labels= param2, 
                                include_lowest= True) )

        prob = pd.value_counts ( pd.cut(x= df[param0],     
                                bins= param1, 
                                labels= param2, 
                                include_lowest= True), 
                                normalize= True )

        return pd.DataFrame({"Frequência" : freq, "Probabilidade" : prob})

    #-----------------------------------------------------------
    #quantile
    elif (key== "quan"):
        #param0 = columnName
        #param1 = fracao ou lista de fracoes/ se param0 = "default"
    
        if param1 == "default":
            return df[param0].quantile([0.25, 0.5, 0.75])
                        
        return df[param0].quantile(q = param1)
    
    #-----------------------------------------------------------
    #Desvio Medio Absoluto
    elif (key== "desvM"):
        #param0 = columnName

        return df[param0].mad()
    
    #-----------------------------------------------------------
    #Variancia
    elif (key== "varian"):
        #param0 = columnName

        return df[param0].var()
    
    #-----------------------------------------------------------
    #Desvio Padrao
    elif (key== "desvP"):
        #param0 = columnName

        return df[param0].std()

#---------------------------------------------------------------------------------------------
#PROBABILIDADE - Distribuicao Binomial

def Probabilidade_DistribBinomial (k, n, p, cumulativo= False):
    
    #p= probabilidade de sucesso evento unico
    #q= (1-p) = probabilidade de fracasso evento unico
    #n= numero de eventos estudados
    #k= numero de eventos desejados que tenham sucesso (pode ser uma lista)

    if (cumulativo):
        return binom.cdf(k,n,p)

    else:
        return binom.pmf(k,n,p)

#---------------------------------------------------------------------------------------------
#PROBABILIDADE - Distribuicao Poisson

def Probabilidade_DistribPoisson (k, u):

    #e= constante= 2.718281828459045
    #u= representa o numero medio de ocorrencias em um determinado intervalo de tempo ou espaco
    #k= numero de sucessos no intervalo desejado

    return poisson.pmf(k, u)

#---------------------------------------------------------------------------------------------
#PROBABILIDADE - Distribuicao Normal

def Probabilidade_DistribNormal (x, o, u, typeP= "cumulative"):

    #x= variavel normal
    #o= desvio padrao
    #u= media
    #typeP= cumulative, between, rest

    if (typeP== "cumulative"):
        Z= (x - u)/o

        return norm.cdf(Z)

    elif (typeP== "between"):
        Zinf= (x[0] - u)/o
        Zsup= (x[1] - u)/o

        return norm.cdf(Zsup) - norm.cdf(Zinf)

    elif (typeP== "rest"):
        Z= (x - u)/o

        return 1 - norm.cdf(Z)

#---------------------------------------------------------------------------------------------
#PROBABILIDADE - Intervalo de Confianca

def intervaloConfianca(significancia, media_amostral, sigma):

    #sigma= desvio padrao/ raiz(quantidade Amostra)
    
    return norm.interval (alpha= significancia, loc= media_amostral, scale= sigma)

#---------------------------------------------------------------------------------------------
#PROBABILIDADE - Quantidade Amostra

def tamanhoAmostra (z, e, o):

    #z= variavel normal padronizada - ex: caso queira 95% de confianca Z= norm.ppf(0.5 + (0.95/2))
    #o= desvio padrao populacional ou amostral (s) caso seja desconhecido o desvio padrao
    #e= erro inferencial - valor que pode ser variada a variavel normal ex: R$3000 +- 100.. o 100 seria o erro inferencial

    return (z*(o/e))**2

def tamanhoAmostra (N, z, o, e):

    #N= Tamanho da populacao
    #z= variavel normal padronizada - ex: caso queira 95% de confianca Z= norm.ppf(0.5 + (0.95/2))
    #o= desvio padrao populacional ou amostral (s) caso seja desconhecido o desvio padrao
    #e= erro inferencial - valor que pode ser variada a variavel normal ex: R$3000 +- 100.. o 100 seria o erro inferencial

    return ((z**2)*(o**2)*N) / ( ((z**2)*(o**2)) + (e**2)*(N-1) )

#============================================================================================



if __name__ == "__main__":

    teste_convertListToPandas= False
    teste_convertDictToPandas= False
    teste_listPandasColumn= False
    teste_renamePandas= False
    teste_estatisticaPandas= False
    teste_Distribuicoes= False
    teste_TeoremaLimiteCentral= True

    if (teste_convertListToPandas):
        dadosEmLista= ['laptop', 'printer', 'tablet', 'desk', 'chair']
        valorEmLista= [1000, 2000, 1500, 5000, 100]
        
        df= convertListToPandas([dadosEmLista, valorEmLista], ["Produtos", "Valor"]) 

        print (df)

    #---------------------------------------------------------------------------------------------

    if (teste_convertDictToPandas):

        dadosDict= {'laptop' : [1000], 'printer': [2000], 'tablet': 1500, 'desk': 5000, 'chair': 100}

        df= convertDictToPandas(dadosDict)

        print(df)

    #---------------------------------------------------------------------------------------------

    if (teste_listPandasColumn):

        dadosEmLista= ['laptop', 'printer', 'tablet', 'desk', 'chair']
        valorEmLista= [1000, 2000, 1500, 5000, 100]
        
        df= convertListToPandas([dadosEmLista, valorEmLista], ["Produtos", "Valor"]) 

        listValores= listPandasColumn(df, "Valor")

        print (listValores)

    #---------------------------------------------------------------------------------------------

    if (teste_renamePandas):

        dadosEmLista= ['laptop', 'printer', 'tablet', 'desk', 'chair']
        valorEmLista= [1000, 2000, 1500, 5000, 100]
        
        df= convertListToPandas([dadosEmLista, valorEmLista], ["Produtos", "Valor"]) 

        renamePandas(df, 0, ["teste1", "teste2"])

        renameIndexAxisPandas(df, 0, "teste")
        renameIndexAxisPandas(df, 1, {0: "valor1", 1: "valor2", 2: "valor3", 3: "valor4", 4: "valor5"})

        print (df)

    #---------------------------------------------------------------------------------------------

    if (teste_estatisticaPandas):

        df= pd.read_csv(r"./arquivosTeste/Curso de Estatística/dados.csv")

        labels= ["E", "D", "C", "B", "A"]
        classes= [0, 1576, 3152, 7880, 15760, 200000]
        
        pd.cut(x= df["Renda"], bins= classes, labels= labels, include_lowest= True)

        dfResult= estatisticaPandas (df, "segm", param0= "Renda", param1= classes, param2= labels)
        ordenarIndex(dfResult)
        print (dfResult)

        dfResult= estatisticaPandas(df, "quan", param0= "Renda", param1= "default")
        print (dfResult)

        df= pd.DataFrame( data= {"Fulanin": [8,10,4,8,6,10,8],
                                 "Beltrano": [10, 2, 0.5, 1, 3, 9.5, 10],
                                 "Sicrano": [7.5, 8, 7, 8, 8, 8.5, 7]},
                          index= ["Matemática", "Portugues", "Ingles", "Geografia",
                                  "Historia", "Fisica", "Quimica"])

        df.rename_axis("Matérias", axis= "columns", inplace= True)

        dfResult= estatisticaPandas (df, "min", param0= "Fulanin", param1= 2)
        dfResult= estatisticaPandas (df, "desvP", param0= "Fulanin")
        print (dfResult)

    #---------------------------------------------------------------------------------------------
    if (teste_Distribuicoes):

        k= [5,8]
        n= 10
        p= 1/4

        result= Probabilidade_DistribBinomial (k, n, p)
        print (result)

        u= 20
        k= 15

        result= Probabilidade_DistribPoisson (k, u)
        print (result)
        
        x= 1.8
        u= 1.7
        o= 0.1

        result= Probabilidade_DistribNormal(x, o, u)
        print (result)
        
    #---------------------------------------------------------------------------------------------
    if (teste_TeoremaLimiteCentral):

        n= 2000
        totalAmostra= 1500



