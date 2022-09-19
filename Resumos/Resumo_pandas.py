import pandas as pd

#pandasObj.columns = ["col1", "col2", "col3"] #Set os nomes das colunas
#pandasObj["columnName"] #Acessa todos os dados de uma coluna
#pandasObj["columnName"].unique() #Retorna todos os valores unicos da serie de dados da coluna
#pandasObj["columnName"].value_counts() #Conta os valores e ordena do mais frequente para o menos frequente
#pandasObj["columnName"].mean() #Calcula a media de todos os valores
#pandasObj.columnName.plot(kind= "hist") #Plota os valores da coluna
#pandasObj.columnName.median() #Calcula a mediana dos valores da coluna
#pandasObj["columnName"].describe() #Descreve varios valores como media, quantidade, max, min e etc dos dados da coluna
#pandasObj.query("columnName==X") #Filtra todos os dados que tem o Valor X em columnName
#pandasObj.query("columnName!=X") #Filtra todos os dados que tem o Valor diferente de X em columnName
#pandasObj.query("columnName==X")["NotaColumn"].mean() #Filtra todos os dados que tem o Valor X em columnName
#pandasObj.groupby("columnName") #Agrupa todos os dados que tiverem o mesmo valor em columnName
#pandasObj.groupby("columnName").mean() #Calcula a media do grupo dos valores agrupados
#pandasObj["columnName"].index() #lista os indexes
#pandasObj["columnName"].values() #lista os valores
#pandasObj["columnName"].values_counts().to_frame() #Converte em data fram
#pandasObj["columnName"].loc["name"] #Localiza a linhas com o valor name
#pandasObj["columnName"].sum() #soma os valores
#dataF = pd.DataFrame(dados) #Cria um data frame com uma lista

#----------------------------------------------------------------------------------------------

#IMPORTANDO DADOS
#CSV
dados = pd.read_csv("path.csv", sep = ";")

#TXT
dados = pd.read_table("path.txt")

#XLSX
dados = pd.read_excel("path.xlsx")

#JSON
dados = pd.read_json("path.json")

#HTML tabelas em sites
dados = pd.read_html("url")
#caso tenha mais de uma tabela no site
dados[0]
dados[1]

#----------------------------------------------------------------------------------------------

#FUNCIONALIDADES

#Acessando uma coluna
dados["nomeColuna"]

#Apenas valores unicos
dados["nomeColuna"].unique()
dados["nomeColuna"].drop_duplicates()
#Utilizando o inplace, ele define dados como sendo o resultado sem valores repetidos
dados["nomeColuna"].drop_duplicates(inplace= True)

#Pegar uma parte dos dados para verificacao
dados.head(5)

#Apresentar as dimensoes do dataframe
dados.shape
dados.shape[0]
dados.shape[1]

#Obtendo os index
dados.index

#Modificar nome de uma coluna
dados["nomeColuna"].columns = "newName" #!

#Ordenar os unicos
sorted(dados["nomeColuna"].unique())

#Obtendo o minimo e max
dados["nomeColuna"].max()
dados["nomeColuna"].min()

#Contar valores e normalizar 
dados["nomeColuna"].value_counts(normalize= True)
percentual = dados["nomeColuna"].value_counts(normalize= True)*100





