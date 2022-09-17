from nltk import FreqDist as nltkFreqDist
import numpy as np

#---------------------------------------------------------------------------------------------

def maxTurbo (lista, nreturns= 1, key="escalar", out= "itens"):
    
    #key: escalar, frequencia
    #out: itens, values, all
    
    listReturn= [[],[]]
    
    if key=="escalar":
        for ret in range(nreturns):
            listReturn[0].append(max(lista))
            listReturn[1].append(max(lista))
            lista.remove(max(lista))
    
    elif key=="frequencia":
        freqList= nltkFreqDist(lista)
        results= (freqList.most_common(nreturns))
        
        listItens= []
        listValues= []
        for item in results:
            listItens.append(item[0])
            listValues.append(item[1])
            
        listReturn[0]= listItens
        listReturn[1]= listValues
        
    elif key=="probabilidade":
        freqList= nltkFreqDist(lista)
        results= (freqList.most_common(nreturns))
        
        listItens= []
        listValues= []
        for item in results:
            listItens.append(item[0])
            listValues.append(item[1]/len(lista))
            
        listReturn[0]= listItens
        listReturn[1]= listValues
        
    
    #RETURNS
    if len(listReturn[0]) == 1:
        if (out == "itens"):
            return listReturn[0][0]
        elif (out == "values"):
            return listReturn[1][0]
        else:
            return listReturn[0][0], listReturn[1][0]
    
    else:
        if (out == "itens"):
            return listReturn[0]
        elif (out == "values"):
            return listReturn[1]
        else:
            return listReturn[0], listReturn[1]

#---------------------------------------------------------------------------------------------

def round(floatOrInt, precision = 5):
    return round(float(floatOrInt), precision)

#---------------------------------------------------------------------------------------------

def sciStr(floatOrInt, precision = 5, exp_digit = 3, min_digits = 5):
    return str(np.format_float_scientific(float(floatOrInt), precision=precision, exp_digits=exp_digit, min_digits=min_digits))