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

def sciStr(floatOrInt, precision = 5, exp_digit = 3, min_digits = 5):
    return str(np.format_float_scientific(float(floatOrInt), precision=precision, exp_digits=exp_digit, min_digits=min_digits))

#---------------------------------------------------------------------------------------------

def round(floatOrInt, precision = 5):
    return round(float(floatOrInt), precision)

#---------------------------------------------------------------------------------------------

def removeEspecialCaracters(inText):

    outText = inText.replace("|","").replace("/","").replace("\\","").replace("*","").\
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