import numpy as np
import pandas as pd



def thread():
    data = dataLoader()
    candidates = getCandidates()

    result = []
    final = []
    iEThreshold, cDThreshold, rPThreshold = 0, 0, 0


    while candidates:
        p = candidates.pop()
        if not p or len(p) == 0:
            break

        iE = impackEvaluation(p)
        if iE < iEThreshold:
            for item in getSubstes(p):
                candidates.remove(item)
            continue

        cD = changeDection(p)
        if cD < cDThreshold:
            continue


        iP = isolationPower(p)
        iPs = []
        for subset in getSubstes(p):
            iPs.append(isolationPower(subset))
        if iP > max(iPs):
            result.append(p)
        else:
            for item in getSubstes(p):
                candidates.remove(item)

    for p in result:
        rP = getRP(p)
        if rP < rPThreshold:
            result.remove(p)
        else:
            final.append([p, rP])

    return final






def dataLoader():
    data = []
    file = open("data.txt", "r")
    for line in file.readlines():
        data.append(line.strip().split(','))
    return data[1:]

def getCandidates():
    pass


def impackEvaluation(p):
    pass


def getSubstes(p):
    pass


def changeDection(p):
    pass


def isolationPower(p):
    pass


def getRP(p):
    pass



print(dataLoader())