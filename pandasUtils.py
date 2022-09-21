import pandas as pd

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

def estatisticaPandas (df, key, param0= None, param1= None, param2= None, param3= None):
    #key = max, min, freq, prob, porc, media, median, descrip, segm

    #-----------------------------------------------------------

    #max
    if (key== "max"):
        #param0 = columnName
        #param1 = numero de valores

        return df[param0].nlargest(param1).values


    #-----------------------------------------------------------

    #min

    #-----------------------------------------------------------

    #frequencia

    #-----------------------------------------------------------

    #probabilidade

    #-----------------------------------------------------------

    #porcentagem

    #-----------------------------------------------------------

    #media

    #-----------------------------------------------------------

    #mediana

    #-----------------------------------------------------------

    #descricao

    #-----------------------------------------------------------

    if (key == "segm"):
        #segment
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




    

#============================================================================================

if __name__ == "__main__":

    teste_convertListToPandas= False
    teste_convertDictToPandas= False
    teste_listPandasColumn= False
    teste_renamePandas= False
    teste_estatisticaPandas= True

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

        df= pd.DataFrame( data= {"Fulanin": [8,10,4,8,6,10,8],
                                 "Beltrano": [10, 2, 0.5, 1, 3, 9.5, 10],
                                 "Sicrano": [7.5, 8, 7, 8, 8, 8.5, 7]},
                          index= ["Matemática", "Portugues", "Ingles", "Geografia",
                                  "Historia", "Fisica", "Quimica"])

        df.rename_axis("Matérias", axis= "columns", inplace= True)

        dfResult= estatisticaPandas (df, "max", param0= "Fulanin", param1= 2)
        teste= print (dfResult)
    