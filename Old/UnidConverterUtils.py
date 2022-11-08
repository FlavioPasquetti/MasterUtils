


def comprimento (value, inUnid, outUnid):

    inMult = 1
    if (inUnid == "m"): inMult = 1
    elif (inUnid == "cm"): inMult = 100
    elif (inUnid == "mm"): inMult = 1000

    outMult = 1
    if (outUnid == "m"): outMult = 1
    elif (outUnid == "cm"): outMult = 100
    elif (outUnid == "mm"): outMult = 1000

    return value*outMult/inMult

#---------------------------------------------------------------------------------------------

def area (value, inUnid, outUnid):

    inMult = 1
    if (inUnid == "m"): inMult = 1
    elif (inUnid == "cm"): inMult = 100
    elif (inUnid == "mm"): inMult = 1000

    outMult = 1
    if (outUnid == "m"): outMult = 1
    elif (outUnid == "cm"): outMult = 100
    elif (outUnid == "mm"): outMult = 1000

    return value*(outMult*outMult)/(inMult*inMult)

#---------------------------------------------------------------------------------------------

def force (value, inUnid, outUnid):

    inMult = 1
    if (inUnid == "n"): inMult = 1
    elif (inUnid == "kn"): inMult = 0.001
    elif (inUnid == "tonf"): inMult = 0.00010197

    outMult = 1
    if (outUnid == "n"): outMult = 1
    elif (outUnid == "kn"): outMult = 0.001
    elif (outUnid == "tonf"): outMult = 0.00010197

    return value*outMult/inMult

#---------------------------------------------------------------------------------------------

def press (value, inUnidForce, inUnidLength, outUnidForce, outUnitLength):

    inMultForce = 1
    if (inUnidForce == "n"): inMultForce = 1
    elif (inUnidForce == "kn"): inMultForce = 0.001
    elif (inUnidForce == "tonf"): inMultForce = 0.00010197

    outMultForce = 1
    if (outUnidForce == "n"): outMultForce = 1
    elif (outUnidForce == "kn"): outMultForce = 0.001
    elif (outUnidForce == "tonf"): outMultForce = 0.00010197

    inMultLength = 1
    if (inUnidLength == "m"): inMultLength = 1
    elif (inUnidLength == "cm"): inMultLength = 100
    elif (inUnidLength == "mm"): inMultLength = 1000

    outMultLength = 1
    if (outUnitLength == "m"): outMultLength = 1
    elif (outUnitLength == "cm"): outMultLength = 100
    elif (outUnitLength == "mm"): outMultLength = 1000

    return value*(outMultForce/inMultForce)/((outMultLength*outMultLength)/(inMultLength*inMultLength))

#---------------------------------------------------------------------------------------------

def moment (value, inUnidForce, inUnidLength, outUnidForce, outUnitLength):

    inMultForce = 1
    if (inUnidForce == "n"): inMultForce = 1
    elif (inUnidForce == "kn"): inMultForce = 0.001
    elif (inUnidForce == "tonf"): inMultForce = 0.00010197

    outMultForce = 1
    if (outUnidForce == "n"): outMultForce = 1
    elif (outUnidForce == "kn"): outMultForce = 0.001
    elif (outUnidForce == "tonf"): outMultForce = 0.00010197

    inMultLength = 1
    if (inUnidLength == "m"): inMultLength = 1
    elif (inUnidLength == "cm"): inMultLength = 100
    elif (inUnidLength == "mm"): inMultLength = 1000

    outMultLength = 1
    if (outUnitLength == "m"): outMultLength = 1
    elif (outUnitLength == "cm"): outMultLength = 100
    elif (outUnitLength == "mm"): outMultLength = 1000

    return value*(outMultForce/inMultForce)*(outMultLength/inMultLength)