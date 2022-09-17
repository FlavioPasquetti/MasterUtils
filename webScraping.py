from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup as bs
from urllib.error import URLError, HTTPError
import pandas as pd


#----------------------------------------------------------------------------------------------------------------------------

defaultHeaders = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Mobile Safari/537.36"}

#----------------------------------------------------------------------------------------------------------------------------


def trata_html (html):

    #Convertendo o tipo bytes para string
    html= html.decode("utf-8")
    #Eliminando caracteres de tabulaçao, quebra de linha e etc
    html= " ".join(html.split())
    #Eliminando espaços em branco entre as tags
    html= html.replace("> <", "><")

    return html

#----------------------------------------------------------------------------------------------------------------------------

def soupUrl (url):

    global defaultHeaders

    soup= None

    try:
        req= Request(url, headers= defaultHeaders)
        response= urlopen(req)
        html= response.read()
        html= trata_html(html)

        soup= bs(html, "html.parser")

    except HTTPError as e:
        print (e.status, e.reason)

    except URLError as e:
        print (e.reason)


    return soup

#----------------------------------------------------------------------------------------------------------------------------

def downloadImgSrc (imgSrc, outPath):

    urlretrieve(imgSrc, outPath)

#----------------------------------------------------------------------------------------------------------------------------

#soup.find("img") #Encontra a primeira tag "img"
#soup.findAll("img") #Lista todos as tags "img"
#soup("img") #Lista todos as tags "img"
#soup.findAll(["h1","h2","h3","h4","h5","h6"])
#soup.findAll("p", {"class":"txt-value"}) #Lista todos as tags p com o atributo class = txt-value
#soup.findAll(text = True) #Lista todos as tags com atributo text 
#soup.findAll(class_ = True) #Lista todos as tags com atributo class
#soup.find("h2").find_parent("div")  #Obtem a tag pai (tag maior) do h2 que seja uma div
#soup.find("h2").find_parents()  #Lista todos as tags pai do h2

#soup.find("h2").findNextSibling() #Obtem a proxima tag no mesmo nivel da h2
#soup.find("h2").findPreviousSibling() #Obtem a tag anterior no mesmo nivel da h2
#soup.find("h2").findPreviousSiblings() #Lista todas as tags anteriores no mesmo nivel da h2
#soup.find("h2").findNext() #Obtem a proxima tag depois de h2
#soup.find("h2").findPrevious()  #Obtem a tag anterios da h2
#soup.find("h2").findAllNext()   #Obtem todas as tags depois da h2
#getText() - Obtem o texto associado a tag
#soup.img.attrs / soup.img.attrs.keys() / soup.img.attrs.values() / soup.img["class"] / soup.img.get("class") - Acessando os atributos

#----------------------------------------------------------------------------------------------------------------------------

#RESUMO HTML

#TAGS
#<html> - Determina o inicio do documento
#<head> - Cabeçalho. Contém informações e configurações do documento
#<body> - É o corpo do documento, onde todo o conteudo é colocado. Esta é a parte visivel em um navegador

#<div> - Define uma divisão de pagina. Pode ser formatada de diversas maneiras
#<h1>, <h2>, ... - Marcadores de titulos
#<p> - Marcador de Paragrafo
#<a> - Hiperlink
#<img> - Exibição de Imagens
#<table> - Definição de Tabelas
#<ul>, <li> - Definição de Listas 

#ATRIBUTOS
#<.. id=valor> - valor unico em todo o documento
#<.. class=valor> - valor padrao para um determinado tipo de objeto, definido como uma classe




