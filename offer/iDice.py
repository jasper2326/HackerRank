import copy
import math


def thread(iEThreshold, cDThreshold, rPThreshold, characterNum):
    # load data
    data, elements = dataLoader()
    # get possible feature combinations
    candidates = getCandidates(characterNum)

    result = []
    final = []


    while candidates:
        p = candidates.pop(0)
        # validation
        if not p or len(p) == 0:
            break
        # get all subsets of p
        subsets = getSubstes(elements, p)
        # calculate impact evaluation of p
        iE = impactEvaluation(data, elements, p)
        if iE < iEThreshold:
            # remove all p's subsets
            for subset in subsets:
                if subset in candidates:
                    candidates.remove(subset)
            continue
        # calculate change rate
        cD = changeDection(data, elements, p)
        if cD < cDThreshold:
            continue
        # calculate isolation power of p and its subsets
        iP = isolationPower(data, elements, p)
        iPs = []
        for subset in subsets:
            iPs.append(isolationPower(data, elements, subset))
        # check if p's ip is greater than all its subsets
        if iP > max(iPs):
            result.append(p)
            for item in getSubstes(elements, p):
                if item in candidates:
                    candidates.remove(item)
    print(len(result))
    for p in result:
        rP = getRP(data, elements, p)
        if rP > rPThreshold:
            final.append([p, rP])


    def count0(word1):
        length = 0
        for char in word1:
            if char == '0':
                length += 1
        return length
    return sorted(final, key=count0)






def dataLoader():
    data = {}
    elements = set()
    file = open("data.txt", "r")

    for lines in file.readlines():
        line = lines.strip().split(',')
        # features are stored as a tuple
        key = ''.join(line[0:4])
        # values are stored as a list
        if key in elements:
            data[key].append([int(line[-2]), int(line[-1])])
        else:
            elements.add(key)
            data[key] = [[int(line[-2]), int(line[-1])]]


    return data, elements


def getCandidates(characterNum):
    digits = '0' * characterNum
    chr = ["0abc"]
    res = []
    for i in range(0, len(digits)):
        num = int(digits[i])
        tmp = []
        for j in range(0, len(chr[num])):
            if len(res):
                for k in range(0, len(res)):
                    tmp.append(res[k] + chr[num][j])
            else:
                tmp.append(str(chr[num][j]))
        res = copy.copy(tmp)

    def count0(word1):
        length = 0
        for char in word1:
            if char == '0':
                length += 1
        return length

    return sorted(res, key=count0, reverse=True)[1:]


def evaluate(source, target):
    # test if target is a subset of source
    for i in range(len(source)):
        if source[i] == '0':
            continue
        elif source[i] != target[i]:
            return False
    return True


def getSubstes(elements, p):
    # get all p's subsets in elements
    result = []
    for element in elements:
        if evaluate(p, element):
            result.append(element)
    return result


def impactEvaluation(data, elements, p):
    ie = 0
    for element in getSubstes(elements, p):
        ie += data[element][0][0]
    return ie


def changeDection(data, elements, p):
    cd = 0
    for element in getSubstes(elements, p):
        cd += abs(data[element][0][1] - data[element][0][0])
    return cd


def isolationPower(data, elements, p):
    ip = 0
    Xa, Xb, Oa, Ob = 0, 0, 0, 0
    for element in elements:
        Oa += data[element][0][1]
        Ob += data[element][0][0]
        if evaluate(p, element):
            Xa += data[element][0][1]
            Xb += data[element][0][0]
    pax, pbx = Xa/(Xa + Xb), Xb/(Xa + Xb)
    paxbar, pbxbar = (Oa - Xa)/(Oa + Ob - Xa - Xb), (Ob - Xb)/(Oa + Ob - Xa - Xb)
    return -(Xa * math.log2(1/pax) + Xb * math.log2(1/pbx)
             + (Oa - Xa) * math.log2(1/paxbar) + (Ob - Xb) * math.log2(1/pbxbar))/(Oa + Ob)



def getRP(data, elements, p):
    Xa, Xb, Oa, Ob = 0, 0, 0, 0
    for element in elements:
        Oa += data[element][0][1]
        Ob += data[element][0][0]
        if evaluate(p, element):
            Xa += data[element][0][1]
            Xb += data[element][0][0]
    pa, pb = Xa/Oa, Xb/Ob
    return pa * math.log2(pa/pb)


data, elements = dataLoader()
#print(data)
#print(elements)
cans = getCandidates(4)
#print(type(cans))
#print(cans)
#print(evaluate(('c', '0', '0', '0'), ('c', 'a', '0', '0')))
#print(getSubstes(elements, ('0', 'a', 'b', 'c')))
#print(impackEvaluation(data, elements, ('c', 'a', '0', '0')))
#print(changeDection(data, elements, ('c', 'a', '0', '0')))
#print(isolationPower(data, elements, ('c', 'a', '0', '0')))
#print(getRP(data, elements, ('a', '0', '0', '0')))

decide = sorted(thread(300, 100, 0.1, 4), key=lambda x: x[1], reverse=True)
print(decide)