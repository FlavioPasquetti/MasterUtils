import numpy as np
import os
import output as out
import math


#Abrir arquivo externamente
def openExt (path):
    os.startfile(path)


#Arredondar para uma base qualquer
def myround(x, base):
    val = base * round(x/base)
    val = round(val, 3)
    return val


#Funcao para espacamento dos valores escritos
def tabsSpace (stringBack, tabQ):
    scriptStringPart = ""

    for i in range(tabQ - int(len(str(stringBack))/4)):
        scriptStringPart += "\t"

    return scriptStringPart


#Funcao para encontrar a primeira linha que contenha uma determinada string em um arquivo aberto
def readToFind(fileOp, findString, findString2 = ""):

    while (True):
        lineString = fileOp.readline()
        if findString in lineString:
            break

        elif (findString2 != "" and findString2 in lineString):
            break

        #Fim do arquivo
        if not lineString:
            fileOp.seek(0,0)
            lineString = "EOF"
            break

    return lineString


def sciStr(floatOrInt):
    return str(np.format_float_scientific(float(floatOrInt), precision=5, exp_digits=3, min_digits=5))


def removeDuplicate(listA):
    l = []
    for i in listA:
        if i not in l:
            l.append(i)
    l.sort()
    return l

def difLists (listA, listB):
    l = []
    for i in listA:
        if i not in listB:
            l.append(i)

    for i in listB:
        if i not in listA:
            l.append(i)

    l = removeDuplicate(l)
    l.sort()
    return l

#convert unit Sempre recebe em metros 
def unitConv (valor, displayUnit):

    try:
        valor = float(valor)
    except:
        return valor
    
    displayMult = 1
    if displayUnit == "mm":
        displayMult = 1000

    elif displayUnit == "cm":
        displayMult = 100

    valor = valor * displayMult

    return valor


def addOffset (listValues, offset, index):
    
    #Verificando condicoes para funcionamento correto
    if (len(listValues) <= 0):
        return listValues
    elif (len(listValues[0]) <= index):
        return listValues
    
    #Loop na lista adicionando o offset
    for i in range(len(listValues)):
        
        try:  #Valor da lista e offset devem ser do mesmo tipo
            listValues[i][index] = listValues[i][index] + offset 
        except:
            pass
        
    return listValues


def addOffsetXYZ (listValues, offsetX, offsetY, offsetZ):
    
    #Verificando condicoes para funcionamento correto
    if (len(listValues.keys()) <= 0):
        return listValues
    elif (len(listValues.values()[0]) < 4):
        return listValues
    
    #Loop na lista adicionando o offset
    for nnod, coords in listValues.items():
        
        try:  #Valor da lista e offset devem ser do mesmo tipo
            coords[0] += offsetX
            coords[1] += offsetY
            coords[2] += offsetZ

            listValues[nnod] = coords
        except:
            pass
        
    return listValues
    

#Normalizar a partir de duas coordenadas
def normalize (cIni, cEnd):
    
    dif = [cEnd[0] - cIni[0], cEnd[1] - cIni[1], cEnd[2] - cIni[2]]

    maxValue = max(dif)
    minValue = min(dif)
    
    maxAbs = max(abs(maxValue), abs(minValue))

    norm = [0,0,0] 
    if (maxAbs != 0):
        norm = [dif[0]/maxAbs, dif[1]/maxAbs, dif[2]/maxAbs]

    return norm


#Vetor normal a partir de 3 pontos
def norm3points (nod1, nod2, nod3): 

    vec21 = [nod1[0] - nod2[0], nod1[1] - nod2[1], nod1[2] - nod2[2]]
    vec23 = [nod3[0] - nod2[0], nod3[1] - nod2[1], nod3[2] - nod2[2]]

    norm = [vec21[1]*vec23[2] - vec21[2]*vec23[1], 
            vec21[2]*vec23[0] - vec21[0]*vec23[2], 
            vec21[0]*vec23[1] - vec21[1]*vec23[0]]
    #matrix 
    #[[i  j  k ]
    # [x1 y1 z1]
    # [x2 y2 z2]]

    #normalizando
    maxValue = max(norm)
    norm = [0,0,0] 
    if (maxValue != 0):
        norm = [norm[0]/maxValue, norm[1]/maxValue, norm[2]/maxValue]

    return norm


#Multiplicação de Vetores
def multVec (vec1 , vec2, escalar = False, normalize = True):
    
    if (escalar):
        result = vec1[0]*vec2[0] + vec1[1]*vec2[1] + vec1[2]*vec2[2]
        
    else:
        result = [vec1[1]*vec2[2] - vec1[2]*vec2[1], 
                vec1[2]*vec2[0] - vec1[0]*vec2[2], 
                vec1[0]*vec2[1] - vec1[1]*vec2[0]]
        #matrix 
        #[[i  j  k ]
        # [x1 y1 z1]
        # [x2 y2 z2]]
        
    
        if (normalize): 
            try:
                maxValue = max(result)
                vecMult = [result[0]/maxValue, result[1]/maxValue, result[2]/maxValue]
            except:
                pass    
            
        
    return result


#Rotaracao de um vetor
def rotVec (vec, grausX, grausY, grausZ, precision = 5):

    radX = (float(grausX)*math.pi) / 180.0
    radY = (float(grausY)*math.pi) / 180.0
    radZ = (float(grausZ)*math.pi) / 180.0

    mRot = [[math.cos(radY)*math.cos(radZ), math.cos(radY)*math.sin(radZ), -math.sin(radY)], 
            [math.sin(radX)*math.sin(radY)*math.cos(radZ) - math.cos(radX)*math.sin(radZ), math.sin(radX)*math.sin(radY)*math.sin(radZ) + math.cos(radX)*math.cos(radZ), math.sin(radX)*math.cos(radY)],
            [math.cos(radX)*math.sin(radY)*math.cos(radZ) + math.sin(radX)*math.sin(radZ), math.cos(radX)*math.sin(radY)*math.sin(radZ) - math.sin(radX)*math.cos(radZ), math.cos(radX)*math.cos(radY)]]


    #multiplicando Vetor pelas matrizes
    vec = [ round(mRot[0][0]*vec[0] + mRot[0][1]*vec[1] + mRot[0][2]*vec[2], precision), 
            round(mRot[1][0]*vec[0] + mRot[1][1]*vec[1] + mRot[1][2]*vec[2], precision), 
            round(mRot[2][0]*vec[0] + mRot[2][1]*vec[1] + mRot[2][2]*vec[2], precision)]

    return vec


#Angulo entre vetores
def angVec(vec01, vec02):

    #vec01 = U
    #vec02 = V

    UV = multVec(vec01, vec02, True, False)

    modU = math.sqrt((vec01[0]**2) + (vec01[1]**2) + (vec01[2]**2))
    modV = math.sqrt((vec02[0]**2) + (vec02[1]**2) + (vec02[2]**2))

    ang = 0
    if (modU != 0 and modV != 0):
        cosO = UV/(modU*modV)
        ang = math.acos(cosO) * 180/math.pi

    return ang


def distPoints (point1, point2):

    return math.sqrt( ((point1[0] - point2[0])**2) + ((point1[1] - point2[1])**2) + ((point1[2] - point2[2])**2) )


# function to return key for any value
def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"


def globalToLocal (vecGlobal, vecLocal, vecConvert):

    #GLOBAL ----------------------------------------------------------------<
    totDist = ((vecGlobal[2]**2 + vecGlobal[1]**2 + vecGlobal[0]**2)**(1/2))
    horDist = (vecGlobal[1]**2 + vecGlobal[0]**2)**(1/2)

    if (horDist == 0 and vecGlobal[2] > 0): angVG = math.pi/2
    elif (horDist == 0 and vecGlobal[2] < 0): angVG = 3*math.pi/2
    elif (totDist == 0):  angVG = 0
    else: angVG = math.acos(horDist/totDist)

    if (vecGlobal[0] == 0 and vecGlobal[1] > 0): angHG = math.pi/2
    elif (vecGlobal[0] == 0 and vecGlobal[1] < 0): angHG = 3*math.pi/2
    elif (horDist == 0): angHG = 0
    else: angHG = math.acos(vecGlobal[0]/horDist)

    #LOCAL ----------------------------------------------------------------<
    totDist = ((vecLocal[2]**2 + vecLocal[1]**2 + vecLocal[0]**2)**(1/2))
    horDist = (vecLocal[1]**2 + vecLocal[0]**2)**(1/2)

    if (horDist == 0 and vecLocal[2] > 0): angVL = math.pi/2
    elif (horDist == 0 and vecLocal[2] < 0): angVL = 3*math.pi/2
    elif (totDist == 0):  angVL = 0
    else: angVL = math.acos(horDist/totDist)

    if (vecLocal[0] == 0 and vecLocal[1] > 0): angHL = math.pi/2
    elif (vecLocal[0] == 0 and vecLocal[1] < 0): angHL = 3*math.pi/2
    elif (horDist == 0): angHL = 0
    else: angHL = math.acos(vecLocal[0]/horDist)

    angV = (angVL - angVG)*180/math.pi
    angH = (angHL - angHG)*180/math.pi

    #ANG CONVERT ---------------------------------------------------------<
    #APLICANDO ANGULOS 
    vecConvert = rotVec(vecConvert,0,-angV,angH)

    return vecConvert

    
def nearPoint (coord, listCoords):

    lessDist = distPoints(coord, listCoords[0])
    nearCoord = listCoords[0]
    
    for coordInList in listCoords:

        dist = distPoints(coord, coordInList)

        if (dist < lessDist):
            lessDist = dist
            nearCoord = coordInList

    return nearCoord, lessDist


def largSectAnsys (secType, secShapeWs, dir):

    larg = 0

    if (secType == "I"):

        if (dir == "Y"): 
            larg = secShapeWs["w3"]
        elif (dir == "Z"): 
            larg = secShapeWs["w2"]

    elif (secType == "RECT"):
        
        if (dir == "Y"): 
            larg = secShapeWs["w2"]
        elif (dir == "Z"): 
            larg = secShapeWs["w1"]

    elif (secType == "CSOLID"):

        if (dir == "Y"): 
            larg = str(float(secShapeWs["w1"])*2)
        elif (dir == "Z"): 
            larg = str(float(secShapeWs["w1"])*2)

    elif (secType == "CTUBE"):

        if (dir == "Y"): 
            larg = str(float(secShapeWs["w2"])*2)
        elif (dir == "Z"): 
            larg = str(float(secShapeWs["w2"])*2)

    elif (secType == "CHAN"):

        if (dir == "Y"): 
            larg = secShapeWs["w3"]
        elif (dir == "Z"): 
            larg = secShapeWs["w2"]

    elif (secType == "L"):

        if (dir == "Y"): 
            larg = secShapeWs["w2"]
        elif (dir == "Z"): 
            larg = secShapeWs["w1"]

    elif (secType == "T"):

        if (dir == "Y"): 
            larg = secShapeWs["w2"]
        elif (dir == "Z"): 
            larg = secShapeWs["w1"]

    elif (secType == "HREC"):

        if (dir == "Y"): 
            larg = secShapeWs["w2"]
        elif (dir == "Z"): 
            larg = secShapeWs["w1"]

    return larg


def create_Folder (workPath):

    if not os.path.exists(workPath):
        os.makdir(workPath)


def extensionFormatValid (filepath, ext):
    return filepath.lower().endswith(ext)


def correctPath (path):
    if (path[-1] != "/"):
        path += "/"

    return path



#if (__name__ == "__main__"):


