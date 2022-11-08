import numpy as np

#---------------------------------------------------------------------------------------------

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

#---------------------------------------------------------------------------------------------

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

#---------------------------------------------------------------------------------------------

def removeEspecialCaracters(inText):

    outText =  inText.replace("|","").replace("/","").replace("\\","").replace("*","").\
              replace("$","").replace("^","").replace('"',"").replace("'","").replace(";","").\
              replace(" ","").replace("-","").replace(".","").replace(",","").replace("ç","").\
              replace("(","").replace(")","").replace("ã","").replace("á","")

    return outText

#---------------------------------------------------------------------------------------------

def float_setCientificFormat (value, precision= 2, exp_digits= 2, min_caract= 2):
    return np.format_float_scientific(value, exp_digits=exp_digits, precision=precision, min_digits=min_caract)

#---------------------------------------------------------------------------------------------

def str_defineNumCaracteres (value, caracters):

    value= str(value)
    if (len(value) > caracters):
        cut= len(value) - caracters
        return value[cut:]
    
    elif (len(value) < caracters):
        addblank= caracters - len(value)
        value= " "*addblank + value

    return value        